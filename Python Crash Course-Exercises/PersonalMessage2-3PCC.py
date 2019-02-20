name=input("What is your name? ")
try:
    name=str(name)
    name=name.strip()
except:
    print("Please input a name")
print("Hello", name.title() +  ', would you like to learn Python today?')
