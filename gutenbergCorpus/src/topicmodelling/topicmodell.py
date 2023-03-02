from bertopic import BERTopic
from nltk.corpus import gutenberg
from sklearn.feature_extraction.text import CountVectorizer
import spacy

class TopicModel():
    def __init__(self):
        nlp = spacy.load('en_core_web_trf')
        vectorizer_model = CountVectorizer(stop_words="english")
        self.model = BERTopic(embedding_model=nlp, vectorizer_model=vectorizer_model)
    
    def compute_topics(self, data):
        topics, probs = self.model.fit_transform(data)
        return topics, probs

    def get_document_info(self, data):
        return self.model.get_document_info(data)

    def get_topic_info(self):
        return self.model.get_topic_info()



if __name__ == "__main__":
    pass
