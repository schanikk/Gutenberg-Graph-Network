# Internal
import os

#External
import pandas as pd

#Relative
from src.topicmodelling.topicmodell import ( TopicModel )
from src.namedentity.namedentities import ( NamedEntity )
from src.util.data_loader import  ( loadMeta, DataLoader, preprocess )
from definitions import TEXT_DIR


def getBookNames(filenames:list) -> list:
    file_names = list()
    for file in filenames:
        file_names.append(file.split('_')[0])
    
    print(file_names)
    return file_names

def filterAndCombine(df, filenames):
    
    #GetIndexOfDataFrame Entry for each book
    booksDfIndex = getBookNames(filenames)
    print(booksDfIndex) 
    
    df = df.set_index('id')
    filteredDF = df.filter(items=booksDfIndex, axis=0)

    # Create New Series with FullText for new Column
    text_series = dict()
    for i,_ in filteredDF.iterrows():
        print(i)
        text_series[i] = DataLoader(i)
    
    #Insert Text
    filteredDF['text'] = text_series

    filteredDF['paras'] = filteredDF.text.apply(preprocess)

    filteredDF = filteredDF.reset_index()

    filteredDF = filteredDF.rename({'index': 'BookFileName'})

    return filteredDF



def main():
    # Initialize Models
 #   tm_model = TopicModel()
 #   ner_model = NamedEntity()

    # Get all Meta Data
    df_meta = loadMeta()

    # Get all Files in text Directory
    listOfBooks = os.listdir(TEXT_DIR)

    #Filter Metadata  to only containing Needed Data
    # For each file load the text  into  the  dataframe
    df_filtered = filterAndCombine(df_meta, listOfBooks)
    
    #DEBBUG
    print(df_filtered[:10])

    
    #Only 100 books
    df_filtered = df_filtered[:1000]


    df_filtered.to_json("./data/checkpoint/temporarydocs.json", orient='records')

    # Train TopicModell



    # retrieve document_info

    # for each document -> NER


    # save to json




if __name__ == "__main__":
    main()
