import pandas as pd

class HistoryManager:
    def __init__(self, file='history.csv'):
        self.file = file

    def save(self, history):
        df = pd.DataFrame(history)
        df.to_csv(self.file, mode='a', header=False, index=False)

    def load(self):
        return pd.read_csv(self.file)
