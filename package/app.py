
import ctypes
import os
import platform
import pprint
import sys
from shutil import copyfile

import qdarktheme
from gtts import gTTS

import config
from configDefault import *
from package.mainwindow import MainWindow
from package.util.Worker import ChatGPTResponse, OpenAIImage

thisFile = os.path.realpath(__file__)
wd = os.path.dirname(thisFile)
if os.getcwd() != wd:
    os.chdir(wd)
if not os.path.isfile("config.py"):
    open("config.py", "a", encoding="utf-8").close()

try:
    from pocketsphinx import LiveSpeech, get_model_path
    isPocketsphinxInstalled = True
except ModuleNotFoundError:
    isPocketsphinxInstalled = False

if config.qtLibrary == "pyside6":
    from PySide6.QtCore import QRegularExpression, Qt, QThread, Signal
    from PySide6.QtGui import (QAction, QFontMetrics, QGuiApplication, QIcon,
                               QStandardItem, QStandardItemModel,
                               QTextDocument)
    from PySide6.QtPrintSupport import QPrintDialog, QPrinter
    from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox,
                                   QCompleter, QDialog, QDialogButtonBox,
                                   QFileDialog, QFormLayout, QHBoxLayout,
                                   QLabel, QLineEdit, QListView, QMainWindow,
                                   QMenu, QMessageBox, QPlainTextEdit,
                                   QProgressBar, QPushButton, QSplitter,
                                   QSystemTrayIcon, QVBoxLayout, QWidget)
else:
    from qtpy.QtCore import QRegularExpression, Qt, QThread
    from qtpy.QtGui import (QFontMetrics, QGuiApplication, QIcon,
                            QStandardItem, QStandardItemModel, QTextDocument)
    from qtpy.QtPrintSupport import QPrintDialog, QPrinter
    from qtpy.QtWidgets import (QApplication, QCheckBox, QComboBox, QCompleter,
                                QDialog, QDialogButtonBox, QFileDialog,
                                QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                                QListView, QMainWindow, QMenu, QMessageBox,
                                QPlainTextEdit, QProgressBar, QPushButton,
                                QSplitter, QSystemTrayIcon, QVBoxLayout,
                                QWidget)


def showMainWindow():
    if not hasattr(config, "mainWindow") or config.mainWindow is None:
        config.mainWindow = MainWindow()
        qdarktheme.setup_theme() if config.darkTheme else qdarktheme.setup_theme("light")
    else:
        config.mainWindow.bringToForeground(config.mainWindow)


def aboutToQuit():
    with open("config.py", "w", encoding="utf-8") as fileObj:
        for name in dir(config):
            excludeFromSavingList = (
                "mainWindow",  # main window object
                "chatGPTApi",  # GUI object
                "chatGPTTransformers",  # used with plugins; transform ChatGPT response message
                "predefinedContexts",  # used with plugins; pre-defined contexts
                "inputSuggestiOns",  # used with plugins; user input suggestions
                "integrate_google_searches_signature",
                "chatGPTApiFunctionSignatures",  # used with plugins; function calling
                "chatGPTApiAvailableFunctions",  # used with plugins; function calling
                # used with plugins; function calling when function name is 'python'
                "pythonFunctionResponse",
            )
            if not name.startswith("__") and not name in excludeFromSavingList:
                try:
                    value = eval(f"config.{name}")
                    fileObj.write("{0} = {1}\n".format(
                        name, pprint.pformat(value)))
                except:
                    pass


def run():
    thisOS = platform.system()
    appName = "ChatGPT-GUI"
    # Windows icon
    if thisOS == "Windows":
        myappid = "chatgpt.gui"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            myappid)
        windowsIconPath = os.path.abspath(
            os.path.join(sys.path[0], "icons", f"{appName}.ico"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            windowsIconPath)
    # app
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    iconPath = os.path.abspath(os.path.join(
        sys.path[0], "icons", f"{appName}.png"))
    appIcon = QIcon(iconPath)
    app.setWindowIcon(appIcon)
    showMainWindow()
    # connection
    app.aboutToQuit.connect(aboutToQuit)

    # Desktop shortcut
    # on Windows
    if thisOS == "Windows":
        desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
        shortcutDir = desktopPath if os.path.isdir(desktopPath) else wd
        shortcutBat1 = os.path.join(shortcutDir, f"{appName}.bat")
        shortcutCommand1 = f'''powershell.exe -NoExit -Command "python '{thisFile}'"'''
        # Create .bat for application shortcuts
        if not os.path.exists(shortcutBat1):
            try:
                with open(shortcutBat1, "w") as fileObj:
                    fileObj.write(shortcutCommand1)
            except:
                pass
    # on macOS
    elif thisOS == "Darwin":
        shortcut_file = os.path.expanduser(f"~/Desktop/{appName}.command")
        if not os.path.isfile(shortcut_file):
            with open(shortcut_file, "w") as f:
                f.write("#!/bin/bash\n")
                f.write(f"cd {wd}\n")
                f.write(f"{sys.executable} {thisFile} gui\n")
            os.chmod(shortcut_file, 0o755)
    # additional shortcuts on Linux
    elif thisOS == "Linux":
        def desktopFileContent():
            iconPath = os.path.join(wd, "icons", "ChatGPT-GUI.png")
            return """#!/usr/bin/env xdg-open

    [Desktop Entry]
    Version=1.0
    Type=Application
    Terminal=false
    Path={0}
    Exec={1} {2}
    Icon={3}
    Name=ChatGPT GUI
    """.format(wd, sys.executable, thisFile, iconPath)

        ubaLinuxDesktopFile = os.path.join(wd, f"{appName}.desktop")
        if not os.path.exists(ubaLinuxDesktopFile):
            # Create .desktop shortcut
            with open(ubaLinuxDesktopFile, "w") as fileObj:
                fileObj.write(desktopFileContent())
            try:
                # Try to copy the newly created .desktop file to:
                from pathlib import Path

                # ~/.local/share/applications
                userAppDir = os.path.join(
                    str(Path.home()), ".local", "share", "applications")
                userAppDirShortcut = os.path.join(
                    userAppDir, f"{appName}.desktop")
                if not os.path.exists(userAppDirShortcut):
                    Path(userAppDir).mkdir(parents=True, exist_ok=True)
                    copyfile(ubaLinuxDesktopFile, userAppDirShortcut)
                # ~/Desktop
                homeDir = os.environ["HOME"]
                desktopPath = f"{homeDir}/Desktop"
                desktopPathShortcut = os.path.join(
                    desktopPath, f"{appName}.desktop")
                if os.path.isfile(desktopPath) and not os.path.isfile(desktopPathShortcut):
                    copyfile(ubaLinuxDesktopFile, desktopPathShortcut)
            except:
                pass

    # system tray
    if config.enableSystemTray:
        app.setQuitOnLastWindowClosed(False)
        # Set up tray icon
        tray = QSystemTrayIcon()
        tray.setIcon(appIcon)
        tray.setToolTip("ChatGPT-GUI")
        tray.setVisible(True)
        # Import system tray menu
        trayMenu = QMenu()
        showMainWindowAction = QAction(config.thisTranslation["show"])
        showMainWindowAction.triggered.connect(showMainWindow)
        trayMenu.addAction(showMainWindowAction)
        # Add a separator
        trayMenu.addSeparator()
        # Quit
        quitAppAction = QAction(config.thisTranslation["exit"])
        quitAppAction.triggered.connect(app.quit)
        trayMenu.addAction(quitAppAction)
        tray.setContextMenu(trayMenu)

        sys.exit(app.exec() if config.qtLibrary == "pyside6" else app.exec_())
