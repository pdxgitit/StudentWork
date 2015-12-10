function greeting(name){
 var first_letter = name.charAt(0).toUpperCase();
 var rest_of = name.slice(1).toLowerCase();
 return("Hello "+ first_letter +rest_of + "!");
}
console.log(greeting("Doug"));
console.log(greeting("doug"));
console.log(greeting("DoUg"))
