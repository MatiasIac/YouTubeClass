class Base {
    constructor() {

    }

    myFunc() {

    }
}

class A extends Base {
    constructor() {
        super();
    }
}

Base.prototype.anotherFunc = function () {
    
};

let a = new A();