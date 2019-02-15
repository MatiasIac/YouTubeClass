using System;

namespace acoplamiento
{

    public interface IAnimal
    {
        void Mensaje();
    }

    public abstract class Animal : IAnimal
    {
        public abstract void Mensaje();
    }

    public abstract class Robot : IAnimal
    {
        public abstract void Mensaje();
    }

    public class Perro : Animal
    {
        public override void Mensaje()
        {
            Console.WriteLine("Perro");
        }
    }

    public class Gato : Animal
    {
        public override void Mensaje()
        {
            Console.WriteLine("Gato");
        }
    }

    public class PerroRobot : Robot
    {
         public override void Mensaje()
        {
            Console.WriteLine("PerroRobot");
        }
    }

    public class GatoRobot : Robot
    {
         public override void Mensaje()
        {
            Console.WriteLine("GatoRobot");
        }
    }

    class Program
    {
        public static IAnimal ConstruirAnimal<T>() 
            where T: IAnimal
        {
            if (typeof(T) == typeof(Gato)) 
            {
                return new Gato();
            }

            if (typeof(T) == typeof(Perro)) 
            {
                return new Perro();
            }

            if (typeof(T) == typeof(PerroRobot)) 
            {
                return new PerroRobot();
            }

            return null;
        }

        static void Main(string[] args)
        {
            var resultado = ConstruirAnimal<Gato>();
            var resultado2 = ConstruirAnimal<Perro>();
            var resultado3 = ConstruirAnimal<PerroRobot>();

            resultado.Mensaje();
            resultado2.Mensaje();
            resultado3.Mensaje();
        }
    }
}
