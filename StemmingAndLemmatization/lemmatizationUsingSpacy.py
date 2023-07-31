import spacy
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp('the bats saw the cats with best stripes hanging upside down by their feet')

# Create list of tokens from given string
tokens = []
for token in doc:
	tokens.append(token)

print(tokens)

lemmatized_sentence = " ".join([token.lemma_ for token in doc])

print(lemmatized_sentence)