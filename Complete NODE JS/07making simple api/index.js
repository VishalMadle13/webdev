const { ok } = require('assert');
const { createDecipheriv } = require('crypto');
const http = require('http');
const data = require('./data');

http.createServer((req,resp)=>
{
   resp.writeHead(200,{'content-Type':'application\json'})
   resp.write(JSON.stringify(data));
   console.log("its running");
   resp.end();

}).listen(4300);



// first parameter of writeHead is the status 
// //  for
//    200    ok
//    201    created
//    404    not found
//    500    internal server error