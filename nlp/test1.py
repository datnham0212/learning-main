from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = "Hello, my name is John. I am a student at the University of California, Berkeley. I am studying computer science."

output = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered = [word for word in output if word.lower() not in stop_words]

print(filtered)
