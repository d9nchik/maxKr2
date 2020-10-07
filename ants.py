inf = float('inf')
distance_matrix = [[inf, 23, 20, 4, 12],
                   [11, inf, 15, 21, 8],
                   [14, 30, inf, 1, 25],
                   [2, 9, 16, inf, 5],
                   [18, 13, 3, 10, inf]]
L = 3  # alfa
B = 2  # betta
Y = 0.7  # gamma
pheromone_matrix = [[0, 0.2, 0.1, 0.1, 0.2],
                    [0.1, 0, 0.3, 0.2, 0.1],
                    [0.3, 0.3, 0, 0.3, 0.3],
                    [0.3, 0.2, 0.3, 0, 0.3],
                    [0.2, 0.3, 0.1, 0.3, 0]]

Lmin = 57 + 5


class Ant:
    def __init__(self, start_point) -> None:
        super().__init__()
        self.path = []
        self.length = inf
        self.start_point = start_point

    def spread_pheromone(self):
        print('Spreading pheromone')
        current_position = self.path[-1]
        for node in self.path:
            pheromone_matrix[current_position][node] += Lmin / self.length
            print('pheromone_matrix[{}][{}] += {}'.format(current_position, node, Lmin / self.length))
            current_position = node

    def come_through_path(self):
        self.path = []
        current_point = self.start_point
        unvisited = [y for y in range(len(distance_matrix))]
        unvisited.remove(current_point)
        self.path.append(current_point)
        while len(unvisited) > 0:
            Ant.display_unvisited(current_point, unvisited)
            unvisited.sort(key=lambda e: Ant.calculate_need_to_go(current_point, e), reverse=True)
            current_point = unvisited[0]
            print('Choose {}'.format(current_point))
            unvisited.remove(current_point)
            self.path.append(current_point)
        self.length = Ant.calculate_path_length(self.path)

    @staticmethod
    def display_unvisited(previous, unvisited):
        for node in unvisited:
            print('{}) = {}'.format(node, Ant.calculate_need_to_go(previous, node)))

    @staticmethod
    def calculate_path_length(path_value):
        current_position = path_value[-1]
        length = 0
        for node in path_value:
            length += distance_matrix[current_position][node]
            current_position = node
        return length

    @staticmethod
    def calculate_need_to_go(i, j):
        return (pheromone_matrix[i][j] ** L) * ((1 / distance_matrix[i][j]) ** B)


def display_pheromone():
    for line in pheromone_matrix:
        for value in line:
            print('%.4f' % value, end=' ')
        print()


def blow_out_pheromone():
    for line in range(len(pheromone_matrix)):
        for y in range(len(pheromone_matrix[line])):
            pheromone_matrix[line][y] *= (1 - Y)


if __name__ == '__main__':
    path = []
    ant = Ant(0)
    for x in range(2):
        print('{} cycle'.format(x + 1))
        ant.come_through_path()
        blow_out_pheromone()
        display_pheromone()
        ant.spread_pheromone()
        if ant.length < Lmin:
            Lmin = ant.length
            path = ant.path
            print('New Lmin={}, path={}'.format(Lmin, path))
        display_pheromone()
        print('-' * 60)
    print('Path: {}; Lmin={}'.format(path, Lmin))
