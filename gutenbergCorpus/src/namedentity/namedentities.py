import spacy
import nltk
from nltk.corpus import gutenberg

def setup():
    nlp = spacy.load("en_core_web_trf")
    return nlp

def create_entities(docs):
    pronoun = ["he", "she", "was:--he", "himself", "herself", "himself;--"]
    dict_ = dict()
    for key,value in docs.items():
        print(f"Para {key} ")
        for span in value.ents:
            temp_list = list()
            if span.label_ == "PERSON" and span.text not in pronoun:
                temp_list.append((span.text, span.label_, span.start, span.end))
                print(span.text, span.start, span.end, span.label_)
        dict_[key] = temp_list
    return dict_

def load_and_process(nlp):
    fileids_ = gutenberg.fileids()
    final_result = dict()
    for fileid in fileids_:
        doc = gutenberg.paras(fileid)
        doc = [' '.join(e) for para in doc for e in para]
        results_ = dict()
        for i, d in enumerate(doc):
            res = nlp(d)
            results_[i] = res
        final_result[fileid]=create_entities(results_)

    return final_result
