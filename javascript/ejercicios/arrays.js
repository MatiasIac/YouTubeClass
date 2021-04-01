let merge_and_sort = (array1, array2) => array1.concat(array2).sort((a, b) => a - b);

const isSorted2 = (a) => {
    const length = a.length;
 
    if (length <= 1) return true;
 
    let l = 0;
    let r = length - 1;
 
    for (; l < r;) {
 
        if (a[l] > a[l + 1] || a[r] < a[r - 1]) return false;
         
        l++;
        r--;
    }
 
    return true;
};

let isSorted = (array) => {
    const array_length = array.length;
    if (array_length <= 1) return true;

    for (let index = 0; index < array_length; index++) {
        if (array[index] > array[index + 1]) {
            return false;
        }
    }

    return true;
}

const arr = [0, 4, 1, 10, 8, 3, 6];
const arr2 = [2, 41, 11, 9, 7, 5, 12];
const arr3 = merge_and_sort(arr, arr2);

console.log(isSorted2(arr3));















const constructFunction = (steps) => {
    let s = "return ";
     
    for (let index = 0; index < steps; index++) {
        s += `(arr[i * ${index * steps}] > arr[(i * ${index * steps}) + 1]) || `;
    }
 
    s = s.substr(0, s.lastIndexOf(" ||")) + ";";
 
    return new Function("i", "arr", s);
};

const isSorted3 = (a, steps) => {
    if (a.length <= 1) return true;
 
    const partitions = constructFunction(steps);
 
    for (let index = 0; index < steps; index++) {
        if (partitions(index, a) === true) return false;
    }
 
    return true;
};


//arr3.forEach((e) => console.log(e));

let bubbleSort = (inputArr) => {
    let len = inputArr.length;
    let checked;

    do {
        checked = false;
        for (let i = 0; i < len; i++) {
            if (inputArr[i] > inputArr[i + 1]) {
                let tmp = inputArr[i];
                inputArr[i] = inputArr[i + 1];
                inputArr[i + 1] = tmp;
                checked = true;
            }
        }
    } while (checked);

    return inputArr;
 };