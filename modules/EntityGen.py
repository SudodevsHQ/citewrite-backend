import nltk
import spacy
from nltk import word_tokenize, pos_tag, ne_chunk
import os
from nltk.tag import StanfordNERTagger
from modules.search.wikipedia import Wiki


class Generator:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.required = []
        self.res = {}

    def run(self):
        entities = []
        spacy_nlp = spacy.load('en')
        article = self.sentence
        document = spacy_nlp(article)

        for element in document.ents:
            entities.append((element.label_, element))

        for e in entities:
            self.required.append(str(e[1]))
        self.required = " ". join(self.required)

    def results(self):
        if not self.required:
            self.required = self.sentence
        for i in [self.required]:
            wiki = Wiki(i)
            search = wiki.search()
            if search:
                self.res.update({i: wiki.result})
