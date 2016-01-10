def fibonacciRec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRec(n-2) + fibonacciRec(n-1)

