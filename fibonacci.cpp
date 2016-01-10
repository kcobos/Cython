int fibonacciRec(int n){
    if (n==0)
        return 0;
    else if (n==1)
        return 1;
    else
        return fibonacciRec(n-2) + fibonacciRec(n-1);
}

extern "C" {
	int fibonacciRecC(int n){return fibonacciRec(n);}
}

