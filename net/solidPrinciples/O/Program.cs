using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    public interface IForma
    {
        void Dibujar();
    }

    public class Rectangulo : IForma
    {
        public void Dibujar()
        {
            throw new NotImplementedException();
        }
    }

    public class Circulo : IForma
    {
        public void Dibujar()
        {
            throw new NotImplementedException();
        }
    }

    public class Triangulo : IForma
    {
        public void Dibujar()
        {
            throw new NotImplementedException();
        }
    }

    public class Cuadrado : IForma
    {
        public void Dibujar()
        {
            throw new NotImplementedException();
        }
    }

    public class Dibujador
    {
        public void Dibujar(List<IForma> formas)
        {
            foreach (var forma in formas)
            {
                forma.Dibujar();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var listaDeFormas = new List<IForma>
            {
                new Circulo(),
                new Rectangulo(),
                new Rectangulo(),
                new Triangulo(),
                new Cuadrado()
            };

            new Dibujador()
                .Dibujar(listaDeFormas);

            Console.ReadLine();
        }
    }
}