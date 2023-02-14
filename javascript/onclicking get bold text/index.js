 //1.print in javascript
 console.log("hellow world");
 document.write("this is doccument ");
 //  alert("alert");

 //2.javascript console api
 console.warn("this is warning");
 console.error("this is error");

// 3. javascript variable
//What are the variables ?
//-->containers to store data values.
var num1 = 32;
var num2 = 54;
console.log(num1+num2);

// 4. DataTypes in javascript 
  // String
var str1="this is a string";
  // Number
var num3= 324;
  // object
var marks={ravi:43,shubham:34,harry:45}
  // Booleans
var a=true;
var b=false;
console.log(a,b)

var sd; //...>print undefined  because value is not assigned
console.log(sd)

var n= null;
console.log(n)



/*
At a very high level
there are two types of datatypes in javascript 
   1. Primitive data types :
       unndefined, null , niumber, String ,boolean,symbol
   2. Reference data types :
       Arrays and objects

*/

var arr =[1,2,3,4,5];
console.log(arr)
console.log(arr[2])

var arr2 = [1,2, "three",4, 5]
console.log(arr2);
console.log(arr2[2])


// 5. Operators in javascript

var a=34;
var b=43;
console.log("The value of a + b ",a+b);
console.log("The value of a - b ",a-b);
console.log("The value of a * b ",a*b);
console.log("The value of a / b ",a/b);

// 6. Assignment operator
var c=b;

console.log(c+=2);
console.log(c-=2);
console.log(c*=2);
console.log(c/=2);

// 7. Comparison operator
var x=24;
var y=14;
console.log("7. Comparison operator x=24 y=14");
console.log(x==y);
console.log(x>=y);
console.log(x<=y);
console.log(x!=y);
console.log(x>y);
console.log(x<y);

// 8. Logical Operator
console.log("8. Logical Operator")
//and
console.log(true&&true)
console.log(true&&false)
console.log(false&&true)
console.log(false&&false)
//Or
console.log(true||true)
console.log(true||false)
console.log(false||true)
console.log(false||false)
//not
console.log(!true)
console.log(!false)


// 9. Functions
function avg(a,b)
{
    return (a+b)/2;
}
c1= avg(4,6);
c2= avg(14,24);
console.log(c1,c2);

// 10. Conditionals in javascript
var age =23;
// if-else statement
if(age<8)
{
    console,log("You are a kid")
}
else
{
    console.log("You are not kid")
}
   // if-else Ladder
   //---->if-else if -else if -else

// 11. Loop

var arr3=[1,2,3,4,5,6]
  //for
  for(var i=0; i<arr3.length; i++)
  {
    console.log(arr3[i]);
  }
   //forEach
   arr3.forEach(function(element)
   {
    console.log(element)
   })
   //while
   let j=0;
   while(j<arr3.length)
   {
    console.log(arr3[j]);
    j++;
   }
   //do while
   do{
    console.log(arr3[j]);
    j++;
   }
   while(j<arr3.length);    
   
/* in array
   
   .pop()- delete last element in array
   .push("x")- add element in array
   .shift()- remove first element
   .unshift()-add element at first place

   ex. arr.pop();
*/


// 12. String methods in javascript
let myString = "Vishal is goood boy";
console.log(myString.length);
console.log(myString.indexOf("good"));
console.log(myString.lastIndexOf("good"));
console.log(myString.slice(1,4));
d= myString.replace("vishal","rohan");
console.log(d);

let myDate = new Date();
console.log(myDate)
console.log(myDate.getTime);
console.log(myDate.getFullYear)
console.log(myDate.getDay)
console.log(myDate.getMonth)
console.log(myDate.getHours)
 

// 13.  DOM Manupulation
let elem= document.getElementById('click');
console.log(elem);

let elemClass = document.getElementsByClassName('container');
console.log(elemClass);
 
//elemClass[0].style.background="yellow";
elemClass[0].classList.add("bg-primary");//adds the class 
elemClass[0].classList.add("text-success");
//elemClass[0].classList.remove("text-success"); //remove the class

console.log(elem.innerHTML);
console.log(elem.innerText);

console.log(elemClass[0].innerHTML);
console.log(elemClass[0].innerText);

tn = document.getElementsByTagName('div');
console.log(tn);

createdElement=document.createElement('p');
createdElement.innerText="This is a created para";
tn[0].appendChild(createdElement);

createdElement2= document.createElement('b');
createdElement2.innerText= "This is a created bold";
tn[0].replaceChild(createdElement2,createdElement);


console.log("document title : ",document.title);
console.log("document URL : ",document.URL);
console.log("document script : ",document.scripts);
console.log("document links : ",document.links);
console.log("document images : ",document.images);
console.log("document domain : ",document.domain);


// 14. selecting using query 
sel = document.querySelector('.container');
console.log(sel);
sel=document.querySelectorAll('.container');
console.log(sel);


//function for click me button
function clicked()
{
    console.log('the button is clicked');
}
window.onload=function()
{
    console.log('the document was loaded');
}

// 15. Events in javaScript
// firstContainer.addEventListener('click',function(){
//     console.log("clicked on container");
// });
// firstContainer.addEventListener('mouseover',function(){
//     console.log("mouse on container");
// });
// firstContainer.addEventListener('mouseout',function(){
//     console.log("mouse out of container");
// })
// firstContainer.addEventListener('mouseup',function(){
//     console.log("mouse up when clicked on container")
// })
// firstContainer.addEventListener('mousedown',function(){
//     console.log("mouse down  when clicked on container")
// })

firstContainer.addEventListener('click',function(){
    document.querySelectorAll('.container')[1].innerHTML="<b> We have clicked</b>"
    console.log("clicked on container");
});

let prevHTML = document.querySelectorAll('.container')[1].innerHTML;
firstContainer.addEventListener('mouseup',function(){
    document.querySelectorAll('.container')[1].innerHTML=prevHTML;
    console.log("mouse up when clicked on container")
})
firstContainer.addEventListener('mousedown',function(){
    document.querySelectorAll('.container')[1].innerHTML="<b> We have clicked</b>"
    console.log("mouse down  when clicked on container");
})

// //ARROW Function
// sum=(a,b)=>{ return a+b; };
// //simple function 
// function sum(a,b){ return a+b ;};

logkaro=()=>{
    document.querySelectorAll('.container')[1].innerHTML="<b>Set interval fired</b>"
    console.log("I am your log");
  }


// 16. SetTimeout and Setinterval
 //setTimeout(logkaro, 2000);//logkaro function will call after 2 sec
 //clr= setInterval(logkaro, 2000);//logkaro function repeatedly called after 2 sec
 
 //for stoping the set interval we use 
 //  clearInterval(clr);
  

// 17. loacalStorage 
localStorage.setItem('name','vishal')
localStorage
localStorage.getItem('name');

// 18. JSON  JavaScript Object Nootation 
obj = {name: "vishal",length: 1};
jso = JSON.stringify(obj);
console.log(typeof jso);
console.log(jso);
 



 

 