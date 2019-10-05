from modules.search.wikipedia import Wiki


class RawGenerator:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.res = {}

    def results(self):
        print(self.sentence)
        for i in [self.sentence]:
            wiki = Wiki(i)
            search = wiki.search()
            if search:
                self.res.update({i: wiki.result})
