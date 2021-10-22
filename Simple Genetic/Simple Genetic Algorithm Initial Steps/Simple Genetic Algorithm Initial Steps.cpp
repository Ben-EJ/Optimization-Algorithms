// Simple Genetic Algorithm Initial Steps.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
const int N = 10;
const int P = 16;
const float MUTRATE = 0.1;
typedef struct {
    int gene[N];
    int fitness;
} individual;



individual population[P];
individual offspring[P];

void fitnessFunc(individual& ind) {
    int fitness = 0;
    for (int i = 0; i < N; i++) {
        if (ind.gene[i] == 1)
            fitness += 1;
    }
    ind.fitness = fitness;
}

void generatePopulation() {
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            
            population[i].gene[j] = rand() % 2;
        }
        population[i].fitness = 0;
    }
}
void printMainPop() {
    for (int i = 0; i < P; i++) {
        cout << "Gene\n";
        for (int x = 0; x < 10; x++) {
            cout << population[i].gene[x];
        }  
        cout << "\n";
        cout << "Fitness\n";
        cout << population[i].fitness << "\n";
        cout << "\n";
    }
}
void printOffspringPop() {
    for (int i = 0; i < P; i++) {
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
    for (int i = 0; i < P; i++) {
        fitnessFunc(population[i]);
    }
}
void selection() {
    int parent1 = 0;
    int parent2 = 0;
    for (int i = 0; i < P; i++) {
        parent1 =  rand() % P;
        parent2 =  rand() % P;
        if (population[parent1].fitness > population[parent2].fitness) {
            offspring[i] = population[parent1];
        }    
        else{
            offspring[i] = population[parent2];
        }   
    }
    
}

void crossover() {
    individual temp;
    for (int i = 0; i < P; i += 2) {
        int crosspoint = 0;
        for (int j = 0; j < N; j++)
            temp.gene[j] = offspring[i].gene[j];
        crosspoint = rand() % P;
        for (int j = crosspoint; j < N; j++) {
            offspring[i].gene[j] = offspring[i + 1].gene[j];
            offspring[i + 1].gene[j] = temp.gene[j];
        }
    }
}

void mutation() {
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            float MUTPROB = (float(rand()) / float((RAND_MAX)) * 1);
            if (MUTPROB < MUTRATE) {
                if (offspring[i].gene[j] == 1) offspring[i].gene[j] = 0;
                else offspring[i].gene[j] = 1;
            }
        }
    }
    
    
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            population[i].gene[j] = offspring[i].gene[j];
        }
        population[i].fitness = offspring[i].fitness;
    }
    
}
int totalFitness(individual pop[P]) {
    int totalFitnessNum = 0;
    for (int i = 0; i < P; i++) {
        totalFitnessNum = totalFitnessNum + pop[i].fitness;
    }
    return totalFitnessNum;
}
void main()
{
    srand(time(NULL));
    generatePopulation();
    testFitness();
    cout << "Total Fitness inital: " << totalFitness(population);
   
    for (int i = 0; i < 50; i++) {
        selection();
        crossover();
        mutation();
        testFitness();
    }
    cout << "\n";
    cout << "Total Fitness after: " << totalFitness(population); 
}

