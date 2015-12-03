// use alt+R to run on Linux
// use control+R to run on Windows

var p = console.log;

var add = function(x,y) {
  return x+y;
};

console.log(add(3,9));

var test_if = function(n) {
  if (n < 3){
    console.log("little");
  } else if (n === 8) {
    console.log("it's 8");
  } else  {
    console.log("big but not 8")
  }
};

test_if(1);
test_if(4);
test_if(8);

console.log(1/0);

var person = {
    "name": "Ollie"
  , "hobby": "danger"
  , "dob": "1970-11-23"
  , "shout": function () {
               console.log("my name is", this.name + "!")
             }
  , "foo": "bar"
};

console.log(person);
person.shout();

p(person["dob"]);
p(person.foo);

p("\n/* keys -> values in person object: */")
for (var k in person) {
  p(k, '->',  person[k]);
}
