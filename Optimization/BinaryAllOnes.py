import random

def fitness(chromosome):
    health = 0
    for gene in chromosome:
        health += gene
    return health

def sortPopulation(population):
    healthList = []
    for chromosome in population:
        healthList.append(fitness(chromosome))
    healthList, population = zip(*sorted(zip(healthList, population), reverse = True))
    return healthList, population

def intialPop(tot_chromosomes, genes_per_chromosome):
    population = []
    for i in range(tot_chromosomes):
        chromosome = []
        for j in range(genes_per_chromosome):
            chromosome.append(random.randint(0,1))
        population.append(chromosome)
    return population

def crossover(population, healthList):
    population = list(population)
    healthList = list(healthList)
    offspring1 = population[0]
    offspring2 = population[1]
    len_chromo = len(offspring1)

    numberCrossOver = random.randint(1,len_chromo>>1)
    temp = [0 for i in range(len_chromo)]

    for i in range(numberCrossOver):
        index = random.randint(0, len(offspring1)-1)
        while(temp[index] != 0):
            index = random.randint(0, len(offspring1)-1)
        temp[index] = 1
        offspring1[index], offspring2[index] = offspring2[index], offspring1[index]

    fitOff1 = fitness(offspring1)
    fitOff2 = fitness(offspring2)

    pop_size = len(healthList)
    for i in range(pop_size):
        note_index_reverse = -1
        rev_ind  = pop_size - i - 1
        if fitOff1 > healthList[rev_ind]:
            population[rev_ind] = offspring1[:]
            healthList[rev_ind] = fitOff1
            note_index_rev = len_chromo - i - 1
            break

    for i in range(pop_size):
        rev_ind = pop_size - i - 1
        if fitOff2 > healthList[rev_ind] and rev_ind != note_index_rev:
            population[rev_ind] = offspring2
            healthList[rev_ind] = fitOff2
            break
    return population

def mutation(population):
        pop_ind = random.randint(0,len(population)-1)
        num_bits = random.randint(1,len(population[pop_ind])>>1)

        temp = [0 for i in range(len(population[pop_ind]))]

        for i in range(num_bits):
            index = random.randint(0,len(population[i])-1)
            while(temp[index] != 0):
                index = random.randint(0, len(population[i])-1)
            temp[index] = 1
            if population[i][index]:
                population[i][index] = 0
            else:
                population[i][index] = 1
        return population
def main():
    pop_size = 10
    genes = 5
    population = intialPop(pop_size, genes)
    generations = 0
    healthList, population = sortPopulation(population)
    print("Generations {}  Fittest {}".format(generations, healthList[0]))
    while(healthList[0] != genes):
        healthList, population = sortPopulation(population)
        print("Generations {}  Fittest {}".format(generations, healthList[0]))
        population = crossover(population, healthList)
        if random.randint(4,1123123)%10 == 0:
            population = mutation(population)
        generations = generations + 1

if __name__ == '__main__':
    main()
