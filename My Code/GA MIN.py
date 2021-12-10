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

class GenerationData:
    def __init__(self, best, mean, bestSolutions, MUTRATE):
        self.best = best
        self.mean = mean
        self.bestSolutions = bestSolutions
        self.MUTRATE = MUTRATE
        
class TestParameters:
    def __init__(self,testNum, N, Pop, MUTRATE, MUTSTEP, GEN, MIN, MAX,SELECROSS,SELESELECT, SELEFIT):
        self.testNum = testNum
        self.N = N
        self.Pop = Pop
        self.MUTRATE = MUTRATE   
        self.MUTSTEP = MUTSTEP
        self.GEN = GEN
        self.MIN = MIN
        self.MAX = MAX
        self.SELECROSS = SELECROSS
        self.SELESELECT = SELESELECT
        self.SELEFIT = SELEFIT
        
def generatePopulationReals(Pop,N,MIN,MAX):
    population = []
    for i in range(0, Pop):
        gene = []
        for j in range(0, N):
            gene.append(random.uniform(MIN,MAX))
        population.append(Individual(gene, 0.0))
    return population

def fitnessFunc(population,Pop,N):
    for i in range(0, Pop):
        fitness = 0
        for x in range(0, N):
            fitness = fitness + population[i].gene[x]

        population[i].fitness = fitness
    return population

def fitnessFunc1(populationVar,Pop,N):
    for i in range(0, Pop):
        fitness = 10 * N
        for x in range(0, N):
            fitness = fitness + (populationVar[i].gene[x] ** 2) - ( 10 * math.cos((2 * 3.14) * populationVar[i].gene[x]) )
        populationVar[i].fitness = fitness
    return populationVar

def fitnessFunc2(population,Pop,N):
    for x in range(0, Pop):
        fitness = 0
        for i in range(0, N - 1):
            step1 = 0
            step2 = 0
            step1 = ((population[x].gene[i + 1] - (population[x].gene[i + 1] ** 2) ) ** 2)
            step2 = (1 - population[x].gene[i]) ** 2
            fitness = fitness + ((100 * step1) + step2)
        population[x].fitness = fitness
    return population

def fitnessFunc3(population,Pop,N):
    for z in range(0, Pop):
        fitness = 0
        step1 = 0
        step2 = 0
        for i in range(N):
            step1 += population[z].gene[i] ** 2
            step2 += math.cos(2 * math.pi * population[z].gene[i])
        fitness = -20 * math.exp(-0.2 * math.sqrt(step1 / N)) - math.exp(step2 / N)
        population[z].fitness = fitness
    return population

def selectFitnessFunc(num, population,Pop,N):
    if (num == 0):
        return fitnessFunc(population,Pop,N)
    elif (num == 1):
        return fitnessFunc1(population,Pop,N)
    elif (num == 2):
        return fitnessFunc2(population,Pop,N)
    else:
        return fitnessFunc3(population,Pop,N)

def selectionTour(population,Pop):
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

def popFitTotal(population,Pop):
    totalFit = 0
    for i in range(0, Pop):
        totalFit = totalFit + (1 / population[i].fitness)
    return totalFit

def rouletteWheel(population,Pop):
    offspring = []
    population_fitness_total = popFitTotal(population,Pop)
    for i in range(0, Pop): 
        selection_point = random.uniform(0, population_fitness_total)
        running_total  = 0 
        j = 0
        while ( running_total <= selection_point ):
            running_total += 1 / population[j].fitness
            j = j + 1 
        offspring.append(population[j-1])
    return offspring

def selection(population,Pop, SELESELECT):
    if(SELESELECT == 0):
        return selectionTour(population, Pop)
    elif(SELESELECT == 1):
        return rouletteWheel(population, Pop)

def crossoverOne(offspring,Pop,N): 
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

def twoPointCrossover(offspring,Pop,N):
    for i in range(0,Pop,2):
        offs1 = copy.deepcopy(offspring[i])
        offs2 = copy.deepcopy(offspring[i + 1])
        temp = copy.deepcopy(offspring[i])

        crossover1 = random.randint(1,N / 2)
        crossover2 = random.randint(crossover1, N)

        for j in range(crossover1, crossover2):
            offs1.gene[j] = copy.deepcopy(offs2.gene[j])
            offs2.gene[j] = copy.deepcopy(temp.gene[j])

        offspring[i] = copy.deepcopy(offs1)
        offspring[i + 1] = copy.deepcopy(offs2)
    return offspring



def crossover(offspring,Pop,N, SELECROSS):
    if (SELECROSS == 0):
        return crossoverOne(offspring,Pop,N)
    elif (SELECROSS == 1):
        return twoPointCrossover(offspring,Pop,N)



def mutationReals(offspring,Pop,N,MUTRATE,MUTSTEP,MAX,MIN):
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

def mutationGauss(offspring,Pop,N,MUTRATE,MUTSTEP,MAX,MIN): 
    for i in range(0, Pop):
        for j in range(0, N): 
            MUTPROB = random.uniform(0.0, 1.0)
            if (MUTPROB < MUTRATE):
                gaussian = random.gauss(0,MUTSTEP)
                offspring[i].gene[j] = offspring[i].gene[j] * gaussian
                if (offspring[i].gene[j] > MAX):
                    offspring[i].gene[j] = MAX     
    return offspring

def minFitness(population,Pop):
    minFitness = population[0].fitness
    for x in range(0, Pop):
        if (population[x].fitness < minFitness):
            minFitness = population[x].fitness
    return minFitness

def bestSolutionOfGen(population,Pop):
    minFitness = population[0].fitness
    bestSolutionNo = []
    for x in range(0, Pop):
        if (population[x].fitness < minFitness):
            minFitness = population[x].fitness
            bestSolutionNo = copy.deepcopy(population[x].gene)
    return bestSolutionNo        

def meanFitness(population,Pop):
    meanFitnessAdd = 0
    for x in range(0, Pop):
        meanFitnessAdd = meanFitnessAdd + population[x].fitness
    
    meanFitnessDiv = meanFitnessAdd / Pop
    return meanFitnessDiv

def minFitnessSave(population, offspring,Pop):
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

def printMainPop(population,Pop,N): 
    for i in range(0, Pop):
        print("Gene ")
        for x in range(0, N):
            print(population[i].gene[x])
        
        print("Fitness")
        print(population[i].fitness)

def printMin(minEachGen):
    for i in range(0, len(minEachGen)):
        print(minEachGen[i])   
def printMean(meanFitnessGen):
    for i in range(0, len(meanFitnessGen)):
        print(meanFitnessGen[i]) 

def GA(N,Pop,MUTRATE, MUTSTEP, GEN, MIN,MAX,SELECROSS,SELESelect,SELEFIT):
    population = []
    offspring = []

    minEachGen = []
    meanFitnessGen = []
    theBestSolutions = []
    population = generatePopulationReals(Pop,N,MIN,MAX)

    population = selectFitnessFunc(SELEFIT, population,Pop,N)
    
    for i in range(0,GEN):

        offspring = selection(population,Pop,SELESelect)

        offspring = crossover(offspring,Pop,N,SELECROSS)
        
        offspring = mutationReals(offspring,Pop,N,MUTRATE,MUTSTEP,MAX,MIN)

        offspring = selectFitnessFunc(SELEFIT, offspring,Pop,N)
        
        population = minFitnessSave(population,offspring,Pop)
        
        minEachGen.append(minFitness(population,Pop))
      
        meanFitnessGen.append(meanFitness(population,Pop))

    return GenerationData(minEachGen, meanFitnessGen,theBestSolutions,MUTRATE)

def plotGraph2D(testPara, genData):
    plt.figure(figsize=(20,10))
    plt.xlabel("Generation", fontsize=15)
    plt.ylabel("Min fitness",  fontsize=15)
    plt.title("GA Graph")

    for x in range(0, len(testPara)):
        ypoints = np.array(genData[x].best)
        zpoints = np.array(genData[x].mean)
        plt.plot(ypoints, label="Best" + " " + str(genData[x].MUTRATE))
        plt.plot(zpoints ,label="Mean" + " " + str(genData[x].MUTRATE))

    plt.legend(loc='best')
    plt.show()

def plotGraph2DAverage(genData,mean,MUTRATE,MUTSTEP):
    plt.figure(figsize=(20,10))
    plt.xlabel("Generations", fontsize=15)
    plt.ylabel("Average Fitness for each generation",  fontsize=15)
    plt.title("Genetic Algorithm results over 10 runs of the system")

    ypoints = np.array(genData)
    y2points = np.array(mean)
    plt.plot(ypoints, label="Best Fitness over 10 runs" + " " + str(MUTRATE) + " " + str(MUTSTEP))
    plt.plot(y2points, label="Average Fitness over 10 runs")

    plt.legend(loc='best')
    plt.show()
    
def lowestInEachTest(genData):
    for i in range(0,len(genData)):
        minFitness = genData[i].best[0]
        for x in range(0,len(genData[i].best)):
            if (genData[i].best[x] < minFitness):
                minFitness = genData[i].best[x]
        print(minFitness)

def lowestInEachTestAppend(genData):
    main = []
    for i in range(0,len(genData)):
        minFitness = genData[i].best[0]
        #bestSolution = []
        for x in range(0,len(genData[i].best)):
            if (genData[i].best[x] < minFitness):
                minFitness = genData[i].best[x]
                #bestSolution = copy.deepcopy(genData[i].bestSolutions[x])
        main.append(minFitness)
        #main.append(bestSolution)
    return main


"""
    

"""
"""
================================
SELECROSS:(Select Crossover)
One Point Crossover: 0 
two Point Crossover: 1
================================
SELESELECT: (Select Selection)
Tournement Selection: 0
Roulette Wheel Selection: 1
================================
SELEFIT: (Select Fitness)
Adding Up Fitness: 0
Rastrigin function: 1
Rosenbrock function: 2
Ackley function: 3
================================
"""
def averageOverTests(testNo,test):
    allgen = []
    meanFitnessAdd = 0
    
    for z in range(0, len(test)):# Takes final element in the best fitness array for a given run of the system
        allgen.append(test[z].best[len(test[z].best) - 1])# appends to array

    #print(allgen)
    for x in range(0, len(allgen)):#Finds average
        meanFitnessAdd = meanFitnessAdd + allgen[x]
    meanFitnessDiv = meanFitnessAdd / len(allgen)
    
    return meanFitnessDiv

def averageOverGen(test,GEN):
    aver = []
    for i in range(0,GEN):
        allgen = []
        meanFitnessAdd = 0
        for z in range(0, len(test)):
            allgen.append(test[z].best[i])

        for x in range(0, len(allgen)):#Finds average
            meanFitnessAdd = meanFitnessAdd + allgen[x]
        aver.append(meanFitnessAdd / len(allgen))
    return aver

def averageMeanOverGen(test,GEN):
    aver = []
    for i in range(0,GEN):
        allgen = []
        meanFitnessAdd = 0
        for z in range(0, len(test)):
            allgen.append(test[z].mean[i])

        for x in range(0, len(allgen)):#Finds average
            meanFitnessAdd = meanFitnessAdd + allgen[x]
        aver.append(meanFitnessAdd / len(allgen))
    return aver

def testAverage(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT):  
    
    genData = []
    testPara = []

    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))

    for i in range(0,len(testPara)):
        genData.append(GA(testPara[i].N,testPara[i].Pop,testPara[i].MUTRATE,testPara[i].MUTSTEP,testPara[i].GEN,testPara[i].MIN,testPara[i].MAX,testPara[i].SELECROSS, testPara[i].SELESELECT,testPara[i].SELEFIT))
    
    return averageOverTests(testNum,genData)
    
def testIndiv(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT):
    genData = []
    testPara = []

    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    testPara.append(TestParameters(testNum,N,Pop,MUTRATE,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    
    for i in range(0,len(testPara)):
        genData.append(GA(testPara[i].N,testPara[i].Pop,testPara[i].MUTRATE,testPara[i].MUTSTEP,testPara[i].GEN,testPara[i].MIN,testPara[i].MAX,testPara[i].SELECROSS, testPara[i].SELESELECT,testPara[i].SELEFIT))
    
    #plotGraph2D(testPara,genData)
    print(averageOverTests(testNum,genData))
    print(lowestInEachTestAppend(genData))
    plotGraph2DAverage(averageOverGen(genData,GEN),averageMeanOverGen(genData,GEN),MUTRATE,MUTSTEP)
    
    #print(genData[0].best)

   

def mainAverageTests():
    GEN = 500
    MUTSTEP = 60    
    SELECROSS = 0
    SELESELECT = 0
    SELEFIT = 2
    MIN = -100
    MAX = 100
    Pop = 50
    
    print(testAverage(1,20,Pop,0.01,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    print(testAverage(1,20,Pop,0.02,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    print(testAverage(1,20,Pop,0.03,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    print(testAverage(1,20,Pop,0.04,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))
    print(testAverage(1,20,Pop,0.05,MUTSTEP,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT))

def mainIndivTests():
    GEN = 500
    SELECROSS = 0
    SELESELECT = 0
    SELEFIT = 3
    MIN = -32  
    MAX = 32

    testIndiv(1,20,100,0.015,1,GEN,MIN,MAX,SELECROSS,SELESELECT,SELEFIT)

#mainAverageTests()
mainIndivTests()
