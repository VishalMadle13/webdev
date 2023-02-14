//for of loop

//array
const names = [ "youtube ","facebook", "instagram","netflix"];

for(const n of names)
{
    console.log(n);
}



// for in loop

//object with name symbols
const symbols = 
{
    yt : "youtube",
    fb : "facebook",
    ig : "instagram",
    nf : "netflix"
}

for(const m in symbols)
{
    console.log(m); // displays only keys in object not values of keys
    console.log(symbols[m]) //displays values in object
}