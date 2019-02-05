#Exercise of fibonacci I

num = int(input('Enter desire num to compute the fibonacci series: '))


def fibonacci_series(num):
    value = 0
    x = 0
    y = 1
    fibonacci_series=[]


    while value < num:
        fibonacci_series.append(x)
        z = x + y
        x = y
        y = z
        value += 1
    return fibonacci_series


print(fibonacci_series(num))