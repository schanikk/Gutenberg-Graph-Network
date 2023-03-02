import  os

#import nltk
#from nltk.corpus.reader.util import *
#from nltk.corpus.reader.plaintext import PlaintextCorpusReader

import pandas as pd

from definitions import ROOT_DIR, DATA_DIR, TEXT_DIR, META_DIR


def loadMeta():
    return pd.read_csv(os.path.join(META_DIR, 'metadata.csv'))


def DataLoader(filename):
    path = os.path.join(TEXT_DIR, filename+'_text.txt')
    with open(path) as f:
        data = f.read()
    return data

def preprocess(data):
    splat = data.split("\n\n")

    return splat
