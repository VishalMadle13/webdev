// input taken in terminal as
//  node index.js __input__
// and stored and displayed in the form of array
// in put content start form index 2 i.e. third element
 
 
 
 console.log(process.argv);
// In terminal if we write as follows
//  node .\08input from commandline\\index.js hello
// it gives array of 
// [
//     'C:\\Program Files\\nodejs\\node.exe',
//     'S:\\VS CODE\\Complete NODE JS\\08input from commanline\\index.js',
//     'hello'
// ]

//
//for 
 console.log(process.argv[2])
// gives the value in array whose index is 2  ...[0,1,2]

// creating the file from terminal input

const fs = require('fs');  //filesystemmodule imported

const input = process.argv;  // gives array 

// fs.writeFileSync(input[2],input[3]);  // in array  at index 2 filename and at index 3 fileContent is allowed in input
// //ex 
// // apple.txt -> input[2]
// // this is a fruit -> input[3]



// making more complex above example by adding add/remove for file 
//
//now here input[2] for add/remove
//         input[3] for fileName
//         input[4] for fileContent

if(input[2]=='add')
{
    fs.writeFileSync(input[3],input[4]);
}
else if(input[2]=='remove')
{
    fs.unlinkSync(input[3]);
}

else
{
    console.log("invalid input");
}
