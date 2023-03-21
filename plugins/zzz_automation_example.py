import config, openai, re
from datetime import datetime


"""
A plugin example to generate multiple chat responses and save in database file.
"""


def loadResponses(predefinedContext, userInput):
    # title
    title = re.sub("\n", " ", userInput)[:50]

    #messages
    messages = [
        {"role": "system", "content" : "You’re a kind helpful assistant"}
    ]
    if predefinedContext in config.predefinedContexts:
        context = config.predefinedContexts[predefinedContext]
        if context:
            messages.append({"role": "assistant", "content" : context})
    messages.append({"role": "user", "content": userInput})

    # responses
    responses = f">>> {userInput}\n\n"
    try:
        completion = openai.ChatCompletion.create(
            model=config.chatGPTApiModel,
            messages=messages,
            max_tokens=config.chatGPTApiMaxTokens,
            temperature=config.chatGPTApiTemperature,
            n=config.chatGPTApiNoOfChoices,
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
        responses = f"OpenAI API returned an API Error: {e}"
    except openai.error.APIConnectionError as e:
        #Handle connection error here
        responses = f"Failed to connect to OpenAI API: {e}"
    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        responses = f"OpenAI API request exceeded rate limit: {e}"

    # process responses
    for t in config.chatGPTTransformers:
        responses = t(responses)
    responses = re.sub("\n\n[\n]+?([^\n])", r"\n\n\1", responses)

    id = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    config.chatGPTApi.database.insert(id, title, responses)


# automate saving responses in database file
userInputs = (
    #"Tell me about ChatGPT",
)
predefinedContexts = (
    "[none]",
)
if userInputs:
    for userInput in userInputs:
        for predefinedContext in predefinedContexts:
            try:
                loadResponses(predefinedContext, userInput)
            except:
                print(f"Failed processing '{predefinedContext}' - '{userInput}'!")
