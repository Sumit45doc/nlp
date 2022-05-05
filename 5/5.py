# Q5. Write a program to implement word sense disambiguation. 
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
import codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

def filteredSentence(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer() 
    ps = PorterStemmer() 

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)
    return filtered_sent

def synonymsCreator(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

def simlilarityCheck(word1, word2):

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0


def simpleFilter(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))
    return filtered_sent


if __name__ == '__main__':

    fileA = codecs.open("file_a.txt", 'r', "utf-8")
    sent2 = fileA.read().lower()
    fileB = codecs.open("file_b.txt", 'r', 'utf-8')
    sent1 = fileB.read().lower()
    query = "start"

    while(query != "end"):

        query = input("Enter Query: ").lower()

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_query = []

        counter1 = 0
        counter2 = 0
        query1_similarity = 0
        query2_similarity = 0

        filtered_sent1 = simpleFilter(sent1)
        filtered_sent2 = simpleFilter(sent2)
        filtered_query = simpleFilter(query)

        for i in filtered_query:

            for j in filtered_sent1:
                counter1 = counter1 + 1
                query1_similarity = query1_similarity + simlilarityCheck(i, j)

            for j in filtered_sent2:
                counter2 = counter2 + 1
                query2_similarity = query2_similarity + simlilarityCheck(i, j)

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_query = []

        filtered_sent1 = filteredSentence(sent1)
        filtered_sent2 = filteredSentence(sent2)
        filtered_query = filteredSentence(query)

        sent1_count = 0
        sent2_count = 0

        for i in filtered_query:

            for j in filtered_sent1:

                if(i == j):
                    sent1_count = sent1_count + 1

            for j in filtered_sent2:
                if(i == j):
                    sent2_count = sent2_count + 1

        if((sent1_count + query1_similarity) > (sent2_count+query2_similarity)):
            print("Mammal Bat")

        else:
            print("Cricket Bat")

    print("\nTERMINATED")