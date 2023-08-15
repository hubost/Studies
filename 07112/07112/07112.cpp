// 07112.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include <iostream>


int main()
{
    int wynikand,wyniknand;

    int wynikor,wynikxor,wyniknor,wynikxnor;

    int wyniknot1, wyniknot2;

    int a, b;
    std::cout << "Podaj A:";
    std::cin >> a;
    std::cout << "Podaj B:";
    std::cin >> b;
    if (a == 0 || a == 1 && b == 0 || b == 1) {

        //and
        wynikand = a * b;
        std::cout <<" AND "<< a << " * " << b << " = " << wynikand << std::endl;
        //or
        wynikor = a + b;
        if (wynikor > 1) {
            wynikor = 1;
        }
        std::cout << "  OR " << a << " + " << b << " = " << wynikor << std::endl;

        //not
        wyniknot1 = (!a); wyniknot2 = (!b);
        std::cout << " NOT " << a << " = " << wyniknot1 << " , " << b << " = " << wyniknot2 << std::endl;

        //nand
        wyniknand = (!wynikand);
        std::cout << "NAND " << a << " * " << b << " = " << wyniknand << std::endl;

        //nor
        wyniknor = (!wynikor);
        std::cout << " NOR " << a << " + " << b << " = " << wyniknor << std::endl;
        //xor
        wynikxor = 1;
        if (a == b) {
            wynikxor = 0;
        }
        std::cout << " XOR " << a << " + " << b << " = " << wynikxor << std::endl;
        //xnor
        wynikxnor = (!wynikxor);
        std::cout << "XNOR " << a << " + " << b << " = " << wynikxnor << std::endl;
   
    }
        
        else std::cout << "A i B musza miec wartosc 0 lub 1.";


    }


// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln
