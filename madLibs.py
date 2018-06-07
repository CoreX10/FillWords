#!python3

import re,os

input_list = []
for i in ['adjective','noun','verb','noun']:
    print('Enter a ' + i +':')
    input_words = str(input()).lower()
    input_list += [input_words]

sentenceFile = open('E:\\learnpython\FillWords\sentence.txt')
sentenceText = sentenceFile.read()

wordRegex = re.compile(r'[A-Z][A-Z]+')
words = wordRegex.findall(sentenceText)

for i in words:
    

print(str(words))
sentenceFile.close()

