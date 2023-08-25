
pln = 1.00
dolar = 4.14
euro = 4.47
def main():
    value = input("Wprowadź liczbę którą chcesz zamienić: ")
    currency = input("Wprowadź obecną walutę (PLN/€/$): ")
    currencyTo = input("Wprowadź nową walutę (PLN/€/$): ")
    if currency == '$':
        if currencyTo == 'PLN' :
            totalValue = (pln * dolar) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"PLN.")
        elif currencyTo == '€':
            totalValue = (dolar / euro) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"euro.")
    if currency == 'PLN':
        if currencyTo == '$' :
            totalValue = (pln / dolar) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"$.")
        elif currencyTo == '€':
            totalValue = (pln / dolar) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"euro.")
    if currency == '€':
        if currencyTo == 'PLN' :
            totalValue = (pln * euro) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"PLN.")
        elif currencyTo == '$':
            totalValue = (euro / dolar) * int(value)
            print("Wymieniono na "+str(int(totalValue))+"$.")

    ##if currency == 'PLN':

   ## if currency == '€':
main()


