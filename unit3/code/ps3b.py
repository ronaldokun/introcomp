# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab

#from ps3b_precompiled_35 import *

#random.seed(0)

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

        

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if random.random() >= self.getClearProb():
            return False
        else:
            return True
        

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        
        # Check if the virus particule will reproduce        
        probToReproduce = self.getMaxBirthProb() * (1.0 - popDensity)
        
        # A probability is always bigger or equal to zero, so we don't check
        # that 
        if random.random() >= probToReproduce:
            raise NoChildException
                        
        else:
            
            return SimpleVirus(self.maxBirthProb, self.clearProb)
            
        



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        
        self.viruses = viruses
        self.maxPop = maxPop
        
    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        
        return len(self.viruses)
                


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        
        # create a new list to accomodate the new population virus and
        # not mutate the current population while iterating over it
        virusesCopy = []
        
        for virus in self.getViruses():
            
            if not virus.doesClear():
                
                virusesCopy.append(virus)
        
        #update the viruses
        self.viruses = virusesCopy
        
        popDensity = self.getTotalPop()/self.getMaxPop()
        
        newViruses = []
        
        for virus in self.getViruses():
            
            try:
                child = virus.reproduce(popDensity)
                
                newViruses.append(child)
            
            except NoChildException:
                
                next
                
        #check if list is not empty
        if len(newViruses):
            self.viruses.extend(newViruses)
            
        return self.getTotalPop()
                

# maxBirthProb, clearProb     
#virus = SimpleVirus(0.9, 0.2)
#patient = Patient([virus], 100)
#
#trials = 20
#
#for i in range(trials):
#    
#    patient.update()
#    
#    print("\n Total Population of viruses at trial", i + 1, ":", patient.getTotalPop())
#    
#    print("\n Population Density: ", patient.getTotalPop()/patient.getMaxPop())
#    
    
                 
def runTimeSteps(patient, timeSteps):

    population = []
    
    for i in range(timeSteps):              
        
        patient.update()
        
        population.append(float(patient.getTotalPop()))
        
    return population


#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    #There are numTrials lists, each internal list contain the number of 
    # virus at each time step
    
    timeSteps = 300
    
    virusPop = [] 
    
    for i in range(numTrials):
        
        #Create a list of viruses   
        infection = [SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses)]
    
        #Instantiate one patient infected with numViruses
        patient = Patient(viruses=infection, maxPop = maxPop)
        
        virusPop.append(runTimeSteps(patient, timeSteps))
        
    averagePop = []
    
    sumStep = 0.0
    
    for i in range(timeSteps):
        
        for virus in virusPop:
            
            sumStep += virus[i]
            
        averagePop.append(float(sumStep/numTrials))
        
        sumStep = 0.0
        
              

    pylab.figure()    
        
    pylab.plot(averagePop, label = "SimpleVirus Population at time t")
    
    pylab.xlabel("Time Step")
    
    pylab.ylabel("Average Virus Population")
    
    pylab.title("SimpleVirus Simulation")
        
    pylab.legend(loc = "best")   
    
    pylab.show()
    
    
    
#simulationWithoutDrug(100, 1000, 0.1, 0.05, 300)
 
#Extreme Case: population should rapidly increase
#simulationWithoutDrug(100, 1000, 0.99, 0.05, 300)

#Extreme Case: Population should rapidly decrease   
#simulationWithoutDrug(100, 1000, 0.1, 0.99, 300)
        
        
        


def buildChildResistance(resistances, mutProb):
    
    childResistance = {}
            
    # check mutations in resistances           
    for drug,value in resistances.items():
                
        # Mutation ocurred
        if random.random() < mutProb:
            childResistance[drug] = not value
                    
        else:
            childResistance[drug] = value
            
    return childResistance
    


#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        
        #Instantiate and initiale Super Class
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        
        self.resistances = resistances

        self.mutProb = mutProb        


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.resistances[drug]
        
        except: KeyError("drug")


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        
        # If there is no resistance to any drug in list return False
        for drug in activeDrugs:
            
            if not self.resistances[drug]:
                
                raise NoChildException
        
        #Checked all drugs
        else:
            
             # Check if the virus particule will reproduce        
             probToReproduce = self.maxBirthProb * (1.0 - popDensity)
        
        # test if it will reproduce        
        if random.random() < probToReproduce:
        
            childResistance = buildChildResistance(self.resistances, \
                                                   self.mutProb)
            return ResistantVirus(self.maxBirthProb, self.clearProb, \
                                  childResistance, self.mutProb)
            
        else:
            raise NoChildException
            
            
            

            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.drugs:
            self.drugs.append(newDrug)
            


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        total = 0

        for virus in self.getViruses():
            
                        
            for drug in drugResist:
                
                if drug in virus.getResistances().keys():
                    if not virus.isResistantTo(drug):
                        break
                else: break
            
            else:
                total+= 1
            
#            #list of True == 1 or False == 0
#            testResist = [virus.isResistantTo(drug) for drug in drugResist \
#             if drug in virus.getResistances().keys()]
#            
#            # If all items of the list were True the sum will be equal to 
#            # len(drugResist)
#            if sum(testResist) == len(drugResist): #and len(drugResist)!=0:
#                total += 1
#            
        return total
            
            


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        
        # create a new list to accomodate the new population virus and
        # not mutate the current population while iterating over it
        virusesCopy = []
        
        for virus in self.getViruses():
            
            if not virus.doesClear():
                
                virusesCopy.append(virus)
        
        #update the viruses list
        self.viruses = virusesCopy
        
        popDensity = self.getTotalPop()/self.getMaxPop()
        
        newViruses = []
        
        for virus in self.getViruses():
            
            try:
                child = virus.reproduce(popDensity, self.drugs)
                
                newViruses.append(child)
            
            except:
                
                next
                
        #check if list is not empty
        if len(newViruses):
            self.viruses.extend(newViruses)
            
        return self.getTotalPop()

#Test of Treated Patient
        
#virus = ResistantVirus(1.0, 0.0, {}, 0.0)
#
#patient = TreatedPatient([virus], 100)
#
#for i in range(100):
#    patient.update()
#    
#print(patient.getTotalPop())

#virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
#virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
#patient = TreatedPatient([virus1, virus2, virus3], 100)
#
#print(patient.getResistPop(['drug1']))
#print(patient.getResistPop(['drug2']))
#print(patient.getResistPop(['drug1','drug2']))
#print(patient.getResistPop(['drug3']))
#print(patient.getResistPop(['drug1', 'drug3']))
#print(patient.getResistPop(['drug1','drug2', 'drug3']))    


def runTimeSteps2(patient, timeSteps, drugResist):
    
    """
    
    patient: An instance of the Patient class
    
    timeSteps: Number of iterations (An integer)
    
    drugResist; A list containing strings of drug names
    
    
    Call the method patient.update() for timeSteps times    
    and update the patient total virus population as well
    as the current population resistant to the drugs 
    listed in drugResist
    
    return a tuple of (Total virus population, number of resistant virus)
    
    """   
    

    population, resistant = [], []
    
    for i in range(timeSteps):              
        
        patient.update()
        
        population.append(patient.getTotalPop())
        
        resistant.append(patient.getResistPop(drugResist))
        
    return (population,resistant)

#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    timeSteps = 150
    
    virusPop = []
    
    virusPopResist = []
    
    
    for i in range(numTrials):
        
        #Create a list of viruses   
        infection = [ResistantVirus(maxBirthProb, clearProb, resistances, \
                                    mutProb) for i in range(numViruses)]
    
        #Instantiate one patient infected with numViruses
        patient = TreatedPatient(infection, maxPop = maxPop)
        
        #Run timeSteps updates without any drug        
        #listPop, listResist = runTimeSteps2(patient, timeSteps, ['guttagonol'])
        
        listPop, listResist = runTimeSteps2(patient, timeSteps, ['guttagonol'])
        
        virusPop.append(listPop)
        
        virusPopResist.append(listResist)
        
        #add drug
        patient.addPrescription('guttagonol')
        
        #Run additional timeSteps with drug 
        listPop, listResist = runTimeSteps2(patient, timeSteps, ['guttagonol'])
        
        # Extend the last appended list with the additional list now with
        # the drug added
        
        virusPop[-1].extend(listPop)
        
        virusPopResist[-1].extend(listResist)
        
        
        
        
    avgPop, avgResist = [],[]
    
    sumPop, sumResist = 0.0, 0.0
    
    for i in range(2 * timeSteps):
        
        #iterate both lists
        for v,r in zip(virusPop, virusPopResist):
            
            sumPop += v[i]; sumResist += r[i]
            
        avgPop.append(sumPop/numTrials)
        
        avgResist.append(sumResist/numTrials)
        
        sumPop, sumResist = 0.0, 0.0
     
    #print("Plotting: ", avgPop)
    
    #print("\nPlotting: ", avgResist)
    
    pylab.figure()
    
    pylab.plot(avgPop, label = "Total")
    
    pylab.plot(avgResist, label = "ResistantVirus")
   
    pylab.title("ResistantVirus Simulation")
    
    pylab.xlabel("Time Step")
    
    pylab.ylabel("# viruses")
             
    pylab.legend(loc = "best")   
    
    pylab.show()
        
        
#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, 100)       
        
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)    
   
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)

#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)

#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)

#random.seed(0)
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)

