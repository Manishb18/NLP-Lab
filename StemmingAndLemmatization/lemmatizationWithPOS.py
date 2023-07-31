import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_with_pos(sentence):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)

    lemmatized_words = []
    for word, tag in pos_tags:
        wordnet_pos = get_wordnet_pos(tag)
        lemmatized_words.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return " ".join(lemmatized_words)

if __name__ == "__main__":
    input_sentence = "The quick best brown foxes are jumping over the lazy dogs."
    lemmatized_sentence = lemmatize_with_pos(input_sentence)
    print("Input Sentence:", input_sentence)
    print("Lemmatized Sentence:", lemmatized_sentence)
