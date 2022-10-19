words = []
alphabet = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
    '\n':0
    }

alphMiddleLetters =alphabet.copy()

alphBeforeMidLetters =alphabet.copy()

alphAfterMidLetters =alphabet.copy()

digraphs = {'ch':0, 'ck':0, 'gh':0, 'kn':0, 'mb':0, 'ng':0, 'ph':0, 'sh':0, 'th':0, 'wh':0, 'wr':0}

f = open('dict.txt')

for word in f:
    #print(word)
    word.strip('\n')
    for char in word:
        alphabet[char] += 1
        if word.index(char) == 2 :
            #print(word)
            #if char == 'n':
            #   print(word)
            alphMiddleLetters[char] +=1
        elif word.index(char) < 2: 
            alphBeforeMidLetters[char] +=1
        elif word.index(char) > 2: 
            alphAfterMidLetters[char] += 1

    #if (word.find('a') != -1) and word.index('a') == 1:
    #    if (word.find('l') != -1) and word.index('l') == 3:
    #       print(word)
         
    for value in digraphs: 
        if word.find(value) != -1:
            #print(word)
            digraphs[value] +=1

        
        #if(char == alphabet[char]):
            #alphabet[char] += 1
    words.append(word)

alphabet.pop('\n')
sortedLetterFreq = sorted(alphabet.items(), key=lambda x: x[1],reverse = True)

sortedDigraphFreq = sorted(digraphs.items(), key = lambda x: x[1], reverse = True)

alphMiddleLetters = sorted(alphMiddleLetters.items(), key = lambda x: x[1], reverse= True)

alphBeforeMidLetters = sorted(alphBeforeMidLetters.items(), key = lambda x: x[1], reverse= True)

alphAfterMidLetters.pop('\n')
alphAfterMidLetters = sorted(alphAfterMidLetters.items(), key = lambda x: x[1], reverse= True)

#print(alphabet)
print("")
print("Letter frequency within 5 charater english words")
print(sortedLetterFreq)
print("")
print("Digraph frequency within 5 charater english words")
print(sortedDigraphFreq)
print("")
print("Letters most common in the middle of 5 character English words")
print(alphMiddleLetters)
print("")
print("Letters most common to be in the first two positions of 5 character English words")
print(alphBeforeMidLetters)
print("")
print("Letters most common to be in the last two positions of 5 character English words")
print(alphAfterMidLetters)

mostValuedWord = ""
wordValue = 0 
for word in words: 
    tempValue = 0
    for char in word:
        if char == '\n':
            break
        if word.count(char) == 1:
            tempValue += alphabet[char]
    if(tempValue > wordValue):
        mostValuedWord = word
        wordValue = tempValue

print("finding word consistanting of most common letters found in 5 character english words")
print(wordValue)
print(mostValuedWord)
