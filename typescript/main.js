var MiEspacioDeNombre;
(function (MiEspacioDeNombre) {
    var math = (function () {
        function math() {
        }
        math.prototype.sum = function (valor1, valor2) {
            return valor1 + valor2;
        };
        return math;
    }());
    MiEspacioDeNombre.math = math;
})(MiEspacioDeNombre || (MiEspacioDeNombre = {}));
var a = new MiEspacioDeNombre.math();
console.log(a.sum(10, 10));
