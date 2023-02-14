const http = require('http');
//what does the http module ? 
//   http module handels the requests and responses in node js

http.createServer((req,resp)=>
{
    resp.write("<h1>hello this is vishal</>");
    resp.end();
}).listen(4500);


//run this code and open localhost:4500 in chrome
