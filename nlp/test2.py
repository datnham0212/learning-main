from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

lem = WordNetLemmatizer()

sentence = "He jumps over them. He has better skills than others. He studies hard to understand the studying material."

sentence_tokens = word_tokenize(sentence)

lemmatized_tokens = [lem.lemmatize(token, pos='v') for token in sentence_tokens]

output = ' '.join(lemmatized_tokens)

print(output)