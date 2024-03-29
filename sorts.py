from typing import List

array = [8, 23, 5, 65, 44, 33, 1, 6]


def direct_merge(array: List[float], k: int = 0):
    """
    Direct merge sort

    :param array: array to be sorted
    :param k: this parameter for recursive call(don't provide it)
    :return: sorted array
    """
    two_power_k = 2 ** k
    if two_power_k >= len(array):
        print('The end')
        return array

    print('Iteration number: {}'.format(k + 1))
    a = []
    b = []
    for x in range(len(array)):
        if x % two_power_k == x % (two_power_k * 2):
            a.append(array[x])
        else:
            b.append(array[x])

    print('a = {}'.format(a))
    print('b = {}'.format(b))
    c = []

    while len(a) != 0 and len(b) != 0:
        a_slice_point = min(len(a), two_power_k)
        mini_a = a[:a_slice_point]
        a = a[a_slice_point:]

        b_slice_point = min(len(b), two_power_k)
        mini_b = b[:b_slice_point]
        b = b[b_slice_point:]

        while len(mini_a) > 0 and len(mini_b) > 0:
            if mini_a[0] < mini_b[0]:
                c.append(mini_a.pop(0))
            else:
                c.append(mini_b.pop(0))

        while len(mini_a) > 0:
            c.append(mini_a.pop(0))

        while len(mini_b) > 0:
            c.append(mini_b.pop(0))

    while len(a) > 0:
        c.append(a.pop(0))

    while len(b) > 0:
        c.append(b.pop(0))

    print('c = {}'.format(c))

    return direct_merge(c, k + 1)


def natural_merge(array: List[float]):
    """
    Natural merge sort

    :param array: array to be sorted
    :return: sorted array
    """
    arrays = [[], []]
    previous_value = float('-inf')
    for element in array:
        if previous_value > element: arrays.reverse()
        arrays[0].append(element)
        previous_value = element

    if len(arrays[1]) == 0:
        print('end')
        return array

    a, b = arrays
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    c = []

    while len(a) > 0 and len(b) > 0:
        previous_value_a = float('-inf')
        previous_value_b = float('-inf')
        while len(a) > 0 and len(b) > 0 and previous_value_a < a[0] and previous_value_b < b[0]:
            if a[0] < b[0]:
                previous_value_a = a.pop(0)
                c.append(previous_value_a)
            else:
                previous_value_b = b.pop(0)
                c.append(previous_value_b)

        while len(a) > 0 and previous_value_a < a[0]:
            previous_value_a = a.pop(0)
            c.append(previous_value_a)

        while len(b) > 0 and previous_value_b < b[0]:
            previous_value_b = b.pop(0)
            c.append(previous_value_b)

    while len(a) > 0:
        c.append(a.pop(0))

    while len(b) > 0:
        c.append(b.pop(0))

    print('array after merge = {}'.format(c))
    return natural_merge(c)


def balanced_poly_path_merge(array: List[float], number_of_files: int = 3):
    """
    Balanced poly path merge

    :param array: array to be sorted
    :param number_of_files: how many file you need to use (default 3)
    :return: sorted array
    """
    files = []
    for x in range(number_of_files):
        files.append([])

    for x in range(len(array)):
        files[x % number_of_files].append(array[x])

    print('files before sort: {}'.format(files))
    for file in files:
        file.sort()
    print('files after sort: {}'.format(files))

    c = []
    while len(c) != len(array):
        values = []
        for file in files:
            if len(file) == 0:
                values.append(float('inf'))
            else:
                values.append(file[0])

        next_value = min(values)
        files[values.index(next_value)].pop(0)
        c.append(next_value)

    return c


def fibonacci_n(n: int):
    """
    Fibonacci n-order

    :param n: order
    :return: function that calculates fibonacci of order n of x argument
    """
    array = []
    for x in range(n):
        array.append(0)
    array.append(1)

    def fibonacci(number: int):
        """
        fibonacci

        :param number: n member
        :return: result of function in this point
        """
        try:
            return array[number - 1]
        except IndexError:
            sum = 0
            for x in range(number - n - 1, number):
                sum += fibonacci(x)
            array.append(sum)
            return sum

    return fibonacci


def get_ideal_division(n: int, depth: int = 10):
    """
    Get ideal division - useful for Multiphase sorting

    :param n: number of files
    :param depth: which depth you want to have
    :return: matrix of size n by depth
    """
    fibonacci = fibonacci_n(n - 1)

    # formula for getting  a_k(L)
    def get_a(k: int, L: int):
        """
        get_a

        :param k: number of row (starting from 1)
        :param L: number of column (starting from 0)
        :return: value a of to order k
        """
        sum = 0
        for fibonacci_index in range(max(L + k - 1, 0), L + n):
            sum += fibonacci(fibonacci_index)
        return sum

    # printing table
    ideal_division = []
    for x in range(depth):
        ideal_row_division = []
        for y in range(n):
            ideal_row_division.append(get_a(y + 1, x))
        ideal_division.append(ideal_row_division)
    return ideal_division


def pretty_print(array: List[List[int]]):
    for row in array:
        for element in row:
            print(element, end='\t')
        print()


if __name__ == '__main__':
    # print(direct_merge(array))
    # print(natural_merge(array))
    # print(balanced_poly_path_merge(array))
    pretty_print(get_ideal_division(5))
