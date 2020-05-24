class Perceptron {

    constructor() {
        this.seed = 1;
        this.threshold = 1;
        this.bias = 0.3;
        this.learnRate = 0.1;
        this.weights = [];
        this.neuralData = [];
    }

    _randomize() {
        const x = Math.sin(this.seed++) * 10000;
        return x - Math.floor(x);
    }

    _multiply(inputs) {
        let result = 0;

        for (var i = 0; i < inputs.length; i++) {
            result += inputs[i] * this.weights[i];
        }

        result += this.threshold * this.weights[this.weights.length - 1];

        return result;
    }

    _sigmoid(x) {
        return 1 / (1 + Math.pow(Math.E, -x));
    }

    _retrain() {
        const neuralDataLength = this.neuralData.length;
        let hasSuccess = true;

        for (let i = 0; i < neuralDataLength; i++) {
            let trainData = this.neuralData.shift();
            hasSuccess = this.train(trainData.input, trainData.target) && hasSuccess;
        }

        return hasSuccess;
    };

    process(inputs) { 
        return Number(this._sigmoid(this._multiply(inputs, this.weights)) > 0.5);
    };

    exercise(iterations) {
        for (let i = 0; i < iterations; i++) {
            if (this._retrain() === true) {
                console.log('Retraining ended after ' + i + ' attempts');
                break;
            }      
        }
    }

    train(inputs, expected) {
        
        while (this.weights.length < inputs.length) {
            this.weights.push(this._randomize());
        }

        //neuron bias
        if (this.weights.length === inputs.length) {
            this.weights.push(this.bias);
        }

        const preceptionResult = this.process(inputs);
        this.neuralData.push({
            input: inputs, 
            target: expected,
            //previousResult: preceptionResult
        });

        if (preceptionResult !== expected) {
            for (let i = 0; i < this.weights.length; i++) { 
                const input = (i == inputs.length) ? this.threshold : inputs[i]; 
                const adjustment = (expected - preceptionResult) * this.learnRate * input; 
                
                this.weights[i] += adjustment; 
                
                if (isNaN(this.weights[i])) {
                    throw new Error('Weight out of boundaries');
                }
            } 
            
            return false; 
        } 
        
        return true; 
    }; 

}

module.exports = Perceptron;