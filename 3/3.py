# Q3. Write a program for Part of Speech Tagging with NLTK. 

import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


def POS(input_text):
    tokenized = sent_tokenize(input_text)
    for i in tokenized:
        wordsList = word_tokenize(i)
        print(wordsList)
        tagged = nltk.pos_tag(wordsList)
        print(tagged)

if __name__ == '__main__':
    text = '''Lord Krishna the supreme power of all, represents love, wisdom, and intellect. The eighth incarnations of Lord Vishnu gave sacred knowledge to Arjuna on the battlefield of Kurukshetra, which we know today as Bhagvad Gita is still relevant today. Srimad Bhagavad Gita comprises of 700 verses, originally in Sanskrit translated in Hindi and English. The religious book contains golden words of wisdom by Lord Krishna. From Dharma to Karma the book is a huge knowledge of seas.'''
    POS(text)
