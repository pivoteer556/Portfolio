#!/usr/bin/python
#answer1.py
#code by Alexander Wilkening 6/3/2017
#enter any directory and program will test every file.
import sys
import glob
import json
import os.path
from operator import itemgetter
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
print(MYARGS)
def main(ARGS):
    print(ARGS)
    for document in ARGS: #open each file
        MaxTempRecordCount = 0  #insantiate the amount of hits found in this document for all stats recorded
        MinTempRecordCount = 0
        PrecipCount = 0
        TotalMaxTemp = 0
        TotalMinTemp = 0
        TotalPrecip = 0
        if "desktop.ini" not in document:
            year = 1985
            document = open(document, "r")
            myDocument = document.readlines() #read the lines
            for line in myDocument: #go through each document
                if int(line[:4]) != year:
                    year += 1
                    print(year)
                    if int(MaxTempRecordCount) == 0:
                        AVGMax = "-9999.00"
                    else:
                        AVGMax = TotalMaxTemp/MaxTempRecordCount #each mean is the total divided by data points
                        AVGMax = str(round(AVGMax, 2))
                    if int(MinTempRecordCount) == 0:
                        AVGMin = "-9999.00"
                    else:
                        AVGMin = TotalMinTemp/MinTempRecordCount
                        AVGMin = str(round(AVGMin, 2))
                    if int(PrecipCount) == 0:
                        AVGPrecip = "-9999.00"
                    else:
                        AVGPrecip = TotalPrecip/PrecipCount
                        AVGPrecip = str(round(AVGPrecip, 2))
                    LIST_OF_FILES_AND_NUMBERS.append([document.name, year, AVGMax, AVGMin, AVGPrecip]) #save the document and the amount of hits to a dictionary to be stored in a list of dictionaries
                numbers = line.split() #split the lines into idividual numbers
                myCounter = 0 #instantiate the condition tester variable
                verificationCounter = 0 #instantiate the verifier for multiple conditions
                while myCounter < 4 : #check to see if there is a data point
                    if myCounter == 1 and int(numbers[myCounter]) != -9999:
                        TotalMaxTemp += (int(numbers[myCounter])/10) #add data point (in appropriate measurement)
                        MaxTempRecordCount += 1 #add amount of data points for mean generation
                    if myCounter == 2 and int(numbers[myCounter]) != -9999:
                        TotalMinTemp += (int(numbers[myCounter])/10)
                        MinTempRecordCount += 1
                    if myCounter == 3 and int(numbers[myCounter]) != -9999:
                        TotalPrecip += (int(numbers[myCounter])/100)
                        PrecipCount += 1
                    myCounter +=1
    printer(LIST_OF_FILES_AND_NUMBERS)

def printer(LIST_OF_FILES_AND_NUMBERS):
    sorted(LIST_OF_FILES_AND_NUMBERS, key=itemgetter(0))
    myFile = open("YearlyAverages.out", 'w')
    for item in LIST_OF_FILES_AND_NUMBERS:
        head, tail = os.path.split(str(item[0]))
        print(tail)
        myFile.write(tail+"\t"+str(item[1])+"\t"+str(item[2])+"\t"+str(item[3])+"\t"+str(item[4]) + "\n")

main(MYARGS)
