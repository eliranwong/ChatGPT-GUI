# ChatGPT-GUI

Use Qt to develop a graphical user interface for use of ChatGPT API

# Background

We have used Qt to develop [a gui for using ChatGPT for bible study with UniqueBible.app](https://github.com/eliranwong/UniqueBible/wiki/Bible-Chat-with-ChatGPT-API).  Here in this project, we modify the code to make it as a standalone application for general purpose.

# ChatGPT API

This application is Qt-based graphical user interface that uses OpenAI ChatGPT API to generate chat conversations.

Users need to register an OpenAI account and generate a API key first.

Read pricing at: https://openai.com/pricing

Generate API key at: https://platform.openai.com/account/api-keys

# Difference between "ChatGPT-GUI" interface and ChatGPT web version

ChatGPT web version is available at: https://chat.openai.com/chat

"ChatGPT-GUI" uses the same model, but with enhanced features not available at ChatGPT web version.

With "ChatGPT-GUI", users can:

* start conversation with a particular context.  With "ChatGPT-GUI", users can specify a context for conversations.  For example, asking "Who is David?" in our original "Bible Chat" get a response related to the bible.

* adjust temperature [What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.]

* adjust number of choices in ChatGPT responses [How many chat completion choices to generate for each input message.]

* save conversations for offline use

* search history for title or content

* edit and save conversations

* listen to text-to-speech audio as Bible Chat generates responses

* enter message with voice

# QuickStart

![Screenshot from 2023-03-09 10-53-02](https://user-images.githubusercontent.com/25262722/224003093-81bd2652-0050-4bf4-9e57-47e2c81ac83a.png)

1) Launch "Bible Chat" from plugins menu
2) Click "Settings" to enter your own OpenAI API key
3) Enter your message in message entry field and press Enter key, to start a conversation

# Graphical User Interface

The Bible Chat Window is separated into left and right areas, by a movable splitter.  Users can move the splitter to either end to hide one of them. 

On the Left, from top to bottom:

* search entry and button for title - enter text here to search for a title, that contains the entered text, in saved record.  You may either press the button or press the "Enter" key after text entry.

* search entry and button for content - enter text here to search for a content, that contains the entered text, in saved record.  You may either press the button or press the "Enter" key after text entry.

* record list - list of saved records or search results.  Select a record to update the content view on the right.

* "Remove" & "Clear All" buttons - remove selected record or remove all records.  Confirmation is required before you proceed the deletion.

* "Help" button - open this wiki page

On the right, from top to bottom:

* message input - users enter a message here to begin or continue a conversation.  The voice checkbox toggle voice-typing.  The send button sends the message.  Alternately, users can press the "Enter" key after text entry.  When a message is sent, a progress bar is displayed to indicate that the message is being processed.

* content view - display conversation content

* Control interface:

- Settings - open "Settings" dialog, where you can enter OpenAI API key, orgnisation ID, conversation context, text-to-speech language.  In our original "Bible Chat" application, context is set to "about the bible" by default.  You may modify the context to get the conversations focused on a particular topic or context.

- Temperature - according to OpenAI documentation, temperature means "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."

- Choices - according to OpenAI documentation, choices means "How many chat completion choices to generate for each input message."

- Audio checkbox - toggles audio plackback when a new response is loaded.  Users can select default language in "Settings"

- Editable checkbox - toggles to edit the content view or make it read-only

- "New" - open a new conversation

- "Save" saves edited conversation.  Each conservation is automatically saved when a new response is loaded.  Users may edit and updated the content with this button.

# FAQ - Frequently Asked Questions

How to edit a record's title?

> Edit the first line of a record to change its title.

Where is the offline database, that "Bible Chat" works with, stored?

> "ChatGPT.db" in the same folder containing the "ChatGPT-GUI.py" file.  The database file is generated on first run of the application.

Can I change the context to make the conversation context to focus on a particular area in bible study?

> Yes.  Click the "Settings" button to edit the chat context.  The default is empty.  Change it to the topic you want to focus in your conversations.  In our original "Bible Chat", we enter "about the bible" as the context.
