from PySide6.QtCore import QRegularExpression, Qt, QThread, Signal
from PySide6.QtGui import (QAction, QFontMetrics, QGuiApplication, QIcon,
                           QStandardItem, QStandardItemModel, QTextDocument)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCompleter,
                               QDialog, QDialogButtonBox, QFileDialog,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QListView, QMainWindow, QMenu, QMessageBox,
                               QPlainTextEdit, QProgressBar, QPushButton,
                               QSplitter, QSystemTrayIcon, QVBoxLayout,
                               QWidget)

from package import config


class ApiDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(config.thisTranslation["settings"])

        self.apiKeyEdit = QLineEdit(config.openaiApiKey)
        self.apiKeyEdit.setEchoMode(QLineEdit.Password)
        self.orgEdit = QLineEdit(config.openaiApiOrganization)
        self.orgEdit.setEchoMode(QLineEdit.Password)
        self.apiModelBox = QComboBox()
        initialIndex = 0
        index = 0
        for key in ("gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"):
            self.apiModelBox.addItem(key)
            if key == config.chatGPTApiModel:
                initialIndex = index
            index += 1
        self.apiModelBox.setCurrentIndex(initialIndex)
        self.functionCallingBox = QComboBox()
        initialIndex = 0
        index = 0
        for key in ("auto", "none"):
            self.functionCallingBox.addItem(key)
            if key == config.chatGPTApiFunctionCall:
                initialIndex = index
            index += 1
        self.functionCallingBox.setCurrentIndex(initialIndex)
        self.loadingInternetSearchesBox = QComboBox()
        initialIndex = 0
        index = 0
        for key in ("always", "auto", "none"):
            self.loadingInternetSearchesBox.addItem(key)
            if key == config.loadingInternetSearches:
                initialIndex = index
            index += 1
        self.loadingInternetSearchesBox.setCurrentIndex(initialIndex)
        self.maxTokenEdit = QLineEdit(str(config.chatGPTApiMaxTokens))
        self.maxTokenEdit.setToolTip(
            "The maximum number of tokens to generate in the completion.\nThe token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).")
        self.maxInternetSearchResults = QLineEdit(
            str(config.maximumInternetSearchResults))
        self.maxInternetSearchResults.setToolTip(
            "The maximum number of internet search response to be included.")
        # self.includeInternetSearches = QCheckBox(config.thisTranslation["include"])
        # self.includeInternetSearches.setToolTip("Include latest internet search results")
        # self.includeInternetSearches.setCheckState(Qt.Checked if config.includeDuckDuckGoSearchResults else Qt.Unchecked)
        # self.includeDuckDuckGoSearchResults = config.includeDuckDuckGoSearchResults
        self.autoScrollingCheckBox = QCheckBox(
            config.thisTranslation["enable"])
        self.autoScrollingCheckBox.setToolTip(
            "Auto-scroll display as responses are received")
        self.autoScrollingCheckBox.setCheckState(
            Qt.Checked if config.chatGPTApiAutoScrolling else Qt.Unchecked)
        self.chatGPTApiAutoScrolling = config.chatGPTApiAutoScrolling
        self.chatAfterFunctionCalledCheckBox = QCheckBox(
            config.thisTranslation["enable"])
        self.chatAfterFunctionCalledCheckBox.setToolTip(
            "Automatically generate next chat response after a function is called")
        self.chatAfterFunctionCalledCheckBox.setCheckState(
            Qt.Checked if config.chatAfterFunctionCalled else Qt.Unchecked)
        self.chatAfterFunctionCalled = config.chatAfterFunctionCalled
        self.runPythonScriptGloballyCheckBox = QCheckBox(
            config.thisTranslation["enable"])
        self.runPythonScriptGloballyCheckBox.setToolTip(
            "Run user python script in global scope")
        self.runPythonScriptGloballyCheckBox.setCheckState(
            Qt.Checked if config.runPythonScriptGlobally else Qt.Unchecked)
        self.runPythonScriptGlobally = config.runPythonScriptGlobally
        self.contextEdit = QLineEdit(config.chatGPTApiContext)
        firstInputOnly = config.thisTranslation["firstInputOnly"]
        allInputs = config.thisTranslation["allInputs"]
        self.applyContextIn = QComboBox()
        self.applyContextIn.addItems([firstInputOnly, allInputs])
        self.applyContextIn.setCurrentIndex(
            1 if config.chatGPTApiContextInAllInputs else 0)
        self.predefinedContextBox = QComboBox()
        initialIndex = 0
        index = 0
        for key, value in config.predefinedContexts.items():
            self.predefinedContextBox.addItem(key)
            self.predefinedContextBox.setItemData(
                self.predefinedContextBox.count()-1, value, role=Qt.ToolTipRole)
            if key == config.chatGPTApiPredefinedContext:
                initialIndex = index
            index += 1
        self.predefinedContextBox.currentIndexChanged.connect(
            self.predefinedContextBoxChanged)
        self.predefinedContextBox.setCurrentIndex(initialIndex)
        # set availability of self.contextEdit in case there is no index changed
        self.contextEdit.setDisabled(
            True) if not initialIndex == 1 else self.contextEdit.setEnabled(True)
        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QFormLayout()
        # https://platform.openai.com/account/api-keys
        chatAfterFunctionCalled = config.thisTranslation["chatAfterFunctionCalled"]
        runPythonScriptGlobally = config.thisTranslation["runPythonScriptGlobally"]
        autoScroll = config.thisTranslation["autoScroll"]
        predefinedContext = config.thisTranslation["predefinedContext"]
        context = config.thisTranslation["chatContext"]
        applyContext = config.thisTranslation["applyContext"]
        latestOnlineSearchResults = config.thisTranslation["latestOnlineSearchResults"]
        maximumOnlineSearchResults = config.thisTranslation["maximumOnlineSearchResults"]
        required = config.thisTranslation["required"]
        optional = config.thisTranslation["optional"]
        layout.addRow(f"OpenAI API Key [{required}]:", self.apiKeyEdit)
        layout.addRow(f"Organization ID [{optional}]:", self.orgEdit)
        layout.addRow(f"API Model [{required}]:", self.apiModelBox)
        layout.addRow(f"Max Token [{required}]:", self.maxTokenEdit)
        layout.addRow(
            f"Function Calling [{optional}]:", self.functionCallingBox)
        layout.addRow(
            f"{chatAfterFunctionCalled} [{optional}]:", self.chatAfterFunctionCalledCheckBox)
        layout.addRow(
            f"{predefinedContext} [{optional}]:", self.predefinedContextBox)
        layout.addRow(f"{context} [{optional}]:", self.contextEdit)
        layout.addRow(f"{applyContext} [{optional}]:", self.applyContextIn)
        layout.addRow(
            f"{latestOnlineSearchResults} [{optional}]:", self.loadingInternetSearchesBox)
        layout.addRow(
            f"{maximumOnlineSearchResults} [{optional}]:", self.maxInternetSearchResults)
        layout.addRow(f"{autoScroll} [{optional}]:",
                      self.autoScrollingCheckBox)
        layout.addRow(
            f"{runPythonScriptGlobally} [{optional}]:", self.runPythonScriptGloballyCheckBox)
        layout.addWidget(buttonBox)
        self.autoScrollingCheckBox.stateChanged.connect(
            self.toggleAutoScrollingCheckBox)
        self.chatAfterFunctionCalledCheckBox.stateChanged.connect(
            self.toggleChatAfterFunctionCalled)
        self.runPythonScriptGloballyCheckBox.stateChanged.connect(
            self.toggleRunPythonScriptGlobally)
        self.functionCallingBox.currentIndexChanged.connect(
            self.functionCallingBoxChanged)
        self.loadingInternetSearchesBox.currentIndexChanged.connect(
            self.loadingInternetSearchesBoxChanged)

        self.setLayout(layout)

    def api_key(self):
        return self.apiKeyEdit.text().strip()

    def org(self):
        return self.orgEdit.text().strip()

    def context(self):
        return self.contextEdit.text().strip()

    def contextInAllInputs(self):
        return True if self.applyContextIn.currentIndex() == 1 else False

    def predefinedContextBoxChanged(self, index):
        self.contextEdit.setDisabled(
            True) if not index == 1 else self.contextEdit.setEnabled(True)

    def predefinedContext(self):
        return self.predefinedContextBox.currentText()
        # return self.predefinedContextBox.currentData(Qt.ToolTipRole)

    def apiModel(self):
        # return "gpt-3.5-turbo"
        return self.apiModelBox.currentText()

    def functionCalling(self):
        return self.functionCallingBox.currentText()

    def enable_auto_scrolling(self):
        return self.chatGPTApiAutoScrolling

    def toggleAutoScrollingCheckBox(self, state):
        self.chatGPTApiAutoScrolling = True if state else False

    def enable_chatAfterFunctionCalled(self):
        return self.chatAfterFunctionCalled

    def toggleChatAfterFunctionCalled(self, state):
        self.chatAfterFunctionCalled = True if state else False

    def enable_runPythonScriptGlobally(self):
        return self.runPythonScriptGlobally

    def toggleRunPythonScriptGlobally(self, state):
        self.runPythonScriptGlobally = True if state else False

    def functionCallingBoxChanged(self):
        if self.functionCallingBox.currentText() == "none" and self.loadingInternetSearchesBox.currentText() == "auto":
            self.loadingInternetSearchesBox.setCurrentText("none")

    def loadingInternetSearches(self):
        return self.loadingInternetSearchesBox.currentText()

    def loadingInternetSearchesBoxChanged(self, _):
        if self.loadingInternetSearchesBox.currentText() == "auto":
            self.functionCallingBox.setCurrentText("auto")

    def max_token(self):
        return self.maxTokenEdit.text().strip()

    def max_internet_search_results(self):
        return self.maxInternetSearchResults.text().strip()
