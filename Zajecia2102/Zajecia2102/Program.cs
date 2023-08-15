using System;

namespace Zajecia2102
{
    class Program
    {
        /* static void Main(string[] args)
        {
            
            Console.WriteLine("Wczytaj znak");
            int znak = Console.Read();

            Console.WriteLine("Wprowadzony znak to " + znak);

            // znak = 97 + (znak + 3 - 97) % 26;

            znak = 97 + (38 - znak + 97) % 26;
            char znak1 = (char)znak;
            
            Console.WriteLine("Wprowadzony znak to " + znak1);
            Console.ReadKey(); 
         
        } */

        static void Cezar(String[] args)
        {
            Console.WriteLine("Wprowadź z klawiatury wiadomość do szyfrowania: ");
            ConsoleKeyInfo keyInfo;
            do
            {
                keyInfo = Console.ReadKey(true);
                if (keyInfo.KeyChar >= 97 && keyInfo.KeyChar <= 122)
                {
                    char znak = (char)(((keyInfo.KeyChar - 94) & 26) + 97);
                    Console.Write(znak);
                }

            } while (keyInfo.Key != ConsoleKey.Escape);
        }

        static void Szyfr(String[] args)
        {
            int[,] array1 = { { 1, 2, 3, 4, 5 }, { 6, 7, 8, 9, 10 }, {11, 12, 13, 14, 15},
{16, 17, 18, 19, 20}, {21, 22, 23, 24, 25} };
            int[,] array2 = new int[5, 5];
            System.Array.Clear(array2, 0, array2.Length);
            Console.WriteLine("Tablica jawna wyglada tak: ");
            for (int i = 0; i <= 4; i++) //wyświetlanie array1 - tekst jawny
            {
                for (int j = 0; j <= 4; j++)
                {
                    Console.WriteLine("array1[{0},{1}]={2}", i, j, array1[i, j]);
                }
            }
            for (int i = 0; i <= 4; i++) //zamiana - szyfrowanie
            {
                for (int j = 0; j <= 4; j++)
                {
                    array2[i, j] = array1[j, i];
                }
            }
            Console.WriteLine("Tablica zaszyfrowana wygląda tak: ");
            for (int i = 0; i <= 4; i++) //wyświetlanie array2 - tekst zaszyfrowany
            {
                for (int j = 0; j <= 4; j++)
                {
                    Console.WriteLine("array2[{0},{1}]={2}", i, j, array2[i, j]);
                }
            }
            Console.ReadKey();
        }
            
    }
}
