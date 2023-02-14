var counter = document.querySelector(".followers");
var followers = document.querySelector(".text");

// counter.innerHTML = 1;

let count = 9000;
setInterval(()=>{
    if(count<10000)
    {
        count++; counter.innerHTML=count;
    }
    },1); 

setTimeout(()=>{followers.innerHTML="followers on instagram!"},4000);    
