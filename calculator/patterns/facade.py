class HistoryFacade:
    def __init__(self, manager):
        self.manager = manager

    def save_history(self, history):
        self.manager.save(history)

    def load_history(self):
        return self.manager.load()
