import pprint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from package.chatgptapi import ChatGPTAPI
    from package.mainwindow import MainWindow
# import config

# def setConfig():
#     thisTranslation = {
#         'areyousure': 'Are you sure?',
#         'audio': 'Audio',
#         'chat': 'Chat',
#         'chatContext': 'Chat Context',
#         'choices': 'Choices',
#         'clearAll': 'Clear All',
#         'configure': 'Chat Settings',
#         'editable': 'Editable',
#         'exit': 'Exit',
#         'exitTheApplication': 'Exit the Application',
#         'font': 'Font',
#         'fontSize': 'Font Size',
#         'help': 'Help',
#         'image': 'Image',
#         'language': 'Language',
#         'messageHere': 'Enter your message here ...',
#         'new': 'New',
#         'optional': 'optional',
#         'print': 'Print',
#         'remove': 'Remove',
#         'required': 'required',
#         'save': 'Save',
#         'searchContent': 'Search Content',
#         'searchContentHere': 'Search content here ...',
#         'searchTitle': 'Search Title',
#         'searchTitleHere': 'Search title here ...',
#         'send': 'Send',
#         'stop': 'Stop',
#         'settings': 'Settings',
#         'show': 'Show',
#         'temperature': 'Temperature',
#         'toggleDarkTheme': 'Toggle Dark Theme',
#         'toggleSystemTray': 'Toggle System Tray',
#         'voice': 'voice',
#         'voiceTyping': 'voice typing',
#         'newDatabase': 'New Database',
#         'openDatabase': 'Open Database',
#         'saveDatabaseAs': 'Save Database as ...',
#         'newChat': 'New Chat',
#         'saveChat': 'Save Chat',
#         'exportChat': 'Export Chat',
#         'printChat': 'Print Chat',
#         'replace': 'Replace',
#         'replaceWith': 'Replace with',
#         'searchFor': 'Search for',
#         'replaceSelectedText': 'Replace selected text',
#         'matchingRegularExpression': 'matching regular expression',
#         'all': 'ALL',
#         'replaceAll': 'Replace All',
#         'toggleRegexp': 'Toggle Regular Expression',
#         'fileManager': 'Database Directory',
#         'pluginDirectory': 'Plugins Directory',
#         'predefinedContext': 'Predefined Context',
#         'toggleMultilineInput': 'Toggle Multiline User Input',
#         'latestOnlineSearchResults': 'Latest Online Search Results',
#         'maximumOnlineSearchResults': 'Maximum Online Search Results',
#         'include': 'Include',
#         'applyContext': 'Apply Context in',
#         'firstInputOnly': 'First Input Only',
#         'allInputs': 'All Inputs',
#         'autoScroll': 'Auto Scroll',
#         'enable': 'Enable',
#         'countPromptTokens': 'Count Prompt Tokens',
#         'textSelection': 'Text Selection',
#         'webBrowser': 'Web Browser',
#         'runAsSystemCommand': 'Run as System Command',
#         'runAsPythonCommand': 'Execute as Python Script',
#         'plugins': 'Plugins',
#         'chatAfterFunctionCalled': 'Chat with Function Response',
#         'runPythonScriptGlobally': 'Run Python Script Globally',
#         'readTextFile': 'Read Text File',
#         'customise': 'Customise',
#         'repository': 'Repository',
#         'about': 'About',
#         'donate': 'Donate',
#     }
#     defaultSettings = (
#         ('chatGPTApiAudio', 0),
#         ('chatGPTApiAudioLanguage', 'en'),
#         ('chatGPTApiModel', 'gpt-3.5-turbo'),
#         ('chatGPTApiPredefinedContext', '[none]'),
#         ('chatGPTApiContext', ''),
#         ('chatGPTApiLastChatDatabase', ''),
#         ('chatGPTApiMaxTokens', 512),
#         ('chatGPTApiNoOfChoices', 1),
#         ('chatGPTApiTemperature', 0.8),
#         ('chatGPTApiFunctionCall', "none"),
#         ('chatAfterFunctionCalled', True),
#         ('runPythonScriptGlobally', False),
#         ('darkTheme', True),
#         ('developer', False),
#         ('enableSystemTray', False),
#         ('fontSize', 14),
#         ('openaiApiKey', ''),
#         ('openaiApiOrganization', ''),
#         ('pocketsphinxModelPath', ''),
#         ('pocketsphinxModelPathBin', ''),
#         ('pocketsphinxModelPathDict', ''),
#         ('qtLibrary', 'pyside6'),
#         ('regexpSearchEnabled', True),
#         #('includeDuckDuckGoSearchResults', False),
#         #('maximumDuckDuckGoSearchResults', 5),
#         ('loadingInternetSearches', "none"),
#         ('maximumInternetSearchResults', 5),
#         ('chatGPTApiContextInAllInputs', False),
#         ('chatGPTApiAutoScrolling', True),
#         ('thisTranslation', thisTranslation),
#         ('chatGPTPluginExcludeList', ['testing_function_calling', 'zzz_automation_example']),
#     )
#     for key, value in defaultSettings:
#         if not hasattr(config, key):
#             value = pprint.pformat(value)
#             exec(f"""config.{key} = {value} """)
#     for i in thisTranslation:
#         if not i in config.thisTranslation:
#             config.thisTranslation[i] = thisTranslation[i]

thisTranslation = {
    'areyousure': 'Are you sure?',
    'audio': 'Audio',
    'chat': 'Chat',
    'chatContext': 'Chat Context',
    'choices': 'Choices',
    'clearAll': 'Clear All',
    'configure': 'Chat Settings',
    'editable': 'Editable',
    'exit': 'Exit',
    'exitTheApplication': 'Exit the Application',
    'font': 'Font',
    'fontSize': 'Font Size',
    'help': 'Help',
    'image': 'Image',
    'language': 'Language',
    'messageHere': 'Enter your message here ...',
    'new': 'New',
    'optional': 'optional',
    'print': 'Print',
    'remove': 'Remove',
    'required': 'required',
    'save': 'Save',
    'searchContent': 'Search Content',
    'searchContentHere': 'Search content here ...',
    'searchTitle': 'Search Title',
    'searchTitleHere': 'Search title here ...',
    'send': 'Send',
    'stop': 'Stop',
    'settings': 'Settings',
    'show': 'Show',
    'temperature': 'Temperature',
    'toggleDarkTheme': 'Toggle Dark Theme',
    'toggleSystemTray': 'Toggle System Tray',
    'voice': 'voice',
    'voiceTyping': 'voice typing',
    'newDatabase': 'New Database',
    'openDatabase': 'Open Database',
    'saveDatabaseAs': 'Save Database as ...',
    'newChat': 'New Chat',
    'saveChat': 'Save Chat',
    'exportChat': 'Export Chat',
    'printChat': 'Print Chat',
    'replace': 'Replace',
    'replaceWith': 'Replace with',
    'searchFor': 'Search for',
    'replaceSelectedText': 'Replace selected text',
    'matchingRegularExpression': 'matching regular expression',
    'all': 'ALL',
    'replaceAll': 'Replace All',
    'toggleRegexp': 'Toggle Regular Expression',
    'fileManager': 'Database Directory',
    'pluginDirectory': 'Plugins Directory',
    'predefinedContext': 'Predefined Context',
    'toggleMultilineInput': 'Toggle Multiline User Input',
    'latestOnlineSearchResults': 'Latest Online Search Results',
    'maximumOnlineSearchResults': 'Maximum Online Search Results',
    'include': 'Include',
    'applyContext': 'Apply Context in',
    'firstInputOnly': 'First Input Only',
    'allInputs': 'All Inputs',
    'autoScroll': 'Auto Scroll',
    'enable': 'Enable',
    'countPromptTokens': 'Count Prompt Tokens',
    'textSelection': 'Text Selection',
    'webBrowser': 'Web Browser',
    'runAsSystemCommand': 'Run as System Command',
    'runAsPythonCommand': 'Execute as Python Script',
    'plugins': 'Plugins',
    'chatAfterFunctionCalled': 'Chat with Function Response',
    'runPythonScriptGlobally': 'Run Python Script Globally',
    'readTextFile': 'Read Text File',
    'customise': 'Customise',
    'repository': 'Repository',
    'about': 'About',
    'donate': 'Donate',
}


class Config:
    def __init__(self):
        self.chatGPTApiAudioLanguage = 'en'
        self.chatGPTApiModel = 'gpt-3.5-turbo'
        self.chatGPTApiPredefinedContext = '[none]'
        self.chatGPTApiContext = ''
        self.chatGPTApiLastChatDatabase = ''
        self.chatGPTApiMaxTokens = 512
        self.chatGPTApiNoOfChoices = 1
        self.chatGPTApiTemperature = 0.8
        self.chatGPTApiFunctionCall = "none"
        self.chatAfterFunctionCalled = True
        self.runPythonScriptGlobally = False
        self.darkTheme = True
        self.developer = False
        self.enableSystemTray = False
        self.fontSize = 14
        self.openaiApiKey = ''
        self.openaiApiOrganization = ''
        self.pocketsphinxModelPath = ''
        self.pocketsphinxModelPathBin = ''
        self.pocketsphinxModelPathDict = ''
        self.qtLibrary = 'pyside6'
        self.regexpSearchEnabled = True
        self.includeDuckDuckGoSearchResults = False
        self.maximumDuckDuckGoSearchResults = 5
        self.loadingInternetSearches = "none"
        self.maximumInternetSearchResults = 5
        self.chatGPTApiContextInAllInputs = False
        self.chatGPTApiAutoScrolling = True
        self.thisTranslation = thisTranslation
        self.chatGPTPluginExcludeList = [
            'testing_function_calling', 'zzz_automation_example']

        self.predefinedContexts = {
            "[none]": "",
            "[custom]": "",
        }
        self.inputSuggestions = []
        self.chatGPTTransformers = []
        self.chatGPTApiFunctionSignatures = []
        self.chatGPTApiAvailableFunctions = {}

        self.mainWindow: MainWindow | None = None

        self.chatGPTApi: ChatGPTAPI | None = None

    def load_config(self, config):
        for key, value in config.items():
            setattr(self, key, value)
