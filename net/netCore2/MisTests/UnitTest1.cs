using System;
using Xunit;
using MiConsola;

namespace MisTests
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            var servicio = new Servicio();
            var resultado = servicio.Sumar(10);

            Assert.Equal(10, resultado);
        }

        [Fact]
        public void Test2()
        {
            var servicio = new Servicio();
            servicio.Sumar(20);
            var resultado = servicio.Sumar(10);

            Assert.Equal(30, resultado);
        }
    }
}
