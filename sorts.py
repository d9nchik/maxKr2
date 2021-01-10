array = [8, 23, 5, 65, 44, 33, 1, 6]


def direct_merge(array, k=0):
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


if __name__ == '__main__':
    print(direct_merge(array))
