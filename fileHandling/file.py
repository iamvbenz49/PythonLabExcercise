
file = open("sample.txt","r")
wordcount = {}
for i in file.read().split():
  if i not in wordcount:
    wordcount[i] = 1
  else:
    wordcount[i] += 1

file.close()
maxFreq = 0
for i in wordcount:
  if wordcount[i]>maxFreq:
    maxFreq = wordcount[i]
for i in wordcount:
  if wordcount[i]==maxFreq:
    print(i)