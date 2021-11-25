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



'''
N = 20
Pop = 50
MUTRATE = 0.04
MUTSTEP = 20
GEN = 80
MIN = -32
MAX = 32
SELEFIT = 3
'''

N = 20
Pop = 50

MUTRATE = 0.04
MUTSTEP = 20

GEN = 1000

MIN = -100
MAX = 100

SELEFIT = 2

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
            fitness = fitness + population[i].gene[x]

        populationVar[i].fitness = fitness
    return populationVar

def fitnessFunc1(populationVar):
    for i in range(0, Pop):
        fitness = 10 * N
        for x in range(0, N):
            fitness = fitness + (populationVar[i].gene[x] ** 2) - ( 10 * math.cos((2 * 3.14) * populationVar[i].gene[x]) )
        populationVar[i].fitness = fitness
    return populationVar

def fitnessFunc2(population):
    for x in range(0, Pop):
        fitness = 0
        for i in range(0, N - 1):
            step1 = 0
            step2 = 0
            step1 = ((population[x].gene[i + 1] - (population[x].gene[i] * population[x].gene[i])) * (population[x].gene[i + 1] - (population[x].gene[i] * population[x].gene[i])))
            step2 = (1 - population[x].gene[i]) * (1 - population[x].gene[i])
            fitness = fitness + (100 * (step1 + step2))

        population[x].fitness = fitness
    return population

def fitnessFunc3(population):
    for x in range(0, Pop):
        fitness = 0
        step1 = 0
        step2 = 0
        for i in range(0,N):
            step1 = step1 + (population[x].gene[i] ** 2) 
            step2 = step2 + math.cos(2 * 3.14 * population[x].gene[i]) 
        fitness = fitness + (-20 * ( math.exp(-0.2 * math.sqrt(step1 / N)) - math.exp(step2 / N) ) )
        population[x].fitness = fitness
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
        totalFit = totalFit + population[i].fitness
    return totalFit


def selectionMin(population):
    parent1 = 0
    parent2 = 0
    offspring = []  
    for i in range(0,Pop):
        parent1 = random.randint(0, Pop - 1)
        parent2 = random.randint(0, Pop - 1)
        if (population[parent1].fitness < population[parent2].fitness):
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
                alter = random.uniform(0.0, MUTSTEP)
                coinFlip = random.randint(0,1)
                if (coinFlip == 1):
                    offspring[i].gene[j] = offspring[i].gene[j] + alter
                    if (offspring[i].gene[j] > MAX):
                         offspring[i].gene[j] = MAX    
                else:
                    offspring[i].gene[j] = offspring[i].gene[j] - alter
                    if (offspring[i].gene[j] < MIN):
                         offspring[i].gene[j] = MIN        
    return offspring

def minFitness(population):
    minFitness = population[0].fitness
    for x in range(0, Pop):
        if (population[x].fitness < minFitness):
            minFitness = population[x].fitness
    return minFitness

def meanFitness(population):
    meanFitnessAdd = 0
    for x in range(0, Pop):
        meanFitnessAdd = meanFitnessAdd + population[x].fitness
    
    meanFitnessDiv = meanFitnessAdd / Pop
    return meanFitnessDiv

def minFitnessSave(population, offspring):
    minFitness = population[0].fitness
    bestIndervidual = 0
    for x in range(1, Pop):
        if (population[x].fitness < minFitness):
            minFitness = population[x].fitness
            bestIndervidual = x

    worseFitness = population[0].fitness
    worseIndervidual = 0
    
    for x in range(1, Pop):
        if (offspring[x].fitness > worseFitness):
            worseFitness = offspring[x].fitness
            worseIndervidual = x

    offspring[worseIndervidual] = copy.deepcopy(population[bestIndervidual])
    return offspring


minEachGen = []
meanFitnessGen = []

def printMainPop(population): 
    for i in range(0, Pop):
        print("Gene ")
        for x in range(0, N):
            print(population[i].gene[x])
        
        print("Fitness")
        print(population[i].fitness)

def printMin():
    for i in range(0, len(minEachGen)):
        print(minEachGen[i])   
def printMean():
    for i in range(0, len(meanFitnessGen)):
        print(meanFitnessGen[i]) 
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

        minEachGen.append(minFitness(population))
        meanFitnessGen.append(meanFitness(population))

        population = minFitnessSave(population,offspring)

        
main()   
printMin()
print(" ")
#printMean()
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