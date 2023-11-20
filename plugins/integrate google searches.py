import json

import googlesearch

from package import config

# Use google https://pypi.org/project/googlesearch-python/ to search internet for information, about which ChatGPT doesn't know.


def integrate_google_searches(function_args):
    # retrieve argument values from a dictionary
    # print(function_args)
    keywords = function_args.get("keywords")  # required

    info = {}
    for index, item in enumerate(googlesearch.search(keywords, advanced=True, num_results=config.maximumInternetSearchResults)):
        info[f"information {index}"] = {
            "title": item.title,
            "url": item.url,
            "description": item.description,
        }
    return json.dumps(info)


functionSignature = {
    "name": "integrate_google_searches",
    "description": "Search internet for keywords when ChatGPT does not have information",
    "parameters": {
        "type": "object",
        "properties": {
            "keywords": {
                "type": "string",
                "description": "keywords for searches, e.g. ChatGPT",
            },
        },
        "required": ["keywords"],
    },
}

config.integrate_google_searches_signature = [functionSignature]
config.chatGPTApiFunctionSignatures.insert(0, functionSignature)
config.chatGPTApiAvailableFunctions["integrate_google_searches"] = integrate_google_searches
