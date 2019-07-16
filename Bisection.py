low=0
high=100
mean=int((high+low)/2)
print("Please Think of a number between 0 and 100")

while True:
    print("Is your secret number", mean)
    ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.").lower()
    if ans=="l":
        low=mean
    elif ans=="h":
        high=mean
    elif ans=="c":
        break
    else:
        print("please input correctly")
    mean=int((high+low)/2)

print("Game over. Your secret number was:", mean)
