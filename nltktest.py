from nltk.tokenize import sent_tokenize, word_tokenize

#EXAMPLE_TEXT = "heart rate 78 bpm, temperature 98 F. pediatric cancer in low-income countries. I love ES96. Drug administration is accordingly riskier. A unicorn is a fictional animal."

#print file.readline()
import itertools

words = []
with open('exampletext.txt','r') as f:
    for line in f:
        for word in line.split():
           words.append(str(word))   
        # Store the numbers in a set, and use the set to check if the number already exists


length = len(words)
for k in range(length-2):
    keyword1 = words[k]
    keyword2 = words[k+1]
    num = words[k+2]
    if(keyword1 == 'heart' and keyword2 == 'rate'):
        print "Heart Rate:", num
        
for k in range (length-1):
    keyword1 = words[k]
    num = words[k+1]
    if(keyword1 == 'temperature'):
        print "Temperature:", num
        
    #break