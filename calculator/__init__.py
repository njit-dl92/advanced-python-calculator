from .addition import add
from .subtraction import subtract

def load_plugins():
    return {
        'add': add,
        'subtract': subtract
    }
