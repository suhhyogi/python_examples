import numpy as np

x = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])

def pivotal(n, array):
    print('{}, {}'.format(n, array))
    if n == len(array):
        return array
    else:
        y = array
        for i in range(0, len(array)):
            y[n][i] = array[i][n]
            y[i][n] = array[n][i]

        return pivotal(n + 1, y)

print(pivotal(1, x))



