const Perceptron = require("./perceptron/perceptronES6");

const getMaxOf = function(property, trainingModels) {
    return Math.max(...trainingModels.map(t => t[property]));
}

const getLine = function () {
    const w = perceptron.weights;
    const processCoords = {
        y1:-w[2]/w[1],
        y2:-(w[0]+w[2])/w[1],
    };
    
    return processCoords;
}

const perceptron = new Perceptron();

const trainingSet = [
    {name:"Human",x1:32,x2:175,cat:1},
    {name:"Horse",x1:24,x2:170,cat:1},
    {name:"Cat",x1:20,x2:50,cat:1},
    {name:"Piranha",x1:30,x2:10,cat:0},
    {name:"Elephant",x1:24,x2:340,cat:1},
    {name:"Crocodile",x1:64,x2:250,cat:0},
    {name:"Hyena",x1:34,x2:120,cat:0}
];

const maxX = getMaxOf("x1", trainingSet);
const maxY = getMaxOf("x2", trainingSet);

trainingSet.forEach(set => {
    perceptron.train([set.x1 / maxX, set.x2 / maxY], set.cat);
});

console.log(`w: ${perceptron.weights}`);
perceptron.exercise(10000);
console.log(`w: ${perceptron.weights}`);

console.log(perceptron.process([1 / maxX, 200 / maxY]));
console.log(perceptron.process([80 / maxX, 300 / maxY]))
console.log(perceptron.process([20 / maxX, 40 / maxY]));

const size = 340;
const processCoords = getLine();
console.log(`Y1: ${processCoords.y1 * size}, Y2: ${processCoords.y2 * size}`);