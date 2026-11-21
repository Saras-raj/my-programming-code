alert("javaScript chal raha hai!");
console.log("hello rahul")
let name = "rahul";
console.log("welcome to my coding,rahul");
let fullname="rahul";
let FULLNAME="RITESH";
console.log(fullname);
console.log(FULLNAME);
fullname="rahul";
_fullname="rahul";
$fullname="rahul";
console.log("fullname");
let age = "22";
let price = "20000";
console.log(age);
console.log(price);
const PI = 3.14
console.log(PI);
let age1 = 35;
let age2 = "47";
console.log(typeof age1);
console.log(typeof age2);
fullname="manish";
console.log(typeof fullname);
isFollow =true;
console.log(typeof isFollow);
let x = BigInt("123");
let y = Symbol("Hello!");
console.log(x);
console.log(typeof x);
console.log(y);
console.log(typeof y);
// This code of print of hello world
console.log("hello world");
//Artimetic opertaors
let a = 5;
let b = 2;
console.log("a = ", a, " & b=",b);
console.log("a+b=",a+b);
console.log("a-b=",a-b);
console.log("a*b=",a*b);
console.log("a/b=",a/b);
console.log("a%b=",a%b);
console.log("a**b=",a**b);

console.log("a++=",a++);
console.log("a=",a);
console.log("a--=",a--);
console.log("a=",a);
a+=4;
console.log("a=",a);
b-=4;
console.log("b=",b);
//Comparison operator

console.log("5==2",a==b);
 












//ARRAYS
let marks=[96,97,55,44];
console.log(marks);
console.log(marks.length);

//Using for loop Arrays

let heroes = ["ironman","balbeer","spiderman","batman"];
for (let i = 0; i < heroes.length; i++){
    console.log(heroes[i]);
}
//types of Arrays 
let foodItem =["banana","rice","burger","apple"]
foodItem.push("patties","mango","curd")
console.log(foodItem);
















//FUNCTION IN JS
function myfunction (){
    console.log("welcome to my home");
    console.log("we are learning js");


}
myfunction();
myfunction();
let arr = [1,2,3,4,5]
arr.forEach(function printval(val){
console.log(val);
})
 arr = ["bihar","delhi","pune"]
arr.forEach((val,idx) => {
    console.log(val);

});
//filter method
 arr = [1,2,3,4,5];
let evenarr = arr.filter((val) => {
    return val % 2 ===0;
})
console.log(evenarr);

//DOM
let heading= document.getElementById("header");
console.log(heading);
//query selector
let firstelement = document.querySelector("p");
console.log(firstelement);
//query slector
let allelement=document.querySelectorAll("p")
console.log(allelement);

//event

//synchronous Program
console.log("one");
console.log("two");
console.log("three");
//Asynchronous program
console.log("one");
console.log("two");
console.log("three");
function hello(){
    console.log("hello");
}
setTimeout(hello,5000);
console.log("four");
console.log("five");
//callback
function sum(a,b){
    console.log(a+b);
}
function calculator(a,b,sumcallback){
    sumcallback(a,b);
}
calculator(1,2,sum);

function getData(dataId, getNextData){
    //2s
    setTimeout(() => {
        console.log("data",dataId);
        if (getNextData){
            getNextData();
        }

    },2000);
}
//callback hell
getData(1,() =>{
    getData(2,() =>{
        getData(3,() => {
            getData(4);

        });
    });
});

//Promises
let Promises= new Promise((resolve,reject)=>{
    console.log("i am a promise");
});

// Asynic-await
async function hello(){
    console.log("hello");
}