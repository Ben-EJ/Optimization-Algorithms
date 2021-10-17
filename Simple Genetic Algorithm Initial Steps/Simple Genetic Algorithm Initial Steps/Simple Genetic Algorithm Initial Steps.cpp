// Simple Genetic Algorithm Initial Steps.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
const int N = 10;
const int P = 50;

typedef struct {
    int gene[N];
    int fitness;
} individual;



individual population[P];

void fitnessFunc(individual ind) {
    int fitness = 0;
    for (int i = 0; i < N; i++) {
        if (ind.gene[i] == 1)
            fitness += 1;
    }
}

void generatePopulation() {
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            population[i].gene[j] = rand() % 2;
        }
        population[i].fitness = 0;
    }
}
void printPop() {
    for (int i = 0; i < 50; i++) {
        for (int x = 0; x < 10; x++) {
            cout << population[i].gene[x];
        }  
        cout << population[i].fitness << "\n";
        cout << "\n";
    }
}
void main()
{
    generatePopulation();

    //printPop();
}


/*


    for (i = 0; i < P; i++) {
        parent1 = (rand() % P);
        parent2 = (rand() % P);
        if (population[parent1].fitness > population[parent2].fitness)
            offspring[i] = population[parent1];
        else
            offspring[i] = population[parent2]
    }



*/