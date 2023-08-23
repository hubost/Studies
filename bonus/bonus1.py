query = input('Check length of the variable: ')
total_length = len(query)
print("Length:", total_length)

my_variable = 'text'
print(type(my_variable))

query = 'podaj query'
printuj = input(query)
print(printuj)

my_variable = ['a', 'b', 'c', 'd']
answers = ['yes', 'no', 'yes', 'no', 'no']

my_answer = input("What is your answer?")
answers = ['yes', 'no', 'yes', 'no', my_answer]

greeting = "hello"
print(greeting.upper())

countries = []
while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)