# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

fileName="c:/Users/user/Documents/PYTHON/tasks/read_file/story.txt"

def read_file_content(fileName):
    openFile = open(fileName, "r") 
    readFile=openFile.read()

    for item in readFile:
        item= item.strip().lower().strip("/n,.?")
    
    splitWords=readFile.split(" ")

    openFile.close()

    return splitWords

def count_word():
    wordLists=read_file_content(fileName)
    counts={}
    for word in wordLists:
        if word in counts:
            counts[word] +=1
        else:
            counts[word]=1

    for key in list(counts.keys()):
        print(key, ":", counts[key])

    return count_word


print(count_word())