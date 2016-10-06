def fibGen():
    yield 1    # First two fibonacci's are 1, so yield 1 twice
    yield 1
    a = 1
    b = 1
    while True:         # Don't stop calculating numbers!
        a, b = b, a+b   # The right side is executed then assigned to the left
        yield b         # yield the next number

if __name__ == '__main__':
    myGen = fibGen()
    for i in range(11):
        print( next(myGen) )    # Use next() to resume exceution after the yield
