###########################
# 6.00.2x Problem Set 1: Space Cows 

from problemSet1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

class Cow(object):
    def __init__(self, n, w):
        self.name = n
        self.weight = int(w)
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.name) + ': <' + str(self.weight) + '>'


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

def buildListofCows(cows):
    
    list_cows = []

    for k,v in cows.items():
        
        list_cows.append(Cow(k,v))
        
    list_cows = sorted(list_cows, key=Cow.getWeight, reverse=True)
        
    return list_cows
    
    
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        
        withVal, withoutVal = 0,0
        
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += 1
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(Cows, maxUnits, returnItems = True):
    print('Use search tree to allocate', maxUnits,
          'tons')
    trip = []
    val, taken = maxVal(Cows, maxUnits)
    print('Numbers of Cows taken on trip =', val)
    if returnItems:
        for item in taken:
            print('   ', item)
            trip.append(item.getName())
        return trip
    
# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip = []
    # Create a copy of the original dictionaty
    cash_cows = buildListofCows(cows)
    
    #Trace the space left in the spaceship
    left = limit
    
    subtrip = []
    
    
    for i in range(len(cash_cows)):
                   
        if cash_cows[i].getWeight() > limit:
            next                    
        elif cash_cows[i].getWeight() <= space_left:            
            subtrip.append(cash_cows[i].getName())
            space_left = space_left - cash_cows[i].getWeight()
        else:
            
                   
        
            
    if len(subtrip) != 0:
        trip.append(subtrip)
                
    return trip            
            
            
            
            
            
        
    




# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


