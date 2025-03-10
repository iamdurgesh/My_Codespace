let A = "This is a separate file"


console.log(A)
// 1. Javascript Variables (Var, let & const)
var num1 = 34
var num2 = 43
console.log (num1+num2 )

// 2.  Datatypes in javascript Primitive : (number, string, boolean, undefined, null), Reference: (Objects, arrays)
 // Object
var obj = {
    num : 23,
    string : "String",
    boolean : true,
}
console.log(obj)

// Arrays:

var arr = [1,2,3,4,5,6]

// 3. Operators
// Arithmatic operators
var a = 99;
var b = 9;

// console.log("The value of a + b = ", a + b)
// console.log("The value of a - b = ", a - b)
// console.log("The value of a / b = ", a / b)
// console.log("The value of a * b = ", a * b)

// Assignment operators:
var c = b;
// console.log(c)
// c += 10;
// c -= 10;
// c *= 10;
// c /= 10;
// console.log(c)

// Comparision operators
console.log(a == b)
console.log(c == b)

//4.  Functions & Scope: -------------------------------------------------

// a. Function Declaration
function greet(name) {
    return `Hello ${name}`;
}
console.log(greet("babu"))

// b. Function Expression
const greeting = function(name){
    return `Hello ${name}`;
}


console.log(greeting("Aristotle"));

// Arrow function

const greetings = (name) =>`Hallo this is an ${name} Function `;
console.log(greetings("Arrow"));

// Closure: A closure is formed when an inner function references variables from its outer function even after that outer function has returned.

function outer() {
    let count = 0;
    return function increment(){
        count++;
        console.log(count);
    };
}

const counter = outer();
counter(5);
counter(8);

// 5. Objects and Prototypes

// A. Obkect Literal
const person = {
    name: "Alice",
    age: 25,
    greet: function() {
      console.log(`Hi, I am ${this.name}`);
    }
  };
  person.greet(); 

// 6. Arrays and Common methods

const car = ["BMW", "saab", "Honda", "Volvo", "VW"];

const semi_car = car.slice(0,4)

// Using Map to store employee information
let employeeMap = new Map();
employeeMap.set('John', { age: 30, department: 'IT' });
employeeMap.set('Alice', { age: 35, department: 'HR' });

let employeeObject = {
    John : {
        age : 30, 
        department : "IT",
    },
    Alice: {
        age : 33,
        department : "HR",
    }
}

console.log("This employeeObject is : ", employeeObject)

// Accessing employee information using Map
console.log("Employee information using Map:");
console.log(employeeMap.get('John')); 
console.log(employeeMap.get('Alice')); 

// Classes in Javascript 

class Person {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
    greet() {
      console.log(`Hello, I'm ${this.name}`);
    }
  }
  const alice = new Person("Alice", 25);
  alice.greet();


