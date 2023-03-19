import config, pprint

def setConfig():
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
        'predefinedContext': 'Predefined Context',
    }
    defaultSettings = (
        ('chatGPTApiAudio', 0),
        ('chatGPTApiAudioLanguage', 'en'),
        ('chatGPTApiModel', 'gpt-3.5-turbo'),
        ('chatGPTApiPredefinedContext', '[none]'),
        ('chatGPTApiContext', ''),
        ('chatGPTApiLastChatDatabase', ''),
        ('chatGPTApiMaxTokens', 1024),
        ('chatGPTApiNoOfChoices', 1),
        ('chatGPTApiTemperature', 0.8),
        ('darkTheme', True),
        ('developer', False),
        ('enableSystemTray', False),
        ('fontSize', 14),
        ('openaiApiKey', ''),
        ('openaiApiOrganization', ''),
        ('pocketsphinxModelPath', ''),
        ('pocketsphinxModelPathBin', ''),
        ('pocketsphinxModelPathDict', ''),
        ('qtLibrary', 'pyside6'),
        ('regexpSearchEnabled', True),
        ('thisTranslation', thisTranslation)
    )
    for key, value in defaultSettings:
        if not hasattr(config, key):
            value = pprint.pformat(value)
            exec(f"""config.{key} = {value} """)
    for i in thisTranslation:
        if not i in config.thisTranslation:
            config.thisTranslation[i] = thisTranslation[i]

setConfig()