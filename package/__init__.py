# parse config, initialize constants etc.

# temporary workaround: changes to config is lost across modules if it's imported as a module
import importlib
import importlib.util
import os
from pathlib import Path

from package.configDefault import Config

# might be customizable
CONFIG_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "config.py"))
PLUGINS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "plugins"))
CHATS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "chats"))
spec = importlib.util.spec_from_file_location("config", CONFIG_PATH)
if spec is None or spec.loader is None:
    raise FileNotFoundError("config file not found: {CONFIG_PATH}")
config_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config_module)

user_config = {key: getattr(config_module, key)
               for key in dir(config_module)}
config = Config()
config.load_config(user_config)

# set working directory

try:
    from pocketsphinx import LiveSpeech, get_model_path
    isPocketsphinxInstalled = True
except ModuleNotFoundError:
    isPocketsphinxInstalled = False
