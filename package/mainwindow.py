import glob
import os
import platform
import webbrowser
from functools import partial

import qdarktheme
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

from package import PLUGINS_PATH, config
from package.chatgptapi import ChatGPTAPI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def reloadMenubar(self):
        self.menuBar().clear()
        self.createMenubar()

    def createMenubar(self):
        # Create a menu bar
        menubar = self.menuBar()

        # Create a File menu and add it to the menu bar
        file_menu = menubar.addMenu(config.thisTranslation["chat"])

        new_action = QAction(config.thisTranslation["openDatabase"], self)
        new_action.setShortcut("Ctrl+Shift+O")
        new_action.triggered.connect(self.chatGPT.openDatabase)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["newDatabase"], self)
        new_action.setShortcut("Ctrl+Shift+N")
        new_action.triggered.connect(self.chatGPT.newDatabase)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["saveDatabaseAs"], self)
        new_action.setShortcut("Ctrl+Shift+S")
        new_action.triggered.connect(
            lambda: self.chatGPT.newDatabase(copyExistingDatabase=True))
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        new_action = QAction(config.thisTranslation["fileManager"], self)
        new_action.triggered.connect(self.openDatabaseDirectory)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["pluginDirectory"], self)
        new_action.triggered.connect(self.openPluginsDirectory)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        new_action = QAction(config.thisTranslation["newChat"], self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.chatGPT.newData)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["saveChat"], self)
        new_action.setShortcut("Ctrl+S")
        new_action.triggered.connect(self.chatGPT.saveData)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["exportChat"], self)
        new_action.triggered.connect(self.chatGPT.exportData)
        file_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["printChat"], self)
        new_action.setShortcut("Ctrl+P")
        new_action.triggered.connect(self.chatGPT.printData)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        new_action = QAction(config.thisTranslation["readTextFile"], self)
        new_action.triggered.connect(self.chatGPT.openTextFileDialog)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        new_action = QAction(config.thisTranslation["countPromptTokens"], self)
        new_action.triggered.connect(self.chatGPT.num_tokens_from_messages)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        # Create a Exit action and add it to the File menu
        exit_action = QAction(config.thisTranslation["exit"], self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip(config.thisTranslation["exitTheApplication"])
        exit_action.triggered.connect(QGuiApplication.instance().quit)
        file_menu.addAction(exit_action)

        # Create customise menu
        customise_menu = menubar.addMenu(config.thisTranslation["customise"])

        openSettings = QAction(config.thisTranslation["configure"], self)
        openSettings.triggered.connect(self.chatGPT.showApiDialog)
        customise_menu.addAction(openSettings)

        customise_menu.addSeparator()

        new_action = QAction(config.thisTranslation["toggleDarkTheme"], self)
        new_action.triggered.connect(self.toggleTheme)
        customise_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["toggleSystemTray"], self)
        new_action.triggered.connect(self.toggleSystemTray)
        customise_menu.addAction(new_action)

        new_action = QAction(
            config.thisTranslation["toggleMultilineInput"], self)
        new_action.setShortcut("Ctrl+L")
        new_action.triggered.connect(self.chatGPT.multilineButtonClicked)
        customise_menu.addAction(new_action)

        new_action = QAction(config.thisTranslation["toggleRegexp"], self)
        new_action.setShortcut("Ctrl+E")
        new_action.triggered.connect(self.toggleRegexp)
        customise_menu.addAction(new_action)

        # Create predefined context menu
        context_menu = menubar.addMenu(
            config.thisTranslation["predefinedContext"])
        for index, context in enumerate(config.predefinedContexts):
            contextAction = QAction(context, self)
            if index < 10:
                contextAction.setShortcut(f"Ctrl+{index}")
            contextAction.triggered.connect(
                partial(self.chatGPT.bibleChatAction, context))
            context_menu.addAction(contextAction)

        # Create a plugin menu
        plugin_menu = menubar.addMenu(config.thisTranslation["plugins"])

        pluginFolder = PLUGINS_PATH 
        for index, plugin in enumerate(self.fileNamesWithoutExtension(pluginFolder, "py")):
            new_action = QAction(plugin, self)
            new_action.setCheckable(True)
            new_action.setChecked(
                False if plugin in config.chatGPTPluginExcludeList else True)
            new_action.triggered.connect(
                partial(self.updateExcludePluginList, plugin))
            plugin_menu.addAction(new_action)

        # Create a text selection menu
        text_selection_menu = menubar.addMenu(
            config.thisTranslation["textSelection"])

        new_action = QAction(config.thisTranslation["webBrowser"], self)
        new_action.triggered.connect(self.chatGPT.webBrowse)
        text_selection_menu.addAction(new_action)

        new_action = QAction(
            config.thisTranslation["runAsPythonCommand"], self)
        new_action.triggered.connect(self.chatGPT.runPythonCommand)
        text_selection_menu.addAction(new_action)

        new_action = QAction(
            config.thisTranslation["runAsSystemCommand"], self)
        new_action.triggered.connect(self.chatGPT.runSystemCommand)
        text_selection_menu.addAction(new_action)

        # Create About menu
        about_menu = menubar.addMenu(config.thisTranslation["about"])

        openSettings = QAction(config.thisTranslation["repository"], self)
        openSettings.triggered.connect(lambda: webbrowser.open(
            "https://github.com/eliranwong/ChatGPT-GUI"))
        about_menu.addAction(openSettings)

        about_menu.addSeparator()

        new_action = QAction(config.thisTranslation["help"], self)
        new_action.triggered.connect(lambda: webbrowser.open(
            "https://github.com/eliranwong/ChatGPT-GUI/wiki"))
        about_menu.addAction(new_action)

        about_menu.addSeparator()

        new_action = QAction(config.thisTranslation["donate"], self)
        new_action.triggered.connect(lambda: webbrowser.open(
            "https://www.paypal.com/paypalme/MarvelBible"))
        about_menu.addAction(new_action)

    def initUI(self):
        # Set a central widget
        self.chatGPT = ChatGPTAPI(self)
        self.setCentralWidget(self.chatGPT)

        # create menu bar
        self.createMenubar()

        # set initial window size
        # self.setWindowTitle("ChatGPT-GUI")
        self.resize(QGuiApplication.primaryScreen().availableSize() * 3 / 4)
        self.show()

    def updateExcludePluginList(self, plugin):
        if plugin in config.chatGPTPluginExcludeList:
            config.chatGPTPluginExcludeList.remove(plugin)
        else:
            config.chatGPTPluginExcludeList.append(plugin)
        internetSeraches = "integrate google searches"
        if internetSeraches in config.chatGPTPluginExcludeList and config.loadingInternetSearches == "auto":
            config.loadingInternetSearches = "none"
        elif not internetSeraches in config.chatGPTPluginExcludeList and config.loadingInternetSearches == "none":
            config.loadingInternetSearches = "auto"
            config.chatGPTApiFunctionCall = "auto"
        # reload plugins
        config.chatGPTApi.runPlugins()

    def fileNamesWithoutExtension(self, dir, ext):
        files = glob.glob(os.path.join(dir, "*.{0}".format(ext)))
        return sorted([file[len(dir)+1:-(len(ext)+1)] for file in files if os.path.isfile(file)])

    def getOpenCommand(self):
        thisOS = platform.system()
        if thisOS == "Windows":
            openCommand = "start"
        elif thisOS == "Darwin":
            openCommand = "open"
        elif thisOS == "Linux":
            openCommand = "xdg-open"
        # TODO: raise error if unable to detect OS
        return openCommand

    def openDatabaseDirectory(self):
        databaseDirectory = os.path.dirname(
            os.path.abspath(config.chatGPTApiLastChatDatabase))
        openCommand = self.getOpenCommand()
        os.system(f"{openCommand} {databaseDirectory}")

    def openPluginsDirectory(self):
        openCommand = self.getOpenCommand()
        os.system(f"{openCommand} plugins")

    def toggleRegexp(self):
        config.regexpSearchEnabled = not config.regexpSearchEnabled
        self.chatGPT.updateSearchToolTips()
        QMessageBox.information(
            self, "ChatGPT-GUI", f"Regular expression for search and replace is {'enabled' if config.regexpSearchEnabled else 'disabled'}!")

    def toggleSystemTray(self):
        config.enableSystemTray = not config.enableSystemTray
        QMessageBox.information(
            self, "ChatGPT-GUI", "You need to restart this application to make the changes effective.")

    def toggleTheme(self):
        config.darkTheme = not config.darkTheme
        qdarktheme.setup_theme() if config.darkTheme else qdarktheme.setup_theme("light")

    # Work with system tray
    def isWayland(self):
        if platform.system() == "Linux" and not os.getenv('QT_QPA_PLATFORM') is None and os.getenv('QT_QPA_PLATFORM') == "wayland":
            return True
        else:
            return False

    def bringToForeground(self, window):
        if window and not (window.isVisible() and window.isActiveWindow()):
            window.raise_()
            # Method activateWindow() does not work with qt.qpa.wayland
            # platform.system() == "Linux" and not os.getenv('QT_QPA_PLATFORM') is None and os.getenv('QT_QPA_PLATFORM') == "wayland"
            # The error message is received when QT_QPA_PLATFORM=wayland:
            # qt.qpa.wayland: Wayland does not support QWindow::requestActivate()
            # Therefore, we use hide and show methods instead with wayland.
            if window.isVisible() and not window.isActiveWindow():
                window.hide()
            window.show()
            if not self.isWayland():
                window.activateWindow()
