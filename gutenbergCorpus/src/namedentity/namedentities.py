import spacy
import spacy_transformers

class NamedEntity():
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_trf")
        self.filter_words = ["he", "she", "was:--he", "himself", "herself", "himself;--"] 

    def process(self, doc):
        return self.nlp(doc)

    def extractPersons(self, doc):
        temp_list = list()
        for ent in doc.ents:
            if ent.label_ == "PERSON" and ent.text not in self.filter_words:
                temp_list.append(ent.text)

        return temp_list

    def processAndExtract(self, doc):
        doc = self.process(doc)
        return self.extractPersons(doc)
