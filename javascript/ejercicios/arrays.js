const arr = [0, 4, 1, 10, 8, 3, 6];
const arr2 = [2, 41, 11, 9, 7, 5, 12];

let merge_and_sort = (array1, array2) => array1.concat(array2).sort((a, b) => a - b);

const arr3 = merge_and_sort(arr, arr2);

arr3.forEach((e) => console.log(e));

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