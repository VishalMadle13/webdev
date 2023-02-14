

console.log("start executing.....");
setTimeout(() => {
    console.log("logic executing.....");
}, 2000);
console.log("Complete Execution....");

//
// //  : ** output
// start executing.....
// Complete Execution....
// logic executing.....

// adv : code completely run faster

// Drawback

a = 10;
b = 0;       // .....first part

setTimeout(() => {
    b = 30;
}, 1500);        // ........middle part

console.log(a+b)   // ;.......last part

// output : 10
// this is drawback we did not get 30
