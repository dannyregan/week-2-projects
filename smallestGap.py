# Accepts an array, a. Finds the distance between all possible pairs of numbers in the array and returns the smallest distance.
def smallestGap(a):
    smallestDistance = None
    for index in range(len(a) - 2):
        i = index + 1
        while i <= (len(a) - 1):
            currentDistance = abs(a[index] - a[i])
            if smallestDistance == None or currentDistance < smallestDistance:
                smallestDistance = currentDistance
            i += 1
    return smallestDistance


def main():
    a1 = [50, 120, 250, 100, 20, 300, 200]
    a2 = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    print(smallestGap(a1))
    print(smallestGap(a2))

# =================================================
main()