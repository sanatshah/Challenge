import sys
import gc
import math
import traceback


def printStringWithCombo(string, numOfXs, combo):
    updatedString = string
    comboString = str(combo)[2:] 

    #add any missing zeroes to the beginning of the string
    if (len(comboString)<len(numOfXs)):
        for i in range(0, len(numOfXs)-len(comboString)):
            comboString="0" + comboString
	
    #replace the X indexs in the original string with the combo
    for i, value in enumerate(comboString):    
        updatedString = list(updatedString)
        updatedString[numOfXs[i]] = value
	"".join(updatedString)

    print(str("".join(updatedString)))


    #finished when all numbers in combostring are 1 
    notFinished = False 
    for i in comboString: 
	if (i == '0'):
	   notFinished = True
	   
    return notFinished 



if (__name__ == "__main__"): 
    try:

      #grab needed information
      string = sys.argv[1]
      numOfXs = [i for i, letter in enumerate(string) if letter == 'X']

      #binary addition to figure out all the combos, iterating 2^(len(numOfXs)) times
      combo = '0b0'
      printStringWithCombo(string, numOfXs, combo)
      notFinished = True

      while(notFinished):
    	combo = bin(int(combo,2) + int('1',2))
        notFinished = printStringWithCombo(string, numOfXs, combo)
        gc.collect()

    except MemoryError:
      print("Out of memory") 


