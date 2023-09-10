"""
This example uses embedchain to search for keywords with google and write a summary.
"""

from embedchain import App
import googlesearch, config, os
from embedchain.config import LlmConfig

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
answer = search_bot.query(f"Write a summary about {searchInput}", config=query_config)
print(answer)