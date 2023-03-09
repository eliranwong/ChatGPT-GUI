import config, sys, traceback, openai
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
    progress = Signal(int)


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
        #self.kwargs['progress_callback'] = self.signals.progress

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

    def getResponse(self, messages):
        responses = ""
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                n=config.chatGPTApiNoOfChoices,
                temperature=config.chatGPTApiTemperature,
            )
            for index, choice in enumerate(completion.choices):
                chat_response = choice.message.content
                if len(completion.choices) > 1:
                    if index > 0:
                        responses += "\n"
                    responses += f"### Response {(index+1)}:\n"
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
        return responses

    def workOnGetResponse(self, messages):
        # Pass the function to execute
        worker = Worker(self.getResponse, messages) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.parent.processResponse)
        # Connection
        #worker.signals.finished.connect(None)
        # Execute
        self.threadpool.start(worker)
