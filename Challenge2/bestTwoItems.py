import sys

#grab command line arguments
args = sys.argv
allItems = [];
balance = int(args[2]);

#read all lines into a file
file=open(str(args[1]), "r")
for line in file:
    item = line.rsplit(' ', 1);
    allItems.append(item)

#start algorithm (explanation in the README)
forward = 0;
backward = len(allItems)-1
notFinished = True;
bestNumber = 0
bestPair = [];

while (notFinished):

    f = allItems[forward]
    b = allItems[backward]

    fInt = int(f[1])
    bInt = int(b[1])
    sum = fInt + bInt

    if (sum>balance):
        backward = backward - 1
    else:
        forward = forward + 1
        if (sum>bestNumber or sum == balance):
            bestPair = []
            bestNumber = sum
            bestPair.append(f)
            bestPair.append(b)

	    if (sum == balance):
	       break

    if forward == backward :
        notFinished = False
if (bestNumber!=0):
    print ("You will be spending: "+ str(bestNumber))
    print (str(bestPair[0][0])+" "+str(bestPair[0][1])+ " and "+ str(bestPair[1][0]) + " "+ str(bestPair[1][1]))
else:
    print ("Not possible")
