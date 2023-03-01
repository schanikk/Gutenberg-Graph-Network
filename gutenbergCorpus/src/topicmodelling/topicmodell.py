from bertopic import BERTopic
from nltk.corpus import gutenberg
import spacy


def setup():
    dataset = gutenberg.words('austen-sense.txt')
    nlp = spacy.load('en_core_web_md', exclude=['tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer'])
    topic_model = BERTopic(embedding_model=nlp)
    return topic_model,dataset

def create_topic(model, data):
    topics, probs = model.fit_transform(data)
    return topics,probs



if __name__ == "__main__":
    model,dataset = setup()
    topics, probs = create_topic(model,dataset)
    fig = model.visualize_topics()
    fig.show()

