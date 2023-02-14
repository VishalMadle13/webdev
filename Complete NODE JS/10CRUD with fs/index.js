const fs = require('fs');
const path = require('path');
const dirPath =path.join(__dirname,'crud');

// ** Creating file
// fs.writeFileSync(dirPath+'\ apple.txt',"this is simple txt file")
//alternative for above
const filePath = `${dirPath}/apple.txt`;
fs.writeFileSync(filePath,"this is simple file")

// // ** REading the files
// fs.readFile(filePath,'utf8',(err,item)=>{
//     console.log(item);
// });

// // ** Updating the dile
// //-append data

// fs.appendFile(filePath," and the file name is apple.txt",(err)=>
// {
//     if(!err)
//     {
//         console.log("File updated successfully")
//     }
// });

// //-rename file
// fs.rename(filePath,`${dirPath}/fruit.txt`,(err)=>
// {
//     if(!err)
//     {
//         console.log("file updated successfully!")
//     }
// })


// ** Delete file

// fs.unlinkSync(`${dirPath}/fruit.txt`,(err)=>
// {
//     if(!err)
//     {
//         console.log("file deleted successfully!")
//     }
//     else{console.log("err")}
// })