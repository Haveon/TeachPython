def getData(fileName):
    f = open(fileName)        # make a file object to interact with the csv
    lines = f.readlines()     # Get all the lines from the file
    f.close()                 # Tell python we're done with the file

    firstColumn = []
    secondColumn = []
    thirdColumn = []
    for line in lines:
        first, second, third = line.split(',')    # split along commas
        firstColumn.append(float(first))
        secondColumn.append(float(second))
        thirdColumn.append(float(third))

    return firstColumn, secondColumn, thirdColumn

def processData(col1, col2, col3):
    numberOfLines = len(col1)     # Presumably all are the same length
    results = []
    for i in range(numberOfLines):
        operation = col1[i]
        n = col2[i]
        m = col3[i]

        if operation == 0:
            results.append(n+m)
        else:                   # There's only two options, so only check one
            results.append(n-m)

    return results

def writeData(fileName, results):
    f = open(fileName, 'w')    # We need the 'w' flag to say we want to write to the file

    for result in results:
        f.write( '{}\n'.format(result) )    # Don't forget the newline character

    f.close()
    return

if __name__ == '__main__':     # If this script is the first thing to run, do this
    c1, c2, c3 = getData('data.csv')
    solutions = processData(c1, c2, c3)
    writeData('results.csv', solutions)
