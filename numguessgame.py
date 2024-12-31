import random

def main():
    randomInt = random.randint(0,10)
    print("This is the Number Guessing Game! You have 3 tries to guess the number 0-100.")
    attempt = 0
    check = True

    while check and attempt < 3:
        userInput = input('Enter a number 0-100: ')
        attempt += 1

        try:
            num = int(userInput)
            if num == randomInt:
                print("You Win!!!")
                check = False
            elif abs(num - randomInt) <= 5:
                if num > randomInt:
                    print(f"{num} is slightly higher than the random integer.")
                else:
                    print(f"{num} is slightly lower than the random integer.")
            elif num > randomInt:
                print(f"{num} is higher than the random integer.")
            elif num < randomInt:
                print(f"{num} is lower than the random integer.")
        except ValueError:
            print(f"{userInput} is not an integer within 1-10.")

    if attempt == 3:
        print(f"Three tries exceeded. The correct answer was {randomInt}.")
    
if __name__ == "__main__":
    main()