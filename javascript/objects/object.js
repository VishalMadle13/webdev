var user = function(firstName, courseCount) //function
{
    this.firstName = firstName;
    this.courseCount = courseCount;
    this.getCourseCount= function () {
        console.log(`The course count is : ${courseCount}`);
    };
}

console.log(user);  //calling function & get output :  [function user]

var vishal = user("vishal",5);
console.log(vishal);  // gives undefined bcz we are accessing function throgh variable 
//here new keyword is reqired

var vishal = new user("vishal",5);
console.log(vishal);

user.prototype.getFirstname = function()
{
    console.log(`your first name is : ${this.firstName}`);
}

 
vishal.getFirstname();  // calls the getFirstname function

/*
// 

underfined means 
   probably element ptroperty not set
   probably element property not defined
   probably element property never exist
   probably element property never injected nicesly

*/