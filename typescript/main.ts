
class A {

    _message: any;

    constructor(mensaje: any) {
        this._message = mensaje;
    }

    mostrar() : void {
        console.log(this._message);
    }
}

var a = new A("Hola mundo!");
a.mostrar();