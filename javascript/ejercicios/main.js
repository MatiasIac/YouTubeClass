function configurar(i) {
    setTimeout(function () {
        console.log(`Index: ${i} - element: ${arr[i]}`);
    }, 3000);
}

var arr = [10, 12, 15, 21];

for (var i = 0; i < arr.length; i++) {
    //configurar(i);
    setTimeout(function () {
        console.log(`Index: ${i} - element: ${arr[i]}`);
    }, 3000);
}