import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('wordnet')
text = '''Lemmatization is the process of grouping together the different inflected forms of a word so they can be analyzed as a single item. Lemmatization is similar to stemming but it brings context to the words. So it links words with similar meanings to one word.Better.'''

lem = WordNetLemmatizer()

resText  = ""
sentences = sent_tokenize(text)
for sentence in sentences:
    words = word_tokenize(sentence)
    for word in words:
        resText += lem.lemmatize(word)+" "
print("actual text : ", text)
print()
print("Lemmatized : ", resText)