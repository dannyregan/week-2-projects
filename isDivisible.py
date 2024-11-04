def isDivisble(a, i):
    count = 0
    for num in a:
        if num % i == 0:
            count += 1
    return count

def main():
    a1 = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    i1 = 7
    a2 = [18, 54, 76, 81, 36, 48, 99]
    i2 = 9
    print(isDivisble(a1, i1))
    print(isDivisble(a2, i2))

# =================================================
main()