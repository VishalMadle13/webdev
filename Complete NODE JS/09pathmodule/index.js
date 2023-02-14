const fs = require('fs');
const path = require('path');

const dirPath = path.join(__dirname,'files');
console.warn(dirPath)
//
//creating the five files
// for(let i=0; i<5; i++)
// {
//     fs.writeFileSync(dirPath+`/hello${i}.txt`,"this is a simple file")
// }

//
//  reading the files
// fs.readdir(dirPath,(err,files)=>
// {
//     console.log(files);   //files is an array
// }); // gives file in the array

// if we dont want file in array the we use foreach statement
fs.readdir(dirPath,(err,files)=>
{
    files.forEach(item => {
        console.log(item);
    });
})

