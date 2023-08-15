using System;
using System.Security.Cryptography;
using System.Text;

namespace Zajecia2802
{
    class Program
    {
        public static void Main()
        {
            try
            {
                string original = "Dane do zaszyfrowania";
                using (Aes myAes = Aes.Create())
                {
                    byte[] encrypted = EncryptStringToBytes_Aes(original, myAes.Key, myAes.IV);
                    string roundtrip = DecryptStringFromBytes_Aes(encrypted, myAes.Key, myAes.IV);
                    Console.WriteLine("Original: {0}", original);
                    Console.WriteLine("Round Trip: ", original);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: {0}", e.Message);
            }
            System.Console.ReadKey();
        }

        static byte[] EncryptStringToBytes_Aes(string plainText, byte[] Key, byte[] IV)
        {
            if (plainText == null || plainText.Length <= 0)
                throw new ArgumentNullException("plainText");
            if (Key == null || Key.Length <= 0)
                throw new ArgumentNullException("Key");
            if (IV == null || IV.Length <= 0)
                throw new ArgumentNullException("Key");
            byte[] encrypted;
            using (Aes aesAlg = Aes.Create())
            {
                aesAlg.Key = Key;
                aesAlg.IV = IV;
                ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key, aesAlg.IV);
                using (MemoryStream msEncrypt = new MemoryStream())
                {
                    using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                    {
                        using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                        {
                            swEncrypt.Write(plainText);
                        }
                        encrypted = msEncrypt.ToArray();
                    }
                }
            }
            return encrypted;
        }
        static string DecryptStringFromBytes_Aes(byte[] cipherText, byte[] Key, byte[] IV)
        {
            if (cipherText == null || cipherText.Length <= 0)
                throw new ArgumentNullException("cipherText");
            if (Key == null || Key.Length <= 0)
                throw new ArgumentNullException("Key");
            if (IV == null || IV.Length <= 0)
                throw new ArgumentNullException("Key");
            string plaintext = null;
            using (Aes aesAlg = Aes.Create())
            {

            }
        }


















            /* static void Main(string[] args)
            {
                string source = "Hello World";
                using (MD5 md5Hash = MD5.Create())
                {
                    string hash = GetMd5Hash(md5Hash, source);
                    Console.WriteLine("The MD5 hash of " + source + " is: " + hash + ".");
                    Console.ReadKey();
                }

            }

            static string GetMd5Hash(MD5 md5Hash, string input)
            {
                byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));
                StringBuilder sBuilder = new StringBuilder();
                for (int i=0;i<data.Length; i++)
                {
                    sBuilder.Append(data[i].ToString("x2"));
                }
                return sBuilder.ToString();
            }
            static bool VerifyMd5Hash(MD5 md5Hash, string input, string hash)
            {
                string HashOfInput = GetMd5Hash(md5Hash, input);
                StringComparer comparer = StringComparer.OrdinalIgnoreCase;
                if ( 0 == comparer.Compare(HashOfInput, hash))
                {
                    return true;
                }
                else
                {
                    return false;
                }

            }
            */
        }
    }

