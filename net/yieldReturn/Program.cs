using System;
using System.Collections.Generic;
using System.Linq;

namespace yieldReturn
{
    class Program
    {
        public static IEnumerable<int> GetLista(int start)
        {
            for (int i = start; i < i + 2;)
            {
                i += 2;
                yield return i;
            }
        }

        static void Main(string[] args)
        {
            var lista = GetLista(100).Take(100).ToList();

            foreach (var item in lista)
            {
                Console.WriteLine(item);
            }
        }
    }
}
