#!/usr/bin/python
#answer1.py
#code by Alexander Wilkening 6/3/2017
#enter any directory and program will test every file.
import sys
import glob
import json
import os.path
ARGS = []
ARGS = sys.argv
total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
print ("Script name: %s" % str(sys.argv[0]))
#for i in xrange(total):
    #print ("Argument # %d : %s" % (i, str(sys.argv[i])))
    
GLOBAL_DICTIONARY_LIST = []
MYARGS = []
LIST_OF_FILES_AND_NUMBERS = []
MYARGS = glob.glob(ARGS[1])
def main(ARGS):
    for document in ARGS: #open each file
        amountOfHits = 0  #insantiate the amount of hits found in this document
        if "desktop.ini" not in document:
            document = open(document, "r")
            myDocument = document.readlines() #read the lines
            for line in myDocument: #go through each document
                numbers = line.split() #split the lines into idividual numbers
                myCounter = 0 #instantiate the condition tester variable
                verificationCounter = 0 #instantiate the verifier for multiple conditions
                while myCounter < 4 : #check each condition we need
                    if myCounter == 1 and int(numbers[myCounter]) != -9999:
                        verificationCounter += 1
                    if myCounter == 2 and int(numbers[myCounter]) != -9999:
                        verificationCounter += 1
                    if myCounter == 3 and int(numbers[myCounter]) == -9999:
                        verificationCounter += 1
                    if verificationCounter == 3:
                        amountOfHits +=1
                    myCounter +=1
        fileAndHits = [document.name, amountOfHits] #save the document and the amount of hits to a dictionary to be stored in a list of dictionaries
        LIST_OF_FILES_AND_NUMBERS.append(fileAndHits) #add aforementioned dict to aforementioned list
    printer(LIST_OF_FILES_AND_NUMBERS)

def printer(LIST_OF_FILES_AND_NUMBERS):
    myFile = open("MissingPrcpData.out", 'w')
    for item in LIST_OF_FILES_AND_NUMBERS:
        head, tail = os.path.split(str(item[0]))
        myFile.write(tail + "\t" + str(item[1]) + "\n")

main(MYARGS)
                    
