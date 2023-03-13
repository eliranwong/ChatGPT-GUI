# ChatGPT-GUI

Use Qt to develop a standalone graphical user interface for use of ChatGPT API

![screenshot1](https://user-images.githubusercontent.com/25262722/224390511-540f1ca0-2f76-4f83-9332-02aba5cb5b3c.png)

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

* enter message with voice

* use OpenAI image model to generate images

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

![screenshot2](https://user-images.githubusercontent.com/25262722/224164608-fcee440a-8be3-4850-8869-415acc1ce869.png)

1) Launch ChatGPT-GUI by running "python3 ChatGPT-GUI"
2) Click "Settings" to enter your own OpenAI API key
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

* chat or image - this determines whether the message to sent to generate a chat response or an image.

* content view - display conversation content

* Control interface:

- Settings - open "Settings" dialog, where you can enter OpenAI API key, orgnisation ID, conversation context, text-to-speech language.

- Temperature - according to OpenAI documentation, temperature means "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."

- Choices - according to OpenAI documentation, choices means "How many chat completion choices to generate for each input message."

- Font - edit the font size of chat record list and content view

- Editable checkbox - toggles to edit the content view or make it read-only

- "New" - open a new conversation

- "Save" saves edited conversation.  Each conservation is automatically saved when a new response is loaded.  Users may edit and updated the content with this button.

Application menu:

* New - new chat

* Save - save chat

* Configure - open settings dialog

* Toggle Dark Theme - toggle between dark and light theme

* Exit - Exit the application

# FAQ - Frequently Asked Questions

How to edit a record's title?

> Edit the first line of a record to change its title.

Where is the offline database, that "ChatGPT-GUI" works with, stored?

> "ChatGPT.db" in the same folder containing the "ChatGPT-GUI.py" file.  This is a sqlite database file, generated on first run of the application.

Can I change the context to make the conversation context to focus on a particular area?

> Yes.  Click the "Settings" button to edit the chat context.  The default is empty.  Change it to the topic you want to focus in your conversations.

Can I change the language of the interface?

> Yes, simply edit the 'thisTranslation' entry in file 'config.py'.

How to use python plugins to process ChatGPT responses before they are displayed?

1) Create a python file and save it in folder "plugins".

2) In the python file, append the method that transform the response to config.chatGPTTransformers

For example, ChatGPT is weak to produce responses in traditional Chinese.  The following plugin convert all simplified Chinese into traditional Chinese characters:

> import config<br>
> """brew/apt install opencc<br>
> pip3 install opencc-python-reimplemented"""<br>
> from opencc import OpenCC<br>
> <br>
> def convertToTraditionalChinese(text):<br>
>     cc = OpenCC('s2t')<br>
>     return cc.convert(text)<br>
> <br>
> config.chatGPTTransformers.append(convertToTraditionalChinese)<br>
