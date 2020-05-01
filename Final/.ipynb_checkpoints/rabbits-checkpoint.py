import random
import pylab

# Global Variables
MAXRABBITPOP = 10000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    steps = CURRENTRABBITPOP
    
    for i in range(steps):
        
        pRabbitReprod = 1.0 - float(CURRENTRABBITPOP/MAXRABBITPOP)
        
        if random.random() <= pRabbitReprod:
            CURRENTRABBITPOP += 1
            
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    steps = CURRENTFOXPOP
    
    # Check constraints of the problem
    if CURRENTRABBITPOP > 10 and CURRENTFOXPOP > 10:
        
        for i in range(steps):
            
            pFoxEatsRabbit = float(CURRENTRABBITPOP/MAXRABBITPOP)
            
            if random.random() <= pFoxEatsRabbit:
                CURRENTRABBITPOP -= 1
                
                if random.random() <= float(1.0/3):
                    CURRENTFOXPOP += 1
                
                # Check Constraints again, since rabbit pop has declined
                if CURRENTRABBITPOP == 10:break
            
            elif random.random() <= float(1/10):
                CURRENTFOXPOP -= 1
                
                # Check constraints again, since fox pop has declined
                if CURRENTFOXPOP == 10: break
                
            
                    
            
                
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    
    rabbit_populations, fox_populations = [],[]
    
    for i in range(numSteps):
        
        #update the rabbit number
        rabbitGrowth()
        
        #update the fox number
        foxGrowth()
        
        rabbit_populations.append(CURRENTRABBITPOP)
        
        fox_populations.append(CURRENTFOXPOP)
        
    
    return (rabbit_populations, fox_populations)
        


rabbit, fox = runSimulation(200)

pylab.plot(rabbit, '-b', label = "Rabbit") 
pylab.plot(fox, '-r', label = "Fox")
pylab.xlabel = ('Time')
pylab.ylabel = ("Population")
pylab.legend(loc = "best")

#coeff = pylab.polyfit(range(len(rabbit)), rabbit, 2)
#
#pylab.plot(pylab.polyval(coeff, range(len(rabbit))), '-b')
#
#coeff = pylab.polyfit(range(len(fox)), fox, 2)
#
#pylab.plot(pylab.polyval(coeff, range(len(fox))), '-r')



        
        
