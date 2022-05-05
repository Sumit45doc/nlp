# Q10. Write a program to implement the k-means algorithm for text clustering.
#  We use term freq. and inverse document freq. to get the statistics of the given doc.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

inputText = ["This little kitty came to play when I was eating at a restaurant.",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

def readFile(filename): 
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            return lines  

    except IOError:
        print("Error reading input file.")
        sys.exit()

inputText = readFile('corpus.txt')
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(inputText)

true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=30, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()
for i in range(true_k):
    print("Cluster %d: {"% i, end=""),
    for ind in order_centroids[i, :10]:
        print("%s" % terms[ind], end =", "),
    print("}")
print("\n")
print("Test")

testData = [
    "chrome browser to open.",
    "My cat is hungry."
]

for text in testData:
    Y = vectorizer.transform([text])
    prediction = model.predict(Y)
    print(text, ": cluster", prediction)
