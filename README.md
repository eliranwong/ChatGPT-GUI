# ChatGPT-GUI

## ChatGPT Graphical User Interface

A Qt-based graphical user interface application for ChatGPT API.  Both ChatGPT-3 and ChatGPT-4 are supported.

Repository: https://github.com/eliranwong/ChatGPT-GUI

Developer: Eliran Wong

<img width="1243" alt="screenshot" src="https://user-images.githubusercontent.com/25262722/227805265-bd26c0c9-9c6a-4e4d-83c9-3e27ea3d3c7e.png">

# Background

We integrated ChatGPT in one of our gui applications, [UniqueBible.app](https://github.com/eliranwong/UniqueBible/wiki/Bible-Chat-with-ChatGPT-API).  Here in this project, we modify the codes to make ChatGPT-GUI as a standalone application for wider purposes.

# Cross-platform

Winodws, macOS, Linux, ChromeOS are supported.

You may also run on Android via Termux.

# ChatGPT API

This application is Qt-based graphical user interface that uses OpenAI ChatGPT API to generate chat conversations.

Users need to register an OpenAI account and generate a API key first.

Read pricing at: https://openai.com/pricing

Generate API key at: https://platform.openai.com/account/api-keys

# For ChatGPT-4 Users

ChatGPT-GUI supports both ChatGPT-3 and ChatGPT-4.

ChatGPT-GUI uses 'gpt-3-turbo' by default.  To use ChatGPT-4:

1. Make sure you have access to 'gpt-4' or 'gpt4-32k' with your OpenAI API key
2. Select 'gpt-4' or 'gpt4-32k' as API Model in 'Chat Settings'
3. Enter BOTH 'OpenAI API Key' AND 'Organization ID' in 'Chat Settings'

# Difference between "ChatGPT-GUI" interface and ChatGPT web version

ChatGPT web version is available at: https://chat.openai.com/chat

"ChatGPT-GUI" uses the same model, but with enhanced features not available at ChatGPT web version.

With "ChatGPT-GUI", users can:

* include latest internet search results in ChatGPT responses

* enter multiline-message

* predefine context for conversations.  With "ChatGPT-GUI", users can specify a context for conversations.  For example, enter "talk about English literature" as the chat context in "Chat Settings", to get ChatGPT responses related to "English literature".  In addition, users can can choose to apply their customised contexts only in the beginning of a chat or all inputs.

* adjust temperature [What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.]

* adjust number of choices in ChatGPT responses [How many chat completion choices to generate for each input message.]

* adjust font size for text display

* use python plugins, to automate tasks, add predefined context, or to process ChatGPT responses before they are displayed

* edit, print and save conversations

* save conversations for offline use

* search history, based on title or content

* perform search and replace on chat content

* oranize chat history into different separate database files

* enter message with voice-typing

* use OpenAI image model to generate images

* support system tray

* choose to use regular expression for search and replace

# Setup

For Windows users:

> https://github.com/eliranwong/ChatGPT-GUI/wiki/Setup-%E2%80%90-Windows

For macOS, Linux, ChromeOS users

> https://github.com/eliranwong/ChatGPT-GUI/wiki/Setup-%E2%80%90-macOS,-Linux,-ChromeOS

# QuickStart

1) Launch ChatGPT-GUI by running "python3 ChatGPT-GUI.py"
2) Click the "[Settings](https://github.com/eliranwong/ChatGPT-GUI#chat-settings)" button to enter your own OpenAI API key
3) Enter your message and click the "Send" button, to start a conversation

# User Interface

Graphical User Interface

> https://github.com/eliranwong/ChatGPT-GUI/wiki/UI-%E2%80%90-Graphical-User-Interface

Chat Settings

> https://github.com/eliranwong/ChatGPT-GUI/wiki/UI-%E2%80%90-Chat-Settings

# Include Latest Internet Search Results

https://github.com/eliranwong/ChatGPT-GUI/wiki/Include-Latest-Internet-Search-Results

# Plugins

ChatGPT-GUI supports plugins, written in python, to extend functionalities.

How to use python plugins to process ChatGPT responses before they are displayed?

https://github.com/eliranwong/ChatGPT-GUI/wiki/Plugins-%E2%80%90-Transform-ChatGPT-Responses

How to use plugins to customize input suggestion?

> https://github.com/eliranwong/ChatGPT-GUI/wiki/Plugins-%E2%80%90-Input-Suggestions

How to use plugins to customize predefined contexts?

> https://github.com/eliranwong/ChatGPT-GUI/wiki/Plugins-%E2%80%90-Predefined-Contexts

How to use ChatGPT function calling features with plugins?

> https://github.com/eliranwong/ChatGPT-GUI/wiki/Plugins-%E2%80%90-ChatGPT-Function-Calling

# FAQ - Frequently Asked Questions

https://github.com/eliranwong/ChatGPT-GUI/wiki/FAQ-%E2%80%90-Frequently-Asked-Questions