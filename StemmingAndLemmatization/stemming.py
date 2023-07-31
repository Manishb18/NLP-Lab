import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
text = '''Lemmatization is the process of grouping together the different inflected forms of a word so they can be analyzed as a single item. Lemmatization is similar to stemming but it brings context to the words. So it links words with similar meanings to one word. 
Text preprocessing includes both Stemming as well as Lemmatization. Many times people find these two terms confusing. Some treat these two as the same. Actually, lemmatization is preferred over Stemming because lemmatization does morphological analysis of the words.'''

ps = PorterStemmer()
resText  = ""
sentences = sent_tokenize(text)
for sentence in sentences:
    resText += ps.stem(sentence)+" "
print("actual text : ", text)
print()
print("Stemmed text : ", resText)
