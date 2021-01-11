import itertools
from random import randint

pointsOfSplitting = [2, 6, 9]
sizeOfRuicksack = 16
# Check information about mutation, cycles
# and about choosing pattern
# Array of items [price, weight]
items = [[5, 2],
         [6, 4],
         [8, 5],
         [6, 4],
         [4, 2],
         [1, 1],
         [3, 1],
         [4, 2],
         [5, 4],
         [2, 1]]

population = [[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
              [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]]
# setup the algorithm
maxAnimals = len(population)
if pointsOfSplitting[-1] != len(population[0]):
    pointsOfSplitting.append(len(population[0]))

def print_population():
    print('Population:')
    for animal in zip(population, range(len(population))):
        print('S{}='.format(animal[1] + 1), end='')
        print_animal(animal[0])


def print_animal(animal):
    price, weight = count_solution_price_and_weight(animal)
    print('{}=price -> {}, weight -> {}'.format(animal, price, weight))


def count_solution_price_and_weight(animal):
    total_price = 0
    total_weight = 0
    for x in zip(animal, items):
        if x[0] == 1:
            total_price += x[1][0]
            total_weight += x[1][1]
    return total_price, total_weight


def sorting(animal):
    price, weight = count_solution_price_and_weight(animal)
    return -price, weight


def choose_parents():
    population.sort(key=sorting)
    return population[0], population[-2]


# should be done two times
def crossing(first_parent, second_parent):
    babies = [first_parent[:pointsOfSplitting[0]], second_parent[:pointsOfSplitting[0]]]
    for x in range(1, len(pointsOfSplitting)):
        firstHalf = list(
            map(lambda baby: baby + first_parent[pointsOfSplitting[x - 1]:pointsOfSplitting[x]], babies[:]))
        secondHalf = list(
            map(lambda baby: baby + first_parent[pointsOfSplitting[x - 1]:pointsOfSplitting[x]], babies[:]))
        babies = firstHalf + secondHalf
    return babies


def check_baby(baby):
    print_animal(baby)
    if count_solution_price_and_weight(baby)[1] > sizeOfRuicksack:
        print('Baby died!')
    else:
        population.append(baby)


def kill(population_to_clean):
    population_to_clean = list(k for k, _ in itertools.groupby(sorted(population_to_clean, key=sorting)))
    for x in range(len(population_to_clean) - maxAnimals):
        del population_to_clean[-1]
    return population_to_clean


def mutate(baby):
    baby = baby.copy()
    gene = randint(0, len(baby) - 1)
    baby[gene] = (baby[gene] + 1) % 2
    print('Mutated baby')
    check_baby(baby)


if __name__ == '__main__':
    for i in range(5):
        print('{} cycle'.format(i + 1))
        print_population()
        first, second = choose_parents()
        print("First parent: ")
        print(first)
        print("Second parent: ")
        print(second)

        babies = crossing(first, second)
        for x in range(len(babies)):
            print('Baby number: {}'.format(x))
            check_baby(babies[x])
        if i % 2 == 0:
            for babe in babies:
                mutate(babe)

        population.sort(key=sorting)
        print_population()
        print('Killing')
        population = kill(population)
        print_population()
        print('-' * 80)
