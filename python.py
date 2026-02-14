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

#Third code
def number_guessing_game():
    secret_number = random.randint(1, 100) # Generate a random number between 1 and 100
    print("Guess the number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()


#forth code
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
