import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def remove_stopWords(text):
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    resText = ""
    stopWords = []
    for sentence in sentences: 
        words = word_tokenize(sentence)
        for word in words:
            if word.lower() not in stop_words:
                resText+= word+" "
            else:
                stopWords.append(word)
    return (resText, stopWords)

text = ''' This is a sample text which we use to perform stop word removal. Here we use package in nltk called stopWords to identify the stop words in the text.'''
print("Acutal text : ", text)
resText, stopWords = remove_stopWords(text)
print("Text after removing stop words : ", resText)
print('Stop words found  : ', stopWords)