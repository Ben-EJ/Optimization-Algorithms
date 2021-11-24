import math
import random
import array
import matplotlib.pyplot as plt
import numpy as np
import copy

class Individual:
    def __init__(self, gene,fitness):
        self.gene = gene
        self.fitness = fitness

    def getGene(self):
        return self.gene
    def getFitness(self):
        return self.fitness

    def setGeneNo(self, geneNo, geneSet):
        self.gene[geneNo] = geneSet
    def setGene(self, geneSet):
        self.gene = geneSet
    def setFitness(self, fitnessSet):
        self.fitness = fitnessSet

N = 20
Pop = 50

MUTRATE = 0.04
MUTSTEP = 2

GEN = 250

MIN = -32
MAX = 32

SELEFIT = 3

def generatePopulationReals():
    population = []
    for i in range(0, Pop):
        gene = []
        for j in range(0, N):
            gene.append(random.uniform(MIN,MAX))
        population.append(Individual(gene, 0.0))
    return population

def fitnessFunc(populationVar):
    for i in range(0, Pop):
        fitness = 0
        for x in range(0, N):
            fitness = fitness + population[i].getGene()[x]

        populationVar[i].setFitness(fitness)
    return populationVar

def fitnessFunc1(populationVar):
    for i in range(0, Pop):
        fitness = 10 * N
        for x in range(0, N):
            
            fitness = fitness + (populationVar[i].getGene()[x] ** 2) - ( 10 * math.cos((2 * 3.14) * populationVar[i].getGene()[x]) )

        populationVar[i].setFitness(fitness)
    return populationVar

def fitnessFunc2(population):
    for x in range(0, Pop):
        fitness = 0
        for i in range(0, N - 1):
            step1 = 0
            step2 = 0
            step1 = ((population[x].gene[i + 1] - (population[x].gene[i] ** 2)) ** 2)
            step2 = (1 - population[x].gene[i]) ** 2
            fitness = fitness + (100 * (step1 + step2))
        population[x].setFitness(fitness)
    return population

def fitnessFunc3(population):
    for x in range(0, Pop):
        fitness = 0
        step1 = 0
        step2 = 0
        for i in range(0,N):
            step1 = step1 + population[x].gene[i] ** 2
            step2 = step2 + math.cos(2 * 3.14 * population[x].gene[i])
        fitness = fitness + (-20 * ( math.exp(-0.2 * math.sqrt(step1)) - math.exp(step2) ) )
        population[x].setFitness(fitness)
    return population

def selectFitnessFunc(num, population):
    if (num == 0):
        return fitnessFunc(population)
    elif (num == 1):
        return fitnessFunc1(population)
    elif (num == 2):
        return fitnessFunc2(population)
    else:
        return fitnessFunc3(population)


def populationFitnessTotal():
    totalFit = 0
    for i in range(0,Pop):
        totalFit = totalFit + population[i].getFitness()
    return totalFit


def selectionMin(population):
    parent1 = 0
    parent2 = 0
    offspring = []  
    for i in range(0,Pop):
        parent1 = random.randint(0, Pop - 1)
        parent2 = random.randint(0, Pop - 1)
        if (population[parent1].getFitness() < population[parent2].getFitness()):
            offspring.append(population[parent1])
        else: 
            offspring.append(population[parent2])
    return offspring

def crossoverOne(offspring): 
    for i in range( 0, Pop, 2 ): 
        toff1 = copy.deepcopy(offspring[i]) 
        toff2 = copy.deepcopy(offspring[i+1]) 
        temp = copy.deepcopy(offspring[i]) 
        crosspoint = random.randint(1,N) 
        for j in range (crosspoint, N): 
            toff1.gene[j] = toff2.gene[j] 
            toff2.gene[j] = temp.gene[j] 
        offspring[i] = copy.deepcopy(toff1) 
        offspring[i+1] = copy.deepcopy(toff2)
    return offspring    

def uniformCrossover(offspring):
    for i in range(0,len(offspring), 2):
        temp = copy.deepcopy(offspring[i].getGene())
        temp2 = copy.deepcopy(offspring[i + 1].getGene())
        for j in range(0, N):
            crossover = random.randint(0, 1)
            #print(crossover)
            if(crossover == 1):
                temp3 = copy.deepcopy(temp[j])
                temp[j] = copy.deepcopy(temp2[j])
                temp2[j] = copy.deepcopy(temp3)
        offspring[i].gene = copy.deepcopy(temp) 
        offspring[i+1].gene = copy.deepcopy(temp2)
    return offspring


def mutationReals(offspring):
    
    for i in range(0, Pop):
        for j in range(0, N): 
            MUTPROB = random.uniform(0.0, 1.0)
            if (MUTPROB < MUTRATE):
                alter = random.uniform(0, MUTSTEP)
                coinFlip = random.randint(0,2)
                if (coinFlip == 1):
                    aGene1 = offspring[i].getGene()[j] + alter
                    offspring[i].setGeneNo(j, aGene1)
                    if (offspring[i].getGene()[j] > MAX):
                         offspring[i].setGeneNo(j,MAX)     
                else:
                    aGene2 = offspring[i].getGene()[j] - alter
                    offspring[i].setGeneNo(j, aGene2)
                    if (offspring[i].getGene()[j] < MIN):
                         offspring[i].setGeneNo(j,MIN)        
    return offspring

def minFitness(population):
    minFitness = population[0].getFitness()
    for x in range(1, Pop):
        if (population[x].getFitness() < minFitness):
            minFitness = population[x].getFitness()
    return minFitness

def meanFitness(population):
    meanFitnessAdd = 0
    for x in range(0, Pop):
        meanFitnessAdd = meanFitnessAdd + population[x].getFitness()
    
    meanFitnessDiv = meanFitnessAdd / Pop
    return meanFitnessDiv

def minFitnessSave(population):
    minFitness = population[0].getFitness()
    bestIndervidual = 0
    for x in range(1, Pop):
        if (population[x].getFitness() < minFitness):
            minFitness = population[x].getFitness()
            bestIndervidual = x

    worseFitness = population[0].getFitness()
    worseIndervidual = 0
    for x in range(1, Pop):
        if (population[x].getFitness() > worseFitness):
            worseFitness = population[x].getFitness()
            worseIndervidual = x

    population[worseIndervidual] = copy.deepcopy(population[bestIndervidual])
    return population


minEachGen = []
meanFitnessGen = []

def printMainPop(population): 
    for i in range(0, Pop):
        print("Gene ")
        for x in range(0, N):
            print(population[i].getGene()[x])
        
        print("Fitness")
        print(population[i].getFitness())

def printMin():
    for i in range(0, len(minEachGen)):
        print(minEachGen[i])   

def main():
    global population
    global offspring
    population = []
    offspring = []

    population = generatePopulationReals()

    population = selectFitnessFunc(SELEFIT, population)
    
    for i in range(0,GEN):

        offspring = selectionMin(population)

        offspring = crossoverOne(offspring)
        
        offspring = mutationReals(offspring)

        offspring = selectFitnessFunc(SELEFIT, offspring)
        
        population = copy.deepcopy(selectionMin(offspring))

        minEachGen.append(minFitness(population))
        meanFitnessGen.append(meanFitness(population))
        
main()
#printMin()    

plt.figure(figsize=(20,10))

plt.xlabel("Generation", fontsize=15)
plt.ylabel("Min fitness",  fontsize=15)
plt.title("GA Graph")
ypoints = np.array(minEachGen)
zpoints = np.array(meanFitnessGen)
plt.figtext(0.5, 0.01, "N: " + str(N) + " / " + "POP: " + str(Pop) + " / " + "MUTRATE: " + str(MUTRATE) + " / " + "MUTSTEP: " + str(MUTSTEP) + " / " + "GEN: " + str(GEN) + " ",horizontalalignment = "center",  fontsize=20, bbox={"facecolor":"white", "alpha":0.5, "pad":10, })

plt.plot(ypoints, label="Best")
plt.plot(zpoints ,label="Mean", color="red")
plt.legend(loc='best')
plt.show()