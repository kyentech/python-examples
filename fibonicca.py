#f(n) = f(n-2) + f(n-1)
def fib(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return(n-2) + (n-1)
my_num=fib(int(input()))
print(my_num)
     