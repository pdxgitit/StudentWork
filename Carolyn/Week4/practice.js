function reverseString(str) {
  var doug = str.split("");
  var leo = doug.reverse();
  var abby = leo.join("");
  return (abby);
}

console.log(reverseString("hello"));

function factorialize(num) {
  var num1 = 1
  for(var i = 5; i > 0; i-=1) {
    num1 = i * num1;
  }
  return num1
}

console.log(factorialize(5));
