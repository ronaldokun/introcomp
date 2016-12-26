import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    if title:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    # keep the longest run for each Trial
    longest = []
    
    for i in range(numTrials):
        
        # Creat a dictionary of longest runs for each number in the trial
        runs = {}
        
        # make the first die roll        
        lastRow = die.roll()

         # initiate dict for this number            
        if lastRow not in runs.keys():
            
            runs[lastRow] = 1
        
        # count the number of consecutive rolls of the die
        counter = 0
            
        for j in range(numRolls - 1):
            
            row = die.roll()
            
            if row == lastRow:
                
                counter += 1
                
                lastRow = row
                
            else:
                
                # Initiate count of current number
                if row not in runs.keys():
                    
                    runs[row] = 1
                
                # Update the number of consecutive rolls until last roll
                if runs[lastRow] <= counter + 1:
                    
                    runs[lastRow] = counter + 1
                
                lastRow = row
                
                counter = 0
                
        # Update dictionary in the case it didn't enter the else clause        
        if runs[lastRow] <= counter + 1:
                    
            runs[lastRow] = counter + 1
            
        
            
        maxRun = 0
        
        # It'll check for the longest roll in the dict and keep it 
        for k in runs.keys():
            
            if runs[k] > maxRun:
                maxRun = runs[k]
                
        longest.append(maxRun)
        
    mu, std = getMeanAndStd(longest)
    
    makeHistogram(longest, 10, ' size of longest consecutive draw', \
    '# of ocurrences')  
    
    return mu
        
            
        
        
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

#print(getAverage(Die([1,1]), 10, 1000))