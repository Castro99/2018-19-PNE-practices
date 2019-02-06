#Exercise of fibonacci II

def fibonacci_series(num):
    value = 0
    x,y = 0,1
    fibonacci_series=[]


    while value < num:
        fibonacci_series.append(x)
        z = x + y
        y = z
        x = y
        value += 1
    return fibonacci_series


num = int(input('Enter desire num to compute the fibonacci series: '))

def fibonacci_series_total(series):
    final_fibonacci_series = 0
    for i in series:
        final_fibonacci_series += i
    return final_fibonacci_series

total=fibonacci_series_total(fibonacci_series(num))

print("The final output of fibonacci series is: ", total)