from .plugins.addition import add
from .plugins.subtraction import subtract


def load_plugins():
    return {
        'add': add,
        'subtract': subtract
    }
