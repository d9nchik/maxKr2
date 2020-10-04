inf = float('inf')
distance_matrix = [[inf, 23, 20, 4, 12],
                   [11, inf, 15, 21, 8],
                   [14, 30, inf, 1, 25],
                   [2, 9, 16, inf, 5],
                   [18, 13, 3, 10, inf]]
L = 3
B = 2
Y = 0.3
pheromon_matrix = [[0, 0.2, 0.1, 0.1, 0.2],
                   [0.1, 0, 0.3, 0.2, 0.1],
                   [0.3, 0.3, 0, 0.3, 0.3],
                   [0.3, 0.2, 0.3, 0, 0.3],
                   [0.2, 0.3, 0.1, 0.3, 0]]


class Ant:
    def __init__(self) -> None:
        super().__init__()
        path = []

    def spread_pheromone(self):
        pass
