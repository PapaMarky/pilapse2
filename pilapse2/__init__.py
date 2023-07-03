import importlib.metadata
__version__ = importlib.metadata.version(__package__)
def test():
    print(f'this is a test (version: {__version__})')

def make_video():
    print(f'making video with pilapse2 version {__version__}')
