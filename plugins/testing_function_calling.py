import json
from package import config


# modified from source: https://platform.openai.com/docs/guides/gpt/function-calling

def get_current_weather(function_args):
    # retrieve argument values from a dictionary
    location = function_args.get("location") # required
    unit=function_args.get("unit", "fahrenheit") # optional

    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

functionSignature = {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA",
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
    },
}

config.chatGPTApiFunctionSignatures.append(functionSignature)
config.chatGPTApiAvailableFunctions["get_current_weather"] = get_current_weather
