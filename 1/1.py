# Q1. Write a program to measure the document similarity. 
import math
import sys
import string

def read_file(filename): 
      
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data
      
    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()
  
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                     " "*len(string.punctuation)+string.ascii_lowercase)
       
def get_words_from_line_list(text): 
      
    text = text.translate(translation_table)
    word_list = text.split()
      
    return word_list
  
def countFrequency(wordList): 
    dat = {}
      
    for word in wordList:
          
        if word in dat:
            dat[word] = dat[word] + 1
              
        else:
            dat[word] = 1
              
    return dat
  
def wordFrequenciesForFile(filename): 
      
    line_list  = read_file(filename)
    word_list = get_words_from_line_list(filename)
    freq_mapping = countFrequency(word_list)
  
    print("File", filename, ":", )
    print(len(line_list), "lines, ", )
    print(len(word_list), "words, ", )
    print(len(freq_mapping), "distinct words")
  
    return freq_mapping
  
  
def dotProduct(doc1, doc2): 
    sum = 0.0
      
    for key in doc1:
          
        if key in doc2:
            sum += (doc1[key] * doc2[key])
              
    return sum
  
def vectorAngle(doc1, doc2): 
    numerator = dotProduct(doc1, doc2)
    denominator = math.sqrt(dotProduct(doc1, doc1)*dotProduct(doc2, doc2))
      
    return math.acos(numerator / denominator)
  
  
def documentSimilarity(filename_1, filename_2):
      
    wordDic1 = wordFrequenciesForFile(filename_1)
    wordDic2 = wordFrequenciesForFile(filename_2)
    distance = vectorAngle(wordDic1, wordDic2)
      
    print("\nThe distance between the documents is: % 0.6f (radians)"% distance)
      
if __name__ == '__main__':
    documentSimilarity('file_a.txt', 'file_b.txt')