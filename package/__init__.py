# parse config, initialize constants etc.

# set working directory

try:
    from pocketsphinx import LiveSpeech, get_model_path
    isPocketsphinxInstalled = True
except ModuleNotFoundError:
    isPocketsphinxInstalled = False