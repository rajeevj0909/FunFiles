import string # line 41 for reference


def readFile(fileName):
    output = []
    f = open(fileName,"r")  # opens file for reading, fileName is the input to the function
    lines = f.read().splitlines()  # creates variable 'lines' which becomes an array of strings for each line of the file
    for i in lines:         # loops through each sentence of the array lines
        splitSentence = i.split(" ") # each sentence(line of file) is split on the spaces (splitting up words) into an new array
        output.append(splitSentence) # each word then appended to an output array becoming an array of arrays - print output to check!
    f.close()
    # print(lines) # - uncomment this and run the function to see what we are looping through
    return output

def writeFile(fileName, inputData):
    templist = []  # empty array to hold temporary data
    f = open(fileName,"w")  # opens file for writing, fileName is the input to the function
    for sentence in inputData:  # input data is the array of arrays (outer arrray - line of file, inner array - each word on line)         
        tempSentence = " ".join(sentence) # for each word in the array, join together with a space inbetween
        templist.append(tempSentence)  # add this new sentence to the templist as its own element in the array (a string)
        
    for sentence in templist:  # now loop through the sentences in templist and write them to the file
        f.write(str(sentence)) 
        f.write("\n")   
    f.close()

def cleanseSentence(inputData):
    cleanSentenceArray = []
    # inputData is an array of arrays (list of sentences). We want to check each individual character and check for punctuation and change 
    # each first letter of a word to a capital
    for line in inputData:
        cleanSentence = []
        for word in line:
            tempWord = []
            for letter in word:
                if (ord(letter) >= 65 and ord(letter) <= 122) or ord(letter) == 39: # if a lowercase or uppercase letter then addd to temp array
                    tempWord.append(letter)

            if len(tempWord) != 0:  # if array not empty then join the letters together and add it to sentece
                cleanWord = "".join(tempWord)
                cleanSentence.append(string.capwords(cleanWord)) # capitalise first letter of each word - if use .title() then apostrophes messed up

        cleanSentenceArray.append(cleanSentence)
    return cleanSentenceArray

def capitalise(inputFile,outputFile):
    sentenceArray = readFile(inputFile)
    writeFileInput = cleanseSentence(sentenceArray)
    writeFile(outputFile,writeFileInput)

capitalise("output.txt","input.txt")

