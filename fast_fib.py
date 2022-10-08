def fibonacci(n):
    if n == 0:
        return[0,1]
    else:
        a,b = fibonacci(n//2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return[c,d]
        else:
            return[d, c+d]
def fib(n):
    if (n < 0):
        n = -n
        x = -1
        for i in range(0,n):
            x = x*-1
            
        
        return (fibonacci(n)[0] * x)
    else:
        return fibonacci(n)[0]
