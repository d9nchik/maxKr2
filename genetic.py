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

maxAnimals = len(population)


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
    baby = []
    is_first = True
    for x in range(len(population[0])):
        if is_first:
            baby.append(first_parent[len(baby)])
        else:
            baby.append(second_parent[len(baby)])
        if (x + 1) in pointsOfSplitting:
            is_first = not is_first
    check_baby(baby)
    return baby


def check_baby(baby):
    print_animal(baby)
    if count_solution_price_and_weight(baby)[1] > sizeOfRuicksack:
        print('Baby died!')
    else:
        population.append(baby)


def kill():
    population.sort(key=sorting)
    for x in range(len(population) - maxAnimals):
        del population[-1]


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

        babies = []
        print('First baby')
        babies.append(crossing(first, second))
        print('Second baby')
        babies.append(crossing(second, first))
        if i % 2 == 0:
            for babe in babies:
                mutate(babe)

        population.sort(key=sorting)
        print_population()
        print('Killing')
        kill()
        print_population()
        print('-' * 80)
