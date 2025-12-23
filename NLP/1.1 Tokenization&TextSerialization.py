import nltk
from nltk.tokenize import word_tokenize
text = "Selmon bhai!"
tokens = word_tokenize(text)
print(tokens)

#sentence tokenization
from nltk.tokenize import sent_tokenize
text = "Hello Mr. Vinay, how are you doing today? The weather is great, and Python is awesome. The sky is blue."
sentences = sent_tokenize(text)
print(sentences)

#word tokenization
from nltk.tokenize import word_tokenize
text = "Hello Mr. Vinay, how are you doing today?"
words = word_tokenize(text)
print(words)

#Text Serialization
import nltk
