import config, sys, traceback, openai, os, json
if config.qtLibrary == "pyside6":
    from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool
else:
    from qtpy.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(str)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # assign a reference to this current thread
        #config.workerThread = QThread.currentThread()

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class ChatGPTResponse:

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.threadpool = QThreadPool()

    def getResponse(self, messages, progress_callback):
        responses = ""
        try:
            if config.chatGPTApiNoOfChoices == 1 and (config.chatGPTApiFunctionCall == "none" or not config.chatGPTApiFunctionSignatures):
                completion = openai.ChatCompletion.create(
                    model=config.chatGPTApiModel,
                    messages=messages,
                    max_tokens=config.chatGPTApiMaxTokens,
                    temperature=config.chatGPTApiTemperature,
                    n=config.chatGPTApiNoOfChoices,
                    stream=True,
                )
                progress_callback.emit("\n\n~~~ ")
                for event in completion:
                    # stop generating response
                    stop_file = ".stop_chatgpt"
                    if os.path.isfile(stop_file):
                        os.remove(stop_file)
                        break                                    
                    # RETRIEVE THE TEXT FROM THE RESPONSE
                    event_text = event["choices"][0]["delta"] # EVENT DELTA RESPONSE
                    progress = event_text.get("content", "") # RETRIEVE CONTENT
                    # STREAM THE ANSWER
                    progress_callback.emit(progress)
            else:
                if config.chatGPTApiFunctionSignatures:
                    completion = openai.ChatCompletion.create(
                        model=config.chatGPTApiModel,
                        messages=messages,
                        max_tokens=config.chatGPTApiMaxTokens,
                        temperature=config.chatGPTApiTemperature,
                        n=config.chatGPTApiNoOfChoices,
                        functions=config.chatGPTApiFunctionSignatures,
                        function_call=config.chatGPTApiFunctionCall,
                    )
                else:
                    completion = openai.ChatCompletion.create(
                        model=config.chatGPTApiModel,
                        messages=messages,
                        max_tokens=config.chatGPTApiMaxTokens,
                        temperature=config.chatGPTApiTemperature,
                        n=config.chatGPTApiNoOfChoices,
                    )

                response_message = completion["choices"][0]["message"]
                if response_message.get("function_call"):
                    function_name = response_message["function_call"]["name"]
                    if function_name == "python":
                        config.pythonFunctionResponse = ""
                        function_args = response_message["function_call"]["arguments"]
                        insert_string = "import config\nconfig.pythonFunctionResponse = "
                        if "\n" in function_args:
                            substrings = function_args.rsplit("\n", 1)
                            new_function_args = f"{substrings[0]}\n{insert_string}{substrings[-1]}"
                        else:
                            new_function_args = f"{insert_string}{function_args}"
                        try:
                            exec(new_function_args, globals())
                            function_response = str(config.pythonFunctionResponse)
                        except:
                            function_response = function_args
                        info = {"information": function_response}
                        function_response = json.dumps(info)
                    else:
                        #if not function_name in config.chatGPTApiAvailableFunctions:
                        #    print("unexpected function name: ", function_name)
                        fuction_to_call = config.chatGPTApiAvailableFunctions.get(function_name, "integrate_google_searches")
                        try:
                            function_args = json.loads(response_message["function_call"]["arguments"])
                        except:
                            function_args = response_message["function_call"]["arguments"]
                            if function_name == "integrate_google_searches":
                                function_args = {"keywords": function_args}
                        function_response = fuction_to_call(function_args)
                    
                    # check function response
                    # print("Got this function response:", function_response)

                    # process function response
                    # send the info on the function call and function response to GPT
                    messages.append(response_message) # extend conversation with assistant's reply
                    messages.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )  # extend conversation with function response
                    if config.chatAfterFunctionCalled:
                        return self.getResponse(messages, progress_callback)
                    else:
                        responses += f"{function_response}\n\n"

                for index, choice in enumerate(completion.choices):
                    chat_response = choice.message.content
                    if chat_response:
                        if len(completion.choices) > 1:
                            if index > 0:
                                responses += "\n"
                            responses += f"~~~ Response {(index+1)}:\n"
                        responses += f"{chat_response}\n\n"
        # error codes: https://platform.openai.com/docs/guides/error-codes/python-library-error-types
        except openai.error.APIError as e:
            #Handle API error here, e.g. retry or log
            return f"OpenAI API returned an API Error: {e}"
        except openai.error.APIConnectionError as e:
            #Handle connection error here
            return f"Failed to connect to OpenAI API: {e}"
        except openai.error.RateLimitError as e:
            #Handle rate limit error (we recommend using exponential backoff)
            return f"OpenAI API request exceeded rate limit: {e}"
        except:
            #traceback.print_exc()
            responses = traceback.format_exc()
        return responses

    def workOnGetResponse(self, messages):
        # Pass the function to execute
        worker = Worker(self.getResponse, messages) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.parent.processResponse)
        worker.signals.progress.connect(self.parent.printStream)
        # Connection
        #worker.signals.finished.connect(None)
        # Execute
        self.threadpool.start(worker)


class OpenAIImage:

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.threadpool = QThreadPool()

    def getResponse(self, prompt, progress_callback=None):
        try:
            #https://platform.openai.com/docs/guides/images/introduction
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024",
            )
            return response['data'][0]['url']
        # error codes: https://platform.openai.com/docs/guides/error-codes/python-library-error-types
        except openai.error.APIError as e:
            #Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
        except openai.error.APIConnectionError as e:
            #Handle connection error here
            print(f"Failed to connect to OpenAI API: {e}")
        except openai.error.RateLimitError as e:
            #Handle rate limit error (we recommend using exponential backoff)
            print(f"OpenAI API request exceeded rate limit: {e}")
        except:
            traceback.print_exc()
        return ""

    def workOnGetResponse(self, prompt):
        # Pass the function to execute
        worker = Worker(self.getResponse, prompt) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.parent.displayImage)
        # Connection
        #worker.signals.finished.connect(None)
        # Execute
        self.threadpool.start(worker)
