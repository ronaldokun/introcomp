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
        return str(self.name) + ': <' + str(self.weight) + '> tons'


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


def nextVal(toConsider, avail):
    """Assumes toConsider an ordered list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem with the constraint that
         it's obliged to pick the next most heavy item first, i.e, always
         explore the left branch of the graph first if it there is space.

         """
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = nextVal(toConsider[1:], avail)
    else:

        nextItem = toConsider[0]

        #Explore left branch
        withVal, withToTake = nextVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += nextItem.getWeight()

        result = (withVal, withToTake + (nextItem,))

    return result

def testNextVal(Cows, maxUnits, returnItems = True):
    #print('Use search tree to allocate', maxUnits,
    #     'tons')
    trip = []
    val, taken = nextVal(Cows, maxUnits)
    #print('Numbers of Cows taken on trip =', val)
    if returnItems:
        for item in taken:
            #print('   ', item)
            trip.append(item)
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
    # Create an ordered by weight list of the original dictionary
    cash_cows = buildListofCows(cows)

    # this is a list of lists, each inner list is an individual trip
    voyage = []
    trip = []
    subtrip = []
    #Trace the space left in the spaceship
    space_left = limit

    while(len(cash_cows)):
        #If the cow's weight is above the limit, she can't be transpórted
        if cash_cows[0].getWeight() > limit:

            cash_cows.pop(0)

        elif cash_cows[0].getWeight() <= space_left:

            trip.append(cash_cows[0])

            space_left -= cash_cows[0].getWeight()

            cash_cows.pop(0)

        else:
            #check if the remaining cows on the list fit the available space
            subtrip = testMaxVal(cash_cows[1:], space_left)

            if len(subtrip):
                trip += subtrip

            #remove the allocated cows from the original list
            for item in trip:
                if item in cash_cows:
                    cash_cows.remove(item)

            voyage.append([item.getName() for item in trip])

            trip, subtrip = [],[]

            space_left = limit

    # If the last iteration did't enter the else block
    if(len(trip)):
        voyage.append([item.getName() for item in trip])



    return voyage


def fastMaxVal(toConsider, avail, memo = {}):

    """Assumes toConsider a list of subjects,
       avail a weight
       memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
       0/1 knapsack problem and the subjects of that solution

       Notice: the Weight is both the cost and the value metric
    """
    if (len(toConsider), avail) in memo:
        return memo[(len(toConsider), avail)]

    elif toConsider == [] or avail == 0:
        return (0,())

    elif toConsider[0].getWeight > avail:
        #Explore right branch only
        fastMaxVal(toConsider[1:], avail, memo)

    else:

        nextItem = toConsider[0]

        withVal, withToTake = fastMaxVal(toConsider[1:],
                                         avail - nextItem.getWeight(), memo)

        withVal += nextItem.getWeight()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                             avail, memo)

        #Choose better branch
        if withVal > withoutVal:
            return (withVal, withToTake + (nextItem,))

        else:
            result = (withoutVal, withoutToTake)

    memo[(len(toConsider), avail)] = result

    return result


def testMaxVal(Cows, maxUnits, returnItems = True):
    #print('Use search tree to allocate', maxUnits,
    #     'tons')
    trip = []
    val, taken = fastMaxVal(Cows, maxUnits)
    #print('Numbers of Cows taken on trip =', val)
    if returnItems:
        for item in taken:
            #print('   ', item)
            trip.append(item)
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

    #Create ordered list by weight of cows
    # Create an ordered by weight list of the original dictionary
    cash_cows = buildListofCows(cows)

    cow_partitions = get_partitions(cash_cows)

    trip = []

    for partitions in cow_partitions:
        for partition in partitions:
            trip.append(testMaxVal(partition,limit))
        if len(trip) == len(cash_cows):
            break
        else:




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
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    start1 = time.time()
    result = greedy_cow_transport(cows, limit)
    end1 = time.time()
    print('\n *** Greedy time: {}'.format(end1 - start1))


    start2 = time.time()
    result = brute_force_cow_transport(cows, limit)
    end2 = time.time()
    print('\n *** Brute force time: {}'.format(end2 - start2))

    print('\n * * * *  Ratio: {}'.format((end2 - start2)/(end1 - start1)))

"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
