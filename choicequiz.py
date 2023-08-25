quiz = {
    "pytanie1": {
    "pytanie": "Jaka jest stolica Francji?",
    "odpowiedz": "Paryż"
    },"pytanie2":{
    "pytanie": "Jaka jest stolica Polski?",
    "odpowiedz": "Warszawa"
    },"pytanie3":{
    "pytanie": "Jaka jest stolica Hiszpanii?",
    "odpowiedz": "Madryt"
    },"pytanie4":{
    "pytanie": "Jaka jest stolica Niemiec?",
    "odpowiedz": "Berlin"
    },"pytanie5":{
    "pytanie": "Jaka jest stolica Holandii?",
    "odpowiedz": "Amsterdam"
    },"pytanie6":{
    "pytanie": "Jaka jest stolica Belgii?",
    "odpowiedz": "Bruksela"
    },
}
score = 0
for key, value in quiz.items():
    print(value['pytanie'])
    odpowiedz = input("Odpowiedz?")

    if odpowiedz.lower() == value['odpowiedz'].lower():
        print("Zgadza sie")
        score = score +1
        print("Twój wynik to: "+str(score))
    else:
        print("Spróbuj jeszcze raz")
        print("Odpowiedź to "+value['odpowiedz'])
        print("Twój wynik to: " + str(score))

print("Zdobyłeś "+str(score)+" punktów.")
print("Wynik procentowy to: "+str(int(score/7*100)) + "%")

