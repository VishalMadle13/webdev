console.log("hello world 1");
Name="vishal";
console.log(Name[2]);

function myApp()
{   const myVar="value1";
    function myfunc()
    {
        const myVar="value2";
        console.log("inside myFunc",myVar);
    }
    // const myfunc2=function(){ }
    // const myfunc3=()=>{}
    console.log(myVar);
    myfunc();
}

myApp();



//  map Method
//  printing squares of numbers in array by map method
const num = [3,4,6,1,8];
const square= function(num)
{
    return num*num;
}
const squareNumber = num.map(square);
console.log(squareNumber);

// Filter Method
// finding even nums in aray by filter method
//for even
const numbers1=[1,3,2,6,4,8];
const isEven =function(numbers1)
{
    return numbers1%2==0;
}
const evenNumbers= numbers1.filter(isEven);
console.log("Even numbers ",evenNumbers);
//for odd
const isOdd= function(numbers1)
{
    return numbers1%2!==0;
}
const oddNumbers=numbers1.filter(isOdd);
console.log(oddNumbers);

// Reduce Method
//sum the all numbers in array

const num1=[1,2,3,4,5];
const sumAll=num1.reduce((accumulator,currentValue)=>
{
    return accumulator+currentValue;
})
console.log(sumAll);