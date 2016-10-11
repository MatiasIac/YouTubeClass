namespace MiEspacioDeNombre {

    export class math {

        sum(valor1: number, 
            valor2: number) : any {
                return valor1 + valor2;
        }

    }

}

var a = new MiEspacioDeNombre.math();
console.log(a.sum(10, 10));