import nltk
from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()
word = "rocking"

print(lem.lemmatize(word))