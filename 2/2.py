'''
Q2. Write a program to build a bigram language model.
'''
import sys

def readFile(filename): 
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            modLines = []
            words = []
            for line in lines:
                modLines.append(line.strip())
                for word in line.split():
                    words.append(word)

            return modLines, words  

    except IOError:
        print("Error reading input file.")
        sys.exit()
  
def createBigram(words):
   listOfBigrams = []
   bigramCounts = {}
   unigramCounts = {}

   for i in range(len(words)-1):
      if i < len(words) - 1 and words[i+1].islower():

         listOfBigrams.append((words[i], words[i + 1]))

         if (words[i], words[i+1]) in bigramCounts:
            bigramCounts[(words[i], words[i + 1])] += 1
         else:
            bigramCounts[(words[i], words[i + 1])] = 1

      if words[i] in unigramCounts:
         unigramCounts[words[i]] += 1
      else:
         unigramCounts[words[i]] = 1
   return listOfBigrams, unigramCounts, bigramCounts


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    return listOfProb


if __name__ == '__main__':
    lines, words = readFile('corpus.txt')

    print("Lines:", lines,"\n\nWords (Unigrams):", words)

    listOfBigrams, unigramCounts, bigramCounts = createBigram(words)

    print("\nBigrams:", listOfBigrams)
    print("\nUnigrams | Frequency: \n", unigramCounts)
    print("\nBigrams | Frequency: \n", bigramCounts)

    bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)

    print("\nBigrams | Probability: \n", bigramProb)

    inputList="benefit of extra space for typing commands"
    splt=inputList.split()
    
    outputProb1 = 1
    bilist=[]
    bigrm=[]

    for i in range(len(splt) - 1):
        if i < len(splt) - 1:

            bilist.append((splt[i], splt[i + 1]))

    print("\nThe bigrams in given sentence are \n", bilist)
    for i in range(len(bilist)):
        if bilist[i] in bigramProb:
            outputProb1 *= bigramProb[bilist[i]]

        else:
            outputProb1 *= 0

    print('\nP("', inputList, '") = % 0.6f'% outputProb1)
