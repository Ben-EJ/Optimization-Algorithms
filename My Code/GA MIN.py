import math
import random
import array
import matplotlib.pyplot as plt
import numpy as np
import copy
N = 20
Pop = 100

MUTRATE = 0.04
MUTSTEP = 2.55

GEN = 350

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
        
MIN = -100
MAX = 100

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
        fitness = 10 * N
        for x in range(0, N):
            #fitness = fitness + population[i].getGene()[x]
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
def minFitnessSave():
    minFitness = population[0].getFitness()
    bestIndervidual = Individual([],0.0)
    for x in range(1, Pop):
        if (population[x].getFitness() < minFitness):
            minFitness = population[x].getFitness()
            bestIndervidual = population[x]
    return bestIndervidual

def meanFitness(population):
    meanFitnessAdd = 0
    for x in range(0, Pop):
        meanFitnessAdd = meanFitnessAdd + population[x].getFitness()
    
    meanFitnessDiv = meanFitnessAdd / Pop
    return meanFitnessDiv


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

    populationFit = fitnessFunc2(population)
    
    population = copy.deepcopy(populationFit)

    for i in range(0,GEN):

        offspring = selectionMin(population)

        offspringDone1 = crossoverOne(offspring)
        
        offspring = copy.deepcopy(offspringDone1)
        
        offspringDone2 = mutationReals(offspring)
        
        offspring = copy.deepcopy(offspringDone2)
        
        
        population = copy.deepcopy(offspring)

        populationFit = fitnessFunc2(population)
        population = copy.deepcopy(populationFit)
        
        minEachGen.append(minFitness(population))
        meanFitnessGen.append(meanFitness(population))
        
    
main()
printMin()    

plt.figure(figsize=(20,10))

plt.xlabel("Generation", fontsize=15)
plt.ylabel("Min fitness",  fontsize=15)

ypoints = np.array(minEachGen)
zpoints = np.array(meanFitnessGen)

plt.plot(ypoints)
plt.plot(zpoints ,color="red")
plt.show()