#Exercise of fibonacci I

def fibonacci_series(num):
    value = 0
    x,y = 0,1
    fibonacci_series=[]


    while value < num:
        fibonacci_series.append(x)
        z = x + y
        x = y
        y = z
        value += 1
    return fibonacci_series


num = int(input('Enter desire num to compute the fibonacci series: '))


print(fibonacci_series(num))