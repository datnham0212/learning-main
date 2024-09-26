import string
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

import spacy
nlp = spacy.load("en_core_web_sm")

text = """<p id="original-text">
Welcome to the world of Natural Language Processing (NLP)! 
This paragraph delves into the fascinating realm of text analysis, where we'll unravel the magic behind understanding & manipulating human language. Let's embark on a journey through an NLP pipeline, transforming raw text into structured insights. We'll encounter challenges like contractions (e.g., "can't," "wouldn't"), possessives ("Mary's cat," "the company's profits"), hyphenated words ("state-of-the-art," "well-being"), and even emoticons (:-), 😉). Punctuation marks like commas, semicolons (;), and exclamation points (!) will also play a role. Brace yourselves for a captivating exploration of how machines decipher the intricacies of human communication! 
</p>"""
doc = nlp(text)


#Sentence segmentation
#METHOD 1
# text_sentences = sent_tokenize(text)
# print("Sentence Segmentation:")
# for sentence in text_sentences:
#     print(sentence)

#METHOD 2
text_sentences = [sent for sent in doc.sents]
temp = 0
# print("Sentence Segmentation:")
for sentence in text_sentences:
    temp += len(sentence)
#     print(sentence)
print(temp)

#TIL: tokenization is a form of segmentation, but not all segmentation are tokenizations


#Tokenization
#METHOD 1
# words = word_tokenize(text)
# print("Tokenization:")
# print(words)

#METHOD 2
tokens = [token.text for token in doc]
print(len(tokens))
# print(tokens)

#Spacy's tokenization == NLTK's word tokenization
#Spacy's sentence segmmentation == NLTK's sentence tokenization


#Text normalization
#Variation 1
# normalized_tokens = word_tokenize(text.lower())
# print(normalized_tokens)

#Variation 2
normalized_tokens = [token.lower() for token in tokens]
print(len(normalized_tokens))
# print("\nText Normalization (Lowercasing):")
# print(normalized_tokens)


#Stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in normalized_tokens if token not in stop_words]
print(len(filtered_tokens))
# print(filtered_tokens)


#Text cleaning
translator = str.maketrans('','', string.punctuation)
cleaned_tokens = [token.translate(translator) for token in filtered_tokens]
print(len(cleaned_tokens))
# print(cleaned_tokens)


#Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in cleaned_tokens]
print(len(stemmed_tokens))

#Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]
print(len(lemmatized_tokens))

