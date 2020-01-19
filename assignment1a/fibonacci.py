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


    ### Below if checks commented out for test run 2
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

    ### Below line was commented out for test run 3
    file.write(str(series))
    file.close()

    return(series)

#fibonacci()
