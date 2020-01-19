import sys

def getFibonacci(a):
    if (a<=1):
        return a
    else:
        return (getFibonacci(a-1) + getFibonacci(a-2))

def fibonacci(*args):

    # For command-line usage

    try:
        n = args[0]
        b = args[1]
    except:
        n = 10
        b = -1

    #n = args[0]
    #b = args[1]

    if (isinstance(n, bool)):
        n = 10
    if (isinstance(b, bool)):
        b = -1

    try:
        n = int(n)
    except:
        n = 10

    try:
        b = int(b)
    except:
        b = -1

    file = open("fibonacciResults.txt", "w")

    a = 0
    series = []
    while ( n > 0 ):
        toAppend = getFibonacci(a)
        if (toAppend > b):
            series.append(toAppend)
            n = n - 1
        a = a + 1

    file.write(str(series))
    file.close()

    return(series)

#fibonacci()
