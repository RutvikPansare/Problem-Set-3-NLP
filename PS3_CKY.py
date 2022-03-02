"""
NLP 681 PS3
Author: Rutvik pansare rp2832
"""
def CKY(sentence,grammer):
    sentence = sentence.split()
    OPT = [[[] for i in range(len(sentence)+1)] for i in range(len(sentence)+1)]
    path = [[[] for i in range(len(sentence) + 1)] for i in range(len(sentence) + 1)]
    count = len(sentence)
    for i in range(0,len(sentence)):
        for key, value in grammer.items():
            if sentence[i] in value:
                OPT[i+1][i+1].append(key)
                path[i+1][i+1] = [sentence[i]]

    for p in range(1,len(sentence)):
        j=p + 1
        for i in range(1,count):
            if j > i:
                sub_CKY(sentence,grammer,i,j,OPT,path)
                j = j+1
        count = count - 1
    return OPT,path


def sub_CKY(sentence,grammer,i,j,OPT,path):
    result = []
    mid = i
    for _ in range(j-i):
        first = OPT[i][mid]
        second = OPT[mid + 1][j]
        for x in first:
            for y in second:
                new_string = x+y
                keys = []
                for key, value in grammer.items():
                    if x in value:
                        if y in value:
                            keys.append(key)
                            path[i][j] = [(i,mid),(mid+1,j)]
                result.extend(keys)

        mid = mid + 1
    converted_set = set(result)
    result = list(converted_set)
    OPT[i][j] = result
def make_grammer_Dict(data):
    f = open(data, "r")
    newlist = [line.rstrip() for line in f.readlines()]
    grammer = {}
    for line in newlist:
        line = line.strip().split()
        firstWord = line[0]
        second = line[1]
        if firstWord not in grammer:
            grammer[firstWord] = line[2:]
        else:
            value = grammer[firstWord]
            value.extend(line[2:])
    return grammer

def print_path(OPT,path,length,grammer):
    for i in range(length):
        for j in range(length,0,-1):
            destination = OPT[i][j]
            if "S" in destination:
                print(OPT[i][j])
                print("  \\")
                printRecursively(i,j,OPT,path,4)
                return


def printRecursively(i,j,OPT,path,mul):
    destination = path[i][j]
    length = len(destination)

    if length < 2:
        mystring = " " * mul
        mul = mul + 2
        print(mystring + str(destination))
        return
    else:
        for i in range(len(destination)):
            (x, y) = destination[i]
            mystring = " " * mul
            print(mystring + str(OPT[x][y]))
            print(mystring +"   "+ "\\")
            printRecursively(x, y, OPT, path,mul+2)

"""
Please chose the proper grammer file to run the parser for the respective sentence
sentence1: grammar file name -> "PS3_input_1.txt"
sentence2: grammar file name -> "PS3_input_2.txt"
sentence3: grammar file name -> "PS3_input_3.txt"
sentence4: grammar file name -> "PS3_input_4.txt"
sentence5: grammar file name -> "PS3_input_5.txt"
"""

sentence1 = "He hath eaten me out of house and "
sentence2 = "tis not long after but i will wear my heart upon my sleeve ."
sentence3 =  "You know that smoodle pinkered and that I want to get him"
sentence4 = "My door sat through the lamp in the "
sentence5 = "A self-driving small-sized car stopped at the light"

sentences = [sentence1,sentence2,sentence3,sentence4,sentence5]

# enter the name of the sentence to parse as the variable name
#Options:  sentence1,sentence2,sentence3,sentence4,sentence5
sentence_to_parse = sentence1
# enter the file name corresponding to the sentence chosen.
grammer = make_grammer_Dict("PS3_input_1.txt")

length_sentence = len(sentence_to_parse.split())
OPT,path = CKY(sentence_to_parse,grammer)
print_path(OPT,path,length_sentence,grammer)