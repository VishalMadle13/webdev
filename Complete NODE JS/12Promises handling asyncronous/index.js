/*
a = 10;
b = 0;       // .....first part

setTimeout(() => {
    b = 30;
}, 1500);        // ........middle part

console.log(a+b)   // ;.......last part
 */

//handling above problem
let a = 10;
let b = 0;

let waitingData = new Promise((resolve,reject)=>
{
    setTimeout(() => {
        resolve(30);
    }, 1500);
})


waitingData.then((Data)=>
{
    b=Data;
    console.log(a+b);
})