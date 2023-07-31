import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy

# Initialize NLTK Porter Stemmer
stemmer = PorterStemmer()

# Initialize SpaCy Lemmatizer
nlp = spacy.load('en_core_web_sm')

def perform_stemming(text):
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stemmed_tokens)

def perform_lemmatization(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    return " ".join(lemmatized_tokens)

if __name__ == "__main__":
    input_text = "I am running in the races and playing with players."
    
    # Stemming
    stemmed_text = perform_stemming(input_text)
    print("Stemmed Text:")
    print(stemmed_text)
    
    # Lemmatization
    lemmatized_text = perform_lemmatization(input_text)
    print("\nLemmatized Text:")
    print(lemmatized_text)
