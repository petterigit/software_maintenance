def fibonacci(a):
    if (a<=1):
        return a
    else:
        return (fibonacci(a-1) + fibonacci(a-2))

def checkLength(length):
    try:
        length = int(length)
    except:
        length = 10
    return length

def checkStartingFrom(startingFrom):
    try:
        startingFrom = int(startingFrom)
    except:
        startingFrom = -1
    return(startingFrom)


def main():
    n = input("Series length (no input uses default): ")
    b = input("Only numbers over (default: -1): ")
    n = checkLength(n)
    b = checkStartingFrom(b)

    file = open("fibonacciResults.txt", "a")

    a = 0
    while ( n > 0 ):
        toPrint = fibonacci(a)
        if (toPrint > b):
            print("Writing: " + str(toPrint) + " to file")
            file.write(str(toPrint) + "\n")
            n = n - 1
        a = a + 1
    
    file.close()
main()

