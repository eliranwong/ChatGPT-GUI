"""
This example uses embedchain to search for keywords with google and write a summary.
"""

import os

import googlesearch
from embedchain import App
from embedchain.config import LlmConfig

from package import config

os.environ["OPENAI_API_KEY"] = config.openaiApiKey

# Create a bot instance
search_bot = App()

searchInput = input("Search keywords: ")

# Embed online resources
for i in googlesearch.search(searchInput):
    try:
        search_bot.add(i)
    except:
        pass

# Query the bot
query_config = LlmConfig(max_tokens=config.chatGPTApiMaxTokens)
answer = search_bot.query(
    f"Write a summary about {searchInput}", config=query_config)
print(answer)
