def fib(n):
    if n <= 2:
        return [1]*n    # list times int is the same as list+list+...+list (n times)
    else:
        fibList = [1,1]
        for i in range(n-2):    # We need to substract since we already have the first two numbers
            fibList.append(fibList[-2] + fibList[-1])
        return fibList
