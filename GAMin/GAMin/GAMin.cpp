#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <python.h>

using namespace std;
const int N = 10;
const int Pop = 50;
const float MUTRATE = 0.1;
const float MUTSTEP = 0.1;
const float GEN = 50;


typedef struct {
    float gene[N];
    float fitness;
} individual;

individual population[Pop];
individual offspring[Pop];

const float MIN = -5.12; // Use these everywhere 
const float MAX = 5.12;

void fitnessFunc(individual& ind) {//New fitness function at the bottom of worksheet 3
    float fitness = 10 * N;
    for (int i = 0; i < N; i++) {
        //fitness = fitness + ind.gene[i];
        fitness = fitness + (ind.gene[i] * ind.gene[i]) - (10 * cos((2 * 3.14) * ind.gene[i]));
    }
    ind.fitness = fitness;
    
}

void generatePopulationReals() {
    for (int i = 0; i < Pop; i++) {
        for (int j = 0; j < N; j++) {
            
            population[i].gene[j] = ((float(rand()) / float(RAND_MAX)) * (MAX - MIN)) + MIN;
            
        }
        population[i].fitness = 0.0;
    }
}
void printMainPop() {
    for (int i = 0; i < Pop; i++) {
        cout << "Gene\n";
        for (int x = 0; x < 10; x++) {
            cout << population[i].gene[x] << " ";
        }
        cout << "\n";
        cout << "Fitness\n";
        cout << population[i].fitness << "\n";
        cout << "\n";
    }
}
void printOffspringPop() {
    for (int i = 0; i < Pop; i++) {
        cout << "Gene\n";
        for (int x = 0; x < 10; x++) {
            cout << offspring[i].gene[x];
        }
        cout << "\n";
        cout << "Fitness\n";
        cout << offspring[i].fitness << "\n";
        cout << "\n";
    }
}
void testFitness() {
    for (int i = 0; i < Pop; i++) {
        fitnessFunc(population[i]);
    }
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
                if (offspring[i].gene[j] + alter < 5.12) offspring[i].gene[j] = offspring[i].gene[j] + alter;
                else offspring[i].gene[j] = offspring[i].gene[j] - alter;
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
    for (int x = 1; x < Pop; x++) {
        meanFitnessAdd = meanFitnessAdd + population[x].fitness;
    }
    meanFitnessDiv = meanFitnessAdd / Pop;
    return meanFitnessDiv;
}

float minEachGen[Pop];
float meanFitnessGen[Pop]; // Mean fitness for each generation

void pythonOpenGraph() {
    std::ofstream myfile;
    myfile.open("DataMin.csv");
    for (int i = 0; i < 50; i++) {
        myfile << minEachGen[i] << ",";
    }
    
    myfile.close();
}
void main()
{
    srand(time(NULL));
    generatePopulationReals();
    testFitness();
    //cout << "Total Fitness inital: " << totalFitness(population);
    for (int i = 0; i < GEN; i++) {
        selectionMin();
        crossover();
        mutationReals();
        testFitness();
        minEachGen[i] = minFitness();
        meanFitnessGen[i] = meanFitness();
    }
    cout << "\n";
    
    /*for (int i = 0; i < 50; i++) {
        cout << minEachGen[i] << "\n";
    }*/
    printMainPop();
    pythonOpenGraph();
   
}


// In selection take the lowest of each gen turn arrow around
// 
// 