#First code
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)


#Second code
numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    product = product * number
print('The product is:', product)
