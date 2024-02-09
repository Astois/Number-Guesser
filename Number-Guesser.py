def main():
    import random
    print("try to guess the number, between 1 and 100"),
    print("you have 5 guesses"),

    MyNumber = random.randint(1, 100)
    count = 5

    while count > 0:
        UserNumber = int(input("guess the number: "))
        if UserNumber == MyNumber:
            print("you win")
            return
        else:
            count -=1
            print(f"you have {count} guesses left")
            
    if count == 0 : 
        print("You lose!")

        
main()
        