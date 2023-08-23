user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)
# [] - python list
todos = [todo1,todo2,todo3,"Hello"]
print(todos)
print("typ danych:",type(user_prompt))
print("typ danych:",type(todos))
print("typ danych:",type(todo1))

# prompt type: string, todos type: list, todo1 type: string

# both '' and "" can be used but '' can be more confusing (example: ' don't '

# wide space doesn't matter in python (example: todo=2 and todo = 2)

#one declaration in one line

#python console is used for throwaway-code that u want to test

#########################################################################################################################
user_prompt = "Enter a todo: "
todos = []
count = 0
while count < 3:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)
    count = count+1

# for, while, do while, if, - loops

#append - add element to list
#capitalize - first letter uppercase
#title - all first letters uppercase  todos.append(todo.title())


##methods - powtórzyć, arguments - powtórzyć

password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")
print("Correct password")
####

name = input("What is your name? ")
while True:
    print(name.capitalize())
#####
x = 0
while x<5:
    name = input("Insert your name: ")
    name_upper = name.capitalize()
    print(name_upper)
    x = x+1