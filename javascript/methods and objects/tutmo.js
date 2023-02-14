var users={
    firstName : "vishal",
    lastName  : "madle",
    role : "admin",
    loginCount : 5,
    codeChefSingIn : true, 
    courseList : [],
    byCourse : function (courseName)
    {
        this.courseList.push(courseName);
        return `${courseName} course is added in your courses`;
    },
//return `${this.firstName} is enrolled in total of ${this.courseList.length} courses `;
}

console.log(users.firstName);
console.log(users.byCourse("cpp"));
console.log("courseList : " ,users.courseList);



