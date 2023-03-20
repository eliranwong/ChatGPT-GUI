# ChatGPT-GUI

## ChatGPT Graphical User Interface

A Qt-based graphical user interface application for ChatGPT API

Developer: Eliran Wong

![screenshot1](https://user-images.githubusercontent.com/25262722/225602529-10d04bec-2412-4a1c-ae4c-d9f891a18dbe.png)

# Background

We have used Qt to develop [a gui for using ChatGPT for bible study with UniqueBible.app](https://github.com/eliranwong/UniqueBible/wiki/Bible-Chat-with-ChatGPT-API).  Here in this project, we modify the code to make it as a standalone application for general purpose.

# Cross-platform

Winodws, macOS, Linux, ChromeOS are supported.

You may also run on Android via Termux.

# ChatGPT API

This application is Qt-based graphical user interface that uses OpenAI ChatGPT API to generate chat conversations.

Users need to register an OpenAI account and generate a API key first.

Read pricing at: https://openai.com/pricing

Generate API key at: https://platform.openai.com/account/api-keys

# Difference between "ChatGPT-GUI" interface and ChatGPT web version

ChatGPT web version is available at: https://chat.openai.com/chat

"ChatGPT-GUI" uses the same model, but with enhanced features not available at ChatGPT web version.

With "ChatGPT-GUI", users can:

* enter message in multiline-input

* start conversation with a particular context.  With "ChatGPT-GUI", users can specify a context for conversations.  For example, in our screenshots we set "talk about English literature" as the chat context.  This tells ChatGPT to give related responses.

* adjust temperature [What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.]

* adjust number of choices in ChatGPT responses [How many chat completion choices to generate for each input message.]

* adjust font size

* use python plugins to process ChatGPT responses before they are displayed

* save conversations for offline use

* search history, based on title or content

* edit and save conversations

* search and replace chat content

* support multiple database files for storing offline records; it helps users to organize different topics/categories/studies in separate files.

* enter message with voice-typing

* use OpenAI image model to generate images

* support system tray

* choose to use regular expression for search and replace

# Download and Setup (Windows)

Run in terminal:

> git clone https://github.com/eliranwong/ChatGPT-GUI.git

> cd ChatGPT-GUI

> python -m venv venv

> .\venv\Scripts\activate

> pip3 install PySide6 openai gtts pyqtdarktheme

Install 'pocketsphinx' to support voice-typing [optional]:

> pip3 install pocketsphinx

Alternatives to PySide6 [optional]:

"ChatGPT-GUI" supports either PySide6, PySide2 or PyQt5.  You may use PySide2 or PyQt5 instead of PySide6, run

> pip3 install qtpy PySide2 PyQt5

In config.py, change "qtLibrary" to either "pyside2" or "pyqt5", e.g.:

> qtLibrary = 'pyside2'

# Run (Windows)

Run in terminal:

> cd ChatGPT-GUI

> .\venv\Scripts\activate

> python ChatGPT-GUI.py

# Download and Setup (macOS, Linux, ChromeOS)

Run in terminal:

> git clone https://github.com/eliranwong/ChatGPT-GUI.git

> cd ChatGPT-GUI

> python3 -m venv venv

> source venv/bin/activate

> pip3 install PySide6 openai gtts pyqtdarktheme

Install 'pocketsphinx' to support voice-typing [optional]:

> pip3 install pocketsphinx

Alternatives to PySide6 [optional]:

"ChatGPT-GUI" supports either PySide6, PySide2 or PyQt5.  You may use PySide2 or PyQt5 instead of PySide6, run

> pip3 install qtpy PySide2 PyQt5

In config.py, change "qtLibrary" to either "pyside2" or "pyqt5", e.g.:

> qtLibrary = 'pyside2'

# Run (macOS, Linux, ChromeOS)

Run in terminal:

> cd ChatGPT-GUI

> source venv/bin/activate

> python3 ChatGPT-GUI.py

# QuickStart

![screenshot2](https://user-images.githubusercontent.com/25262722/225602535-eaf2a1f9-c2d6-4e3c-8997-24216a2d8dab.png)

1) Launch ChatGPT-GUI by running "python3 ChatGPT-GUI"
2) Click "Settings" to enter your own OpenAI API key.  You may optionally specify a chat context there.
3) Enter your message in message entry field and press Enter key, to start a conversation

# Graphical User Interface

The ChatGPT-GUI Window is separated into left and right areas, by a movable splitter.  Users can move the splitter to either end to hide one of them. 

On the Left, from top to bottom:

* search entry and button for title - enter text here to search for a title, that contains the entered text, in saved record.  You may either press the button or press the "Enter" key after text entry.

* search entry and button for content - enter text here to search for a content, that contains the entered text, in saved record.  You may either press the button or press the "Enter" key after text entry.

* record list - list of saved records or search results.  Select a record to update the content view on the right.

* "Remove" & "Clear All" buttons - remove selected record or remove all records.  Confirmation is required before you proceed the deletion.

* "Help" button - open this wiki page

On the right, from top to bottom:

* message input - users enter a message here to begin or continue a conversation.  The voice checkbox toggle voice-typing.  The send button sends the message.  Alternately, users can press the "Enter" key after text entry.  When a message is sent, a progress bar is displayed to indicate that the message is being processed.

* \+ / - button - toggle multiline user input for message entry

* chat or image - this determines whether the message to sent to generate a chat response or an image.

* content view - display conversation content

* Search and Replace - update content with search and replace; "Repace" button replaces selected text only; "ALL" button replaces all strings that matches search input.

* Control interface:

- Settings - open "Settings" dialog, where you can enter OpenAI API key, orgnisation ID, conversation context, text-to-speech language.

- Temperature - according to OpenAI documentation, temperature means "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."

- Choices - according to OpenAI documentation, choices means "How many chat completion choices to generate for each input message."

- Font - edit the font size of chat record list and content view

- Editable checkbox - toggles to edit the content view or make it read-only

- "New" - open a new conversation

- "Save" saves edited conversation.  Each conservation is automatically saved when a new response is loaded.  Users may edit and updated the content with this button.

Application menu:

* New Database - create a new database file

* Open Database - open an existing database file

* Save Database as - duplicate the currently opened database a different file

* New Chat - create a new chat

* Save Chat - save chat content

* Print Chat - print chat content

* Configure - open settings dialog

* Toggle Dark Theme - toggle between dark and light theme

* Toggle System Tray - toggle system tray; restart the application is required

* Toggle Regular Expression - toggle regular expression for search and replace

* Exit - Exit the application

# FAQ - Frequently Asked Questions

How to edit a record's title?

> Edit the first line of a record to change its title.

Where are database files stored?

> Chat database file is stored in folder "chats" by default.  The default file is named as "default.chat"

What is the format of the database files?

> We use ".chat" as extension for database files to work with the GUI.  They are all standard sqlite files.

Can I change the context to make the conversation context to focus on a particular area?

> Yes.  Click the "Settings" button to edit the chat context.  The default is empty.  Change it to the topic you want to focus in your conversations.

Can I change the language of the interface?

> Yes, simply edit the 'thisTranslation' entry in file 'config.py'.

How to use python plugins to process ChatGPT responses before they are displayed?

Create a python file and save it in folder "plugins".

For example, print response on console in addition to displayint it on GUI:
> import config<br>
> <br>
> def printOnConsole(text):<br>
>     print(text)
>     return text<br>
> <br>
> config.chatGPTTransformers.append(printOnConsole)<br>

You may even modify the content before it is displayed on the GUI.

In the python file, append the method that transform the response to config.chatGPTTransformers

For example, change all characters to upper cases:
> import config<br>
> <br>
> def convertToUpperCases(text):<br>
>     return text.upper()<br>
> <br>
> config.chatGPTTransformers.append(convertToUpperCases)<br>

For example, ChatGPT is weak to produce responses in traditional Chinese.  The following plugin convert all simplified Chinese into traditional Chinese characters:

> import config<br>
> from opencc import OpenCC<br>
> <br>
> def convertToTraditionalChinese(text):<br>
>     cc = OpenCC('s2t')<br>
>     return cc.convert(text)<br>
> <br>
> config.chatGPTTransformers.append(convertToTraditionalChinese)<br>

How to use plugins to customize input suggestion?

You can customize input suggestions by modifying 'config.inputSuggestions' with use of plugins.

For example:

1. Save a python file, e.g. inputSuggestions.py, in folder "plugins".
2. Add content, for example:

> import config

> config.inputSuggestions = config.inputSuggestions + ["Write a summary", "Write an outline", "Write a letter"]

How to use plugins to customize predefined contexts?

You can customize predefined contexts by modifying 'config.predefinedContexts' with use of plugins.

For example:

1. Save a python file, e.g. predefinedContexts.py, in folder "plugins".
2. Add content, for example:

> import config

> config.predefinedContexts["Introduction"] = """Write a introduction pertaining to the following content."""

> config.predefinedContexts["Summary"] = """Write a summary pertaining to the following content."""