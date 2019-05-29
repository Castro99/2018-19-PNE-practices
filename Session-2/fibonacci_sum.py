#Exercise of fibonacci II

x = 0
y = 1
counter=0
n=int(input('Enter desire num to compute the fibonacci series: '))
for i in range(n):
   x, y = y, x+y
   counter += x
print(counter)