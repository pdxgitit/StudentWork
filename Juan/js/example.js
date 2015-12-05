function reverseString(str) {
  var i,
      final = str.slice(-1);
  for (i = -2; i >= 0 - str.length; i -= 1) {
    final += str.slice(i, i + 1);
  }
  return final;
}

reverseString("hello");

function factorialize(num) {
  if (num > 1) {
    return (num * factorialize(num - 1));
  }
  return(1);
}

factorialize(5);

function palindrome(str) {
  var str1 = str.replace(/\W+/g, "").toLowerCase()
      str2 = str1.split('').reverse().join('');
  console.log(str1);
  console.log(str2);
  if (str === str2){
    return true;
  } else {
    return false;
  }
}



palindrome("eye");
palindrome("haughty");
