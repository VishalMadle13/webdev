const red = document.querySelector(".red");
const cyan = document.querySelector(".cyan");
const violet = document.querySelector(".violet");
const orange = document.querySelector(".orange");
const pink = document.querySelector(".pink");
const music = new Audio('tone.mp3');


const center = document.querySelector(".center"); 

// console.log(window.getComputedStyle(red).backgroundColor);
// gives the background color of red class 

const getBGcolor = (selectedElement)=>
{
    return window.getComputedStyle(selectedElement).backgroundColor;
}

//gives the background color of cyan element 
console.log(getBGcolor(cyan));

var color = getBGcolor(red);

//on clicking pink class (pink element) background color of center will be changed
// pink.addEventListener("click",()=>{
//     center.style.background= color;
// }) 

// red.addEventListener("click",()=>{    //similarly for red area 
//   console.log(color);  
//   center.style.backgroundColor=color;
// });

const colorChanger=(Element)=>
{
    return Element.addEventListener("click",()=>{
        center.style.backgroundColor=getBGcolor(Element);
        music.play();
    });
};

colorChanger(orange)
colorChanger(red)
colorChanger(pink)
colorChanger(violet)
colorChanger(cyan)


