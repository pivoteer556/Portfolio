ARGS = []
ARGS = sys.argv
total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
print ("Script name: %s" % str(sys.argv[0]))
GLOBAL_DICTIONARY_LIST = []
MYARGS = []
LIST_OF_FILES_AND_NUMBERS = []
MYARGS = glob.glob(ARGS[1])
def main(ARGS):
    yearsHot, yearsCold, yearsRain = parse(ARGS)
    printer(yearsHot, yearsCold, yearsRain)

def parse(ARGS):
    document = ARGS.readlines() #read the one file put in
    currentMax = 0
    currentMin = 9999.99
    currentPrecip = 0
    currentStation = "0"
    yearsHot = []
    yearsCold = []
    yearsRain = []
    for line in document:
        numbers = line.split() #split the lines into idividual numbers
        if currentStation != numbers[0]: #add averages
            yearsHot.append(hotYear) #add the hottest year
            currentMax = 0 #reset value
            yearsCold.append(coldYear) #add the coldest year
            currentMin = 0 #reset value
            yearsRain.append(rainyYear) #add the rainiest year
            currentPrecip = 0 #reset value
            currentStation = numbers[0] update current station
        if currentStation == numbers[0]: #check to make sure we're on the same station
            if currentMax < numbers[2]: #was this year the highest average temperature so far
                currentMax = numbers[2]
                hotYear = numbers[1]
            if currentMin > numbers[3] and numbers[3] != "-9999.99":#check to see which year was the lowest average annual temperature
                currentMin = numbers[3]
                coldYear = numbers[1]
            if currentPrecip < numbers[4]:#check to see which year was the highest average annual precipitation
                currentPrecip = numbers[4]
                rainyYear = numbers[1]
    return(yearsHot, yearsCold, yearsRain)
def printer(yearsHot, yearsCold, yearsRain):
    myFile = open("MissingPrcpData.out", 'w')
        
                
main(ARGS)
    
