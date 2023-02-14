function doAddition(x)
{
    return function (y){return x+y};
}

console.log(doAddition(1)); // output : [function (anonymous)]

console.log(doAddition(3)(4)); //curring // output : 7

var add= doAddition(4);
console.log(add);//output : [function (anonymous)]

console.log(add(9)) //output : 13