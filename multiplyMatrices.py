# Accepts an array, a, and intenger, i. Returns the count of the number of elements in the array that are divisible by the integer.
def multiplyMatrices(n, matrix1, matrix2):
    matrix = []
    row = 0
    while row < n:
        column = 0
        multipliedRow = []
        while column < n:
            currentProduct = 0
            for i in range(n):
                product = matrix1[row][i] * matrix2[i][column]
                currentProduct += product
            multipliedRow.append(round(currentProduct, 2))
            column += 1
        matrix.append(multipliedRow)
        row += 1
    return matrix


def main():
    matrix1 = [
        [2, 7],
        [3, 5]
    ]
    matrix2 = [
        [8, -4],
        [6, 6]
    ]
    n1 = 2

    matrix3 = [
        [1, 0, 2],
        [3, -2, 5],
        [6, 2, -3]
    ]
    matrix4 = [
        [.3, .25, .1],
        [.4, .8, 0],
        [-.5, .75, .6]
    ]
    n2 = 3

    print(multiplyMatrices(n1, matrix1, matrix2))
    print(multiplyMatrices(n2, matrix3, matrix4))

# =================================================
main()