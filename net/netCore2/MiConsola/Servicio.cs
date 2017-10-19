namespace MiConsola
{
    public class Servicio : IServicio
    {
        private int acumulador;

        public Servicio()
        {
            acumulador = 0;
        }

        public int Sumar(int valor)
        {
            acumulador += valor;
            return acumulador;
        }
    }
}