# Optimization Algorithms

# Introduction 
In this paper I intend to research and compare Artificial bee colony and genetic algorithms. Also compare several different genetic algorithm operators and to optimize the Rosenbrock and Ackley fitness functions. 

# Background Research
## Introduction to ABCs 
Another algorithm for solving optimization problems is the artificial bee colony. The algorithm works similar to a bee colony as you would expect, it has 3 types of bees, employed bees, onlookers and scouts (Karaboga, Basturk,2007). Within this algorithm possible solutions are not represented as individuals with genes as is the case with genetic algorithms and a fitness. Food source represents possible solutions in an optimization problem and the nectar represents the fitness (Karaboga, Basturk,2007). Using this information, it is clear that the representation of the problem is similar in concept both genetic algorithms and bee algorithms, have a problem solution they represent in their respective ways then they have a way of representing the fitness of said problem solution.

## ABC Structure
Breaking down the steps, the first step of the process is the initialization phase. This is where a randomly distributed initial population is created (Karaboga, Basturk, 2007). 
The next phase is the employed bee phase, where in employed bee search for new solutions within the neighborhood of the food sources their memory, when they find one, they evaluate the fitness of the food source (Karaboga, Gorkemli, Ozturk, 2014). The next step once a new food source is produced and greedy selection has been applied between it and its parent, employed bee share the information about the food source with onlooker bees in the hive that are currently dancing in the dancing area (Karaboga, Gorkemli, Ozturk, 2014).

The next phase is the onlooker phase. In this phase food sources are probabilistically chosen by onlooker bees, based on the information that they received from the employed bees (Karaboga, Gorkemli, Ozturk, 2014). In the case of this article, (Karaboga, Gorkemli, Ozturk, 2014) it is stated that a fitness-based selection algorithm like roulette wheel selection can be employed. Fitness based selection is also used in genetic algorithms they are just used in different ways, to select individuals for crossover as opposed to, using selected found food source to apply greedy selection between it and a neighborhood food source after its fitness has been determined (Karaboga, Gorkemli, Ozturk, 2014).         
The next phase of the ABC algorithm is the scout phase. Any solutions that can’t be improved through a predetermined number of trials there employed bees become scouts and those solutions abandoned (Karaboga, Gorkemli, Ozturk, 2014). Scout will then start to find new solutions at random (Karaboga, Gorkemli, Ozturk, 2014).

## ABC parameters
Comparing parameter options for both Genetic algorithms, basic genetic algorithms can have multiple parameters, in the case of this research paper, including Generation, population, mutation rate and crossover rate compared with ABCs, in the case of this study “A comparative study of Artificial Bee Colony algorithm” the basic ABC used in this study employs only one control parameter, which is called limit (Karaboga, Akay, 2009). The limit described in the study is, when the limit is exceeded the food source will no longer be exploited and will be considered abandoned (Karaboga, Akay, 2009). However other basic parameters in the study are used such as, population number and maximum evaluation number (Karaboga, Akay, 2009). 

## Comparison of Genetic algorithms and ABCs
Both genetic algorithms and artificial bee colonies can be used for global optimization. Although both genetic algorithms and ABC seem to be different on the surface, they do share some similarities in regard to the search process, for example the employed bee phase is comparable to the selection stage in a genetic algorithm, as in the employed bee phase solutions are selected and their information saved based on their fitness. Another example it could be argued that the onlooker phase is similar to genetic algorithms mutation however it is guided and not random. 

# Experimentation 

My program’s structure is as follows, first I generate an initial population of individuals. Then test that populations initial fitness. Deep copying is used in all places where the population is being copied from one array to another. After initial fitness has beings calculated the selection process begins. After this step has been completed crossover then mutation is applied to the population. The final step is to calculate the minimum fitness of the generation and the mean fitness of the generation then the elitism function is called, and the best individual is selected and replaced with the worse individual for the next generation. 

Several parameters are included at the top of the program they are as follows, N, Pop, MUTRATE, MUTSTEP, GEN, MIN and MAX. N is equal to the number of chromosomes in each individual. Pop is in reference to the max number of populations in each Generation. Gen or generation is how many times the above GA algorithm will run I.E how many times, selection, crossover, and mutation will happen. MIN and MAX are in reference to the minimum and maximum values and given chromosome can be in an individual. MUTRATE or mutation rate is how often an individual solution will be mutated. When dealing with real numbers as opposed to 1 and 0s you can’t simply flip a 1 to a 0 and vice versa to mutate them. Therefore, MUTSTEP or mutation step is required to determine what will be taken away or added to an individual chromosome to mutate it.

## Optimising Rosenbrock and Ackley fitness functions

The algorithm used for the mutation sweep for both Rosenbrock and Ackley fitness functions and other such tests, includes, one point crossover, tournament selection and uniform mutation. This is the case unless specified otherwise.
A heat map is provided for the mutation sweep for both RosenBrock and Ackley. The greener the fitness value the lower it is.

## Rosenbrock

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture1.jpg)

The table above shows a collection of data produced by a mutation rate and mutstep sweep to find the best possible combination of mutation rate and mutstep values. Each fitness value is produced by a test set contains a set of 10 individual test where the same test with the same parameters is run 10 times, this is to account for the inconsistent results obtained when these tests are run due to the fact that mutation rate and population generation is random the results can vary quite a lot. 

The best fitness values for each run of the system, from all 10 tests for a set is added to one array and then averaged. This then gives one average fitness value for one pair of parameters for example 0.01 mutrate and 10 mutstep will give the average, 5.098354862184059

The other parameters are as follows, population: 100, generations: 500, and the min and max values for each individual chromosomes in an individual are min: -100 and max: 100. 

As can be seen from the mutation sweep for the Rosenbrock fitness function the best fitness is 5.098354862184059 Meaning a mutation rate of 0.02 and a mutstep of 10 is a good starting point to tune the mutation rate and step further. 

### 100 Pop, Mutstep 0.025 and 10 Mutstep
![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture2.jpg)

First testing 0.025 and 10 seemed like the most logical option to try first, as the best finesses are obtained between 0.01 and 0.03, this is done with 100 Population and over 500 generations. As can be seen from both the graph above and the table below, with the increase of mutrate the fitness increased compared to the last run there by meaning it is a good idea to try a much lower mutrate value.

Average: 6.675185664522118

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture3.jpg)

As can be seen from this graph it appears to show premature convergence, however zooming in to the end of the graph shows a something different.

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture4.jpg)

The graph shows however that this is not the case both the average and the best lines are running parallel to each other and separated not running on top of each other this indicates that the algorithm is still searching and has not converged on one solution.

### 100 Pop, Mutstep 0.015 and 10 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture5.jpg)

Decreasing the mutrate to 0.015 as the mutrate between 0.01 and 0.3 gave the best results we get a slight decrease in fitness. 

Average: 5.2300703115953135

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture6.jpg)

As can be seen from this graph compared to the last, both lines have gotten closer together rather than further apart meaning we are on the right track in terms of mutrate and mutstep combination, as the opposite would be true if it was a poor combination of the two.

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture7.jpg)

The end of the graph lines being separated and running parallel still indicate the search process is continuing.

### 100 Pop, Mutstep 0.015 and 5 Mutstep
![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture8.jpg)

Decreasing the mutstep further produces less dramatic changes to genes resulting in even better gene fitness as can be seen bellow.

Average: 2.395774327981293

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture9.jpg)

Again, the lines show convergence however this is not the case as can be seen bellow. 

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture10.jpg)

As can be seen again from this graph although it appears to be converging, further analysis concludes that it is not, by zooming in to the end of the graph the lines are running parallel indicating it’s still searching.

### 100 Pop, Mutstep 0.015 and 2 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture11.jpg)

After analysing both the graph and individual best fitness of each of the test runs the reduction of mutstep further produces to fewer changes to genes, resulting in less new genetic information being added to remove from genes resulting in a worse overall fitness as the GA is getting stuck in the local optimum rather than the global optimum.

Average: 1330.460778658239

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture12.jpg)

Both these graphs (Above and below) further clarify the fact decreasing the mutstep further has caused the fitness to increase and the search to be affected dramatically as the lines in the above graph are taking much longer to converge. The previous graph starts to converge around gen 25 whereas this run is starting to converge around 30 gens.

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture13.jpg)

To achieve the optimum, it may require reverting to the previous best mutrate and mutesteps and increasing the population count as decreasing or increasing Mutrate and mutstep at this point does not yield any better results.

### 200 pop, Mutstep 0.015 and 5 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture14.jpg)

After reverting to the best mutrate and mutstep of previous tests and increasing the population it is clear now the fitness is decreasing to much lower values than previously seen in testing. Although increasing the population does affect the efficiency of the genetic algorithm meaning it will take longer to give an output.

Average: 0.8083008653085122

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture15.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture16.jpg)

Further increase to the population is the best course of action after analysing results as this should lead to a further reduction in fitness.

### 300 Pop, Mutstep 0.015 and 5 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture17.jpg)

After further increases to the population count the resulting fitness values have again decreased further. However, this has yet again made the GA more in efficient and has produced even slower run times for the system.

Average: 0.36067163746478637

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture18.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture19.jpg)

## Ackley

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture20.jpg)

Using the same testing method as the RosenBrock function we can see that -22.24231355118912 is the smallest fitness in this mutation sweep. Therefore, the best starting point for experimentation is 0.02, 10.

### 100 Pop, Mutstep 0.025 and 10 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture21.jpg)

First testing a higher mutrate than the given best combination in the mutation sweep, yield as expected worse results but this is done to get the upper bounds for testing to see how high we can increase the mutrate before drastic changes occur as the best results were found between a mutrate of 0.01 and 0.03, it is clear from this test that we should not increase the mutrate any higher than 0.025. The lines in the graph spreading apart would indicate that there is too much mutation going on this will be reduced in the next test.

Average: -22.444862330907235

### 100 Pop, Mutstep 0.015 and 10 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture22.jpg)

After decreasing both mutrate and mutstep to 0.015 and 10 it is clear that the lines have come further together and starting from this point and working our way down in terms of mutstep is the best option, as in this case as a slightly lower mutrate and mutstep than the best combination in our mutation sweep has given better results.

Average Fitness: -22.477837934574517

### 100 Pop, Mutstep 0.015 and 5 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture23.jpg)

Further testing with a smaller mutstep shows the lines coming closer together rather than further apart, however they still are not quite parallel indicating that too much mutation is still proving to be an issue a further reduction is still required.

Average: -22.60814577345934

### 100 Pop, Mutstep 0.015 and 2 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture24.jpg)

After further reducing the mutstep the lines are running almost parallel indicating we are getting closer the right amount of mutation required to find the optimum solution. Further reduction of mutrate however would likely lead to less optimal results as genes would mutate rarely and with little change when they do mutate and further reduction of mutstep would cause similar issues and thereby increasing the average fitness. The most logical next step would be to increase the population count.

Average: -22.67215876935784

### 200 pop, Mutstep 0.015 and 1 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture25.jpg)

After increasing the population count the lines continued to coverage and are now running parallel indicating it is very close to the optimal solution, a further increase to the population should yield even better results.

Average: -22.702901846403094

### 300 pop, Mutstep 0.015 and 1 Mutstep

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture26.jpg)

Further increase to the population count has yielded better results but only slightly. We can there for conclude that this is indeed the optimum or extremely close.

Average: -22.7079392982269

# Alternative Operators

All parameters chosen for testing these operators were the best parameters found in prior testing for the Rosenbrock and Ackley function respectively.  Unless specified otherwise.

## Crossover – Multipoint
### Rosen Brock fitness:
![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture27.jpg)

Average: 0.25844865889669955

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture28.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture29.jpg)

### Ackley fitness:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture30.jpg)

Average: -22.704808181649533

### Analysis: 
Comparing multipoint crossover to single point crossover we can see that it provides slightly better results in both tests with Rosenbrock and Ackley. Due to the low gene count however, crossover does not have as greater of an effect as mutation would have for example on the search process. If we were to increase this, a greater change would be observed.

## Selection – Roulette wheel
### Rosen Brock fitness:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture31.jpg)

Average: 3.6298063060367944

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture32.jpg)


![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture33.jpg)

### Ackley Fitness:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture34.jpg)

Average: -3.1221355335396783

### Analysis: 
From analysing the results, it is clear that roulette wheel selection has performed worse in this case, this is because this type of selection performs worse with higher amounts of chromosomes within genes, furthermore if all solutions to be selected from have almost identical fitness values, then the chances of each solution being selected are very similar resulting in slightly worse solutions being selected more often. 

## Mutation – Gaussian Mutation
### Rosenbrock fitness:
![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture35.jpg)

Average: 4.532769917491803

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture36.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture37.jpg)

### Ackley Fitness:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture38.jpg)

Average: -22.718281828458807

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture39.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture40.jpg)

### Analysis: 
The mean and standard deviation are parameters that must be adjusted like MUTSTEP, so the best mutrate values that were obtained through testing are not going to provide the best results necessarily. In the instance of the first test with gaussian mutation on the rosenbrock function however, it appears that it has done significantly worse, it is likely the deviation and will need to be increased to see better results with that function as currently the values that will be in the gaussian mutation value will be too small to see any effect when mutating, alternatively the mutation rate could be increased to induce mutation more often. 

The Ackley function however is a different story and has been significantly improved with identical parameters to the parameters found in previous tests. This is likely because the Ackley function uses a smaller min and max values meaning less will have to be added or taken away from chromosomes to make a difference.

# Comparing ABC and GA performance
These are the results obtained by running Yarpiz (2015) artificial bee colony source code.
## Rosenbrock:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture41.jpg)

Rosenbrock function used in MATLAB code.

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture42.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture43.jpg)

## Ackley:

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture44.jpg)

Ackley function used in MATLAB code.


![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture45.jpg)

![alt text](https://github.com/Ben-EJ/BioCompResearchProject/blob/main/Report/Research%20Paper%20Figures/Picture46.jpg)

## Analysis:
Both the ABC algorithm selected, and the genetic algorithm used in testing are using the same population count and epoch amount and number of values in each solution, 300, 500 and 20 respectively. 

It is clear from the ABC Rosenbrock results that it performed significantly worse than the genetic algorithm and the opposite is true comparing the results of the Ackley functions. 

This implementation of the bee algorithm utilises roulette wheel selection. In the tested genetic algorithm, this was proven to perform poorly compared with other selection operators, the reason why Rosen brock function performance was so poor could be related with this issue. I.E a greater number of chromosomes in genes results in poorer performance because you are adding more and more dimensions.

# Conclusion:
In conclusion, from the tests run we can conclude a higher mutrate and mutstep does not provide better results because having too higher of either of these make to dramatic changes on genes resulting on a dramatically increased or decreased fitness. Furthermore, some genetic algorithm operators perform better in some circumstances and worse in others for example roulette wheel selection performing better with fewer chromosomes within genes. If given an opportunity to runs tests a second time, there are a few things I would do differently, including test a wider verity of GA operators and run similar comparisons between ABC and GA but test different ABC algorithms against the GA algorithm to see how they perform.

# References:
Karaboga, Akay, D.K, B.A. (2009) A comparative study of Artificial Bee Colony algorithm, Applied Mathematics and Computation [Online]. Volume 214, Pages 108-132 [Accessed 01 December 2021]

Karaboga, Basturk, D.K, B.B. (2007) A powerful and efficient algorithm for numerical function optimization: artificial bee colony (ABC) algorithm. Journal of Global Optimization[online]. Volume 39, Issue 3. [Accessed 29 November 2021]

Karaboga, Gorkemli, Ozturk, D.K, G.B, C.O. (2014) A comprehensive survey: artificial bee colony (ABC) algorithm and applications. Artificial Intelligence Review [online]. Volume 42, Issue 3. [Accessed 30 November 2021]

Yarpiz (2015) Artificial Bee Colony (ABC) in MATLAB (version 1.0.0.0) [Source Code]. Available from: https://uk.mathworks.com/matlabcentral/fileexchange/52966-artificial-bee-colony-abc-in-matlab [Accessed 4 December 2021]



