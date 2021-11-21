#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>


using namespace std;
const int N = 20;
const int Pop = 50;

const float MUTRATE = 0.04;
const float MUTSTEP = 1.5;

const int GEN = 1000;

typedef struct {
    float gene[N];
    float fitness;
} individual;

individual population[Pop];
individual offspring[Pop];

const float MIN = -100; // Use these everywhere 
const float MAX = 100;


void fitnessFunc(individual& ind) {//New fitness function at the bottom of worksheet 3
    float fitness = 10 * N;
    for (int i = 0; i < N; i++) {
        //fitness = fitness + ind.gene[i];
        fitness = fitness + (ind.gene[i] * ind.gene[i]) - (10 * cos((2 * 3.14) * ind.gene[i]));
        
    }
    ind.fitness = fitness;
    
}

void fitnessFunc2(individual& ind) {
    float fitness = 0;
    for (int i = 0; i < N - 1; i++) {
        int step1 = 0;
        int step2 = 0;
        step1 = pow(ind.gene[i + 1] - pow(ind.gene[i], 2), 2);
        step2 = pow(1 - ind.gene[i], 2);
        fitness = fitness + (100 * (step1 + step2));

        //fitness = fitness +  (100 * (ind.gene[i + 1] - pow(ind.gene[i], 2))    +    pow(1 - ind.gene[i], 2) );
    }
    ind.fitness = fitness;
}

void testFitness() {
    for (int i = 0; i < Pop; i++) {
        fitnessFunc(population[i]);
        //fitnessFunc2(population[i]);
    }
}

void generatePopulationReals() {
    for (int i = 0; i < Pop; i++) {
        for (int j = 0; j < N; j++) {
            
            population[i].gene[j] = ((float(rand()) / float(RAND_MAX)) * (MAX - MIN)) + MIN; 
            
        }
        population[i].fitness = 0.0;
    }
}

int populationFitnessTotal() {
    int totalFit = 0;
    for (int i = 0; i < Pop; i++) {
        totalFit = totalFit + population[i].fitness;
    }
    return totalFit;
}

void selectionMin() {
    int parent1 = 0;
    int parent2 = 0;
    for (int i = 0; i < Pop; i++) {
        parent1 = rand() % Pop;
        parent2 = rand() % Pop;
        if (population[parent1].fitness < population[parent2].fitness) {// Turn this around for minimum
            offspring[i] = population[parent1];
        }
        else {
            offspring[i] = population[parent2];
        }
    }

}

void selectionRoulette() {
    int population_fitness_total = populationFitnessTotal();
    
    for (int i = 0; i < Pop; i++) {
        int selection_point = rand() % population_fitness_total;
        int running_total = 0;

        int j = 0;
        while (running_total <= selection_point) {
            running_total += population[j].fitness;
            j++;
        }
        offspring[i] = population[j - 1];
    }
}
void crossover() {
    individual temp;
    for (int i = 0; i < Pop; i += 2) {
        int crosspoint = 0;
        for (int j = 0; j < N; j++)
            temp.gene[j] = offspring[i].gene[j];
        crosspoint = rand() % Pop;
        for (int j = crosspoint; j < N; j++) {
            offspring[i].gene[j] = offspring[i + 1].gene[j];
            offspring[i + 1].gene[j] = temp.gene[j];
        }
    }
}

void mutationReals() {// Worksheet 3 mutation
    for (int i = 0; i < Pop; i++) {
        for (int j = 0; j < N; j++) {
            float MUTPROB = (float(rand()) / float((RAND_MAX)) * 1);
            if (MUTPROB < MUTRATE) {
                float alter = (float(rand()) / float((RAND_MAX)) * MUTSTEP);
                int coinFlip = rand() % 2;
                if (coinFlip == 1) {
                    offspring[i].gene[j] = offspring[i].gene[j] + alter;
                    if (offspring[i].gene[j] > MAX) offspring[i].gene[j] = MAX;
                }
                else {
                    offspring[i].gene[j] = offspring[i].gene[j] - alter;
                    if (offspring[i].gene[j] < MIN) offspring[i].gene[j] = MIN;
                }
            }
        }
    }

    for (int i = 0; i < Pop; i++) {
        for (int j = 0; j < N; j++) {
            population[i].gene[j] = offspring[i].gene[j];
        }
        population[i].fitness = offspring[i].fitness;
    }
}

int minFitness() {// Finding the worst for minimum, Switch arrow around
    float minFitness = population[0].fitness;

    for (int x = 1; x < Pop; x++) {
        if (population[x].fitness < minFitness) {
            minFitness = population[x].fitness;
        }
    }
    return minFitness;
}

int meanFitness() {
    float meanFitnessAdd = 0;
    float meanFitnessDiv = 0;
    for (int x = 0; x < Pop; x++) {
        meanFitnessAdd = meanFitnessAdd + population[x].fitness;
    }
    meanFitnessDiv = meanFitnessAdd / Pop;
    return meanFitnessDiv;
}

float minEachGen[GEN];
float meanFitnessGen[GEN]; // Mean fitness for each generation

void exportDataBest() {
    std::ofstream myfile;
    myfile.open("DataMin.csv");

    myfile << N << ",";
    myfile << Pop << ",";
    myfile << MUTRATE << ",";
    myfile << MUTSTEP << ",";
    myfile << GEN << ",";
    for (int i = 0; i < GEN; i++) {
        myfile << minEachGen[i] << ",";
    }
    
    myfile.close();
}
void exportDataMean() {
    std::ofstream myfile;
    myfile.open("DataMinMean.csv");
    for (int i = 0; i < GEN; i++) {
        myfile << meanFitnessGen[i] << ",";
    }

    myfile.close();
}

void printMainPop() {
    for (int i = 0; i < Pop; i++) {
        cout << "Gene\n";
        for (int x = 0; x < 10; x++) {
            cout << population[i].gene[x] << " , ";
        }
        cout << "\n";
        cout << "Fitness\n";
        cout << population[i].fitness << "\n";
        cout << "\n";
    }
}

void main()
{
    srand(time(NULL));
    generatePopulationReals();
    testFitness();
    printMainPop();
    for (int i = 0; i < GEN; i++) {
        selectionMin();
        //selectionRoulette();
        crossover();
        mutationReals();
        testFitness();
        minEachGen[i] = minFitness();
        meanFitnessGen[i] = meanFitness();
    }
    cout << "\n";  
    exportDataBest();
    exportDataMean();
}


// In selection take the lowest of each gen turn arrow around
// 
// 