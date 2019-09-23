var perceptron = (function() {
 
    var neuro = function() {
         
        this._seed = 1;
        this._threshold = 1;
        this._bias = 1;
        this._learnRate = 0.1;
        this._weights = [];
        this._neuralData = [];
    };
 
    neuro.prototype._random = function() {
        var x = Math.sin(this._seed++) * 10000;
        return x - Math.floor(x);
    };
 
    neuro.prototype._multiply = function (inputs) {
        var result = 0;
 
        for (var i = 0; i < inputs.length; i++) {
            result += inputs[i] * this._weights[i];
        }
 
        result += this._threshold * this._weights[this._weights.length - 1];
 
        return result;
    },
 
    neuro.prototype._sigmoid = function(x) {
        return 1 / (1 + Math.pow(Math.E, -x));
    };
 
    neuro.prototype._retrain = function() {
        var neuralDataLength = this._neuralData.length;
        var hasSuccess = true;
 
        for (var i = 0; i < neuralDataLength; i++) {
            var trainData = this._neuralData.shift();
 
            hasSuccess = this.train(trainData.input, trainData.target) && hasSuccess;
        }
 
        return hasSuccess;
    };
 
    neuro.prototype.exercise = function(iterations) {
        var i = 0;
 
        while (i++ < iterations) {
            var trainResult = this._retrain();
 
            if (trainResult === true) {
                console.log('Retraining ended after ' + i + ' attempts');
                break;
            }
        }
    };
 
    neuro.prototype.train = function (inputs, expected) {
         
        while (this._weights.length < inputs.length) {
            this._weights.push(this._random());
        }
 
        //neuron bias
        if (this._weights.length === inputs.length) {
            this._weights.push(this._bias);
        }
 
        var preceptionResult = this.process(inputs);
        this._neuralData.push({input: inputs, target: expected, prev: preceptionResult})
 
        if (preceptionResult !== expected) {
            for (var i = 0; i < this._weights.length; i++) { 
                var input = (i == inputs.length) ? this._threshold : inputs[i]; 
                var adjustment = (expected - preceptionResult) * this._learnRate * input;
                
                this._weights[i] += adjustment; 
                
                if (isNaN(this._weights[i])) throw new Error('Weight out of boundaries'); 
            } 
            
            return false; 
        } 
        
        return true; 
    }; 
    
    neuro.prototype.process = function (inputs) { 
        return Number(this._sigmoid(this._multiply(inputs, this._weights)) > 0.5);
    };
 
    return new neuro();
}());

perceptron.train([0, 0], 0);
perceptron.train([0, 1], 0);
perceptron.train([1, 0], 0);

perceptron.exercise(10000);

console.log(perceptron.process([1, 1]));