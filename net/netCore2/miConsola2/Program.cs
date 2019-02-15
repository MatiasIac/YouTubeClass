using System;
using System.Collections.Generic;

namespace miConsola2
{

    public class A
    {
        public string Text { get; set; }
    }

    class Program
    {

        static Object ExecuteSomething()
        {
            Console.WriteLine("Execute Something");
            //return false;
            return new A { Text = "Este es el texto para b" };
            //return "Este es el texto para b";
        }

        static bool Funcion1() {
            Console.WriteLine("Funcion 1");
            return true;
        }

        static void Main(string[] args)
        {
            Func<string, bool> action = p => { 
                Console.WriteLine(p); 
                return true; 
            };

            var variable1 = true;

            _ = (variable1 &&
                (ExecuteSomething() is A b) &&
                Funcion1() &&
                action(b.Text));

        }
    }
}
