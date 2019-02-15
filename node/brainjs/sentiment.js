const brain = require('brain.js');
const network = new brain.NeuralNetwork();

const fixLengths = (data) => {

    let maxLengthInput = -1;
    for (let i = 0; i < data.length; i++) {
      if (data[i].input.length > maxLengthInput) {
        maxLengthInput = data[i].input.length;
      }
    }
  
    for (let i = 0; i < data.length; i++) {
      while (data[i].input.length < maxLengthInput) {
        data[i].input.push(0);
      }
    }
  
    return data;
  }
  
const encode = d => {
    const newArr = [];
    d.split('').map(c => {
        newArr.push((c.charCodeAt(0) / 255))
    });
    return newArr
  }
  
const encodeData = data => {
    return data.map(d => {
        return {
            input:  encode(d.input),
            output: d.output
        }
    });
}
  
const serialize = data => fixLengths(encodeData(data))

/*network.train(serialize(
[ { input: 'I am happy', output: { happy: 1 } },
  { input: 'I feel fine', output: { happy: 1 } },
  { input: 'What a good day!', output: { happy: 1 } },
  { input: 'I am sad', output: { sad: 1 } },
  { input: 'I feel bad', output: { sad: 1 } },
  { input: 'Such a bad day', output: { sad: 1 } } ])
);*/

network.train(serialize(
[ { input: 'I am happy', output: { happy: 1 } },
  { input: 'I feel good', output: { happy: 1 } },
  { input: 'All good mate', output: { happy: 1 } },
  { input: 'So sad', output: { sad: 1 } },
  { input: 'I feel bad', output: { sad: 1 } },
  { input: 'This is bad', output: { sad: 1 } } ])
);

const result = network.run(encode("I am feeling so sad"));
console.log(result);
  