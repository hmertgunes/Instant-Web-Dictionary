import pandas as pd


class Definiton:

    def __init__(self,term):
        self.term = term

    def get(self):
        data = pd.read_csv("files/data.csv")
        return tuple(data.loc[data["word"] == self.term]["definition"])
