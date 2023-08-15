using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Zaliczenie_Ostrowski
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void S_Click(object sender, EventArgs e)
        {

        }
        private static String encryptcezar(String txt, int key)
        {
            String encryptedcezar = "";

            for (int i = 0; i < txt.Length; i++)
            {
                if (Char.IsUpper(txt[i]))
                {
                    int characterIndex = txt[i] - (char)('A');
                    int characterShifted = (characterIndex + key) % 26 + (char)('A');
                    encryptedcezar += (char)(characterShifted);
                }
                else if (Char.IsUpper(txt[i]))
                {
                    int characterIndex = txt[i] - (char)('a');
                    int characterShifted = (characterIndex + key) % 26 + (char)('a');
                    encryptedcezar += (char)(characterShifted);
                }
                else if (Char.IsDigit(txt[i]))
                {
                    int characterNew = (int)(txt[i] + key) % 10;
                    encryptedcezar += (char)(characterNew);
                }
                else { encryptedcezar += txt[i]; }
            }
            return encryptedcezar;

        }
        private static String decryptcezar(String txt, int key)
        {
            String decryptedcezar = "";
            key = key % 26;

            for (int i = 0; i < txt.Length; i++)
            {
                if (Char.IsUpper(txt[i]))
                {
                    int characterIndex = txt[i] - (char)('A');
                    int characterOrgPos = (characterIndex - key) % 26 + (char)('A');
                    decryptedcezar += (char)(characterOrgPos);
                }
                else if (Char.IsLower(txt[i]))
                {
                    int characterIndex = txt[i] - (char)('a');
                    int characterOrgPos = (characterIndex - key) % 26 + (char)('a');
                    decryptedcezar += (char)(characterOrgPos);
                }
                else if (Char.IsDigit(txt[i]))
                {
                    int characterOrgPos = (txt[i] - key) % 10;
                    decryptedcezar += (char)(characterOrgPos);
                }
                else { decryptedcezar += txt[i]; }
            }
            return decryptedcezar;
        }


        private void button1_Click(object sender, EventArgs e)
        {
            double a = trackBar1.Value;
            int przesuniecie = (int)a;
            string encryptedTxt = encryptcezar(textBox1.Text, przesuniecie);
            textBox2.Text = encryptedTxt;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            double b = trackBar1.Value;
            int przesuniecie2 = (int)b;
            string decryptedTxt = decryptcezar(textBox2.Text, przesuniecie2);
            textBox3.Text = decryptedTxt;
        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public void vigenereEncrypt(ref StringBuilder s, string key)
        {
            for (int i = 0; i < s.Length; i++) s[i] = char.ToUpper(s[i]);
            key = key.ToUpper();
            int j = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if (char.IsLetter(s[i]))
                {
                    s[i] = (char)(s[i] + key[j] - 'A');
                    if (s[i] > 'Z') s[i] = (char)(s[i] - 'Z' + 'A' - 1);

                }
                j = j + 1 == key.Length ? 0 : j + 1;

            }


            
        }

        public void VigenereDecrypt (ref StringBuilder s, string key)
        {
            for (int i = 0; i < s.Length; i++) s[i] = char.ToUpper(s[i]);
            key = key.ToUpper();
            int j = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if (Char.IsLetter(s[i]))
                {
                    s[i] = s[i] >= key[j] ?
                       (char)(s[i] - key[j] + 'A') :
                       (char)('A' + ('Z' - key[j] + s[i] - 'A') + 1);
                }
                j = j + 1 == key.Length ? 0 : j + 1;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            StringBuilder s = new StringBuilder(textBox4.Text);
            string key = textBox5.Text;
            vigenereEncrypt(ref s, key);
            textBox6.Text = Convert.ToString(s);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            StringBuilder s = new StringBuilder(textBox7.Text);
            string key = textBox8.Text;
            VigenereDecrypt(ref s, key);
            textBox9.Text = Convert.ToString(s);
        }
    }
}


