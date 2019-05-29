#Exercise make a function n that print the sum of the numbers

number = int(input("Enter number n: "))
def total_sum(n):
    total_number = 0
    for i in range(n):
        total_number = total_number + i + 1

    return total_number


print("The sum of the number you introduce is :", total_sum(number))