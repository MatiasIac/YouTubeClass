var A = (function () {
    function A(mensaje) {
        this._message = mensaje;
    }
    A.prototype.mostrar = function () {
        console.log(this._message);
    };
    return A;
}());
var a = new A("Hola mundo!");
a.mostrar();
