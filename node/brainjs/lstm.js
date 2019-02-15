const brain = require('brain.js');
const network = new brain.recurrent.LSTMTimeStep();

network.train([
    [1, 16, 10], [2, 16, 12], [3, 16, 11], [4, 16, 8], [5, 16, 5],
    [6, 16, 4], [7, 16, 6], [8, 16, 8], [9, 16, 10], [10, 16, 10],
    [11, 16, 12], [12, 16, 11],
    [1, 17, 11],
    [2, 17, 13],
    [3, 17, 10],
    [4, 17, 7],
    [5, 17, 6],
    [6, 17, 6],
    [7, 17, 7],
    [8, 17, 9],
    [9, 17, 10],
    [10, 17, 11],
    [11, 17, 13],
    [12, 17, 12]
]);

const results = network.run([11, 18]);
console.log(results);