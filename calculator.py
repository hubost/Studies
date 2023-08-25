#define functions add, sub, mul, div

def add(a, b):
    answerA = a+b
    print(str(a) + "+" + str(b) + "=" + str(answerA)+ "\n")

def sub(a,b):
    answerS = a - b
    print(str(a) + "+" + str(b) + "=" + str(answerS)+ "\n")

def mul(a,b):
    answerM = a * b
    print(str(a) + "+" + str(b) + "=" + str(answerM)+ "\n")

def div(a,b):
    answerD = a / b
    print(str(a) + "+" + str(b) + "=" + str(answerD)+ "\n")

#while loop to continue the program running
while True:
    # print options to user
    print("1 Addition")
    print("2 Substraction")
    print("3 Multiplication")
    print("4 Division)")
    print("5 Exit")
    # ask for values
    choice = input("Choose option:")
    if choice == "1" :
        print("Addition")
        a = int(input("Input 1st value:"))
        b = int(input("Input 2nd value:"))
        # call the functions
        add(a,b)
    elif choice == "2":
        print("Substraction")
        a = int(input("Input 1st value:"))
        b = int(input("Input 2nd value:"))
        sub(a, b)
    elif choice == "3":
        print("Multiplication")
        a = int(input("Input 1st value:"))
        b = int(input("Input 2nd value:"))
        mul(a, b)
    elif choice == "4":
        print("Division")
        a = int(input("Input 1st value:"))
        b = int(input("Input 2nd value:"))
        div(a, b)
    elif choice== "5":
        print("Exit")
        exit()

