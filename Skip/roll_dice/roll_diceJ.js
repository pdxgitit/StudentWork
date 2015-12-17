// create a variable call "dice" (= *.png)
// create eventListener (or onclick) for "roll" button
// create function that returns random types of dice related to
//      number in field
// create function that creates necessary rows to accommodate the
//      amount of dice to display

// math.random is built-in


window.onload = function() {
    document.getElementById("roll").onclick = makeRoll;
};

var dice = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"];
// var imageFolder = images/'' ;
// var imgsrc = imageFolder +'';

function makeRoll(roll) {
    this.roll = roll;
var num = document.getElementById("dice");
var choice = num.value;

// console.log(choice);

var box = [];

for (i=0; i<choice; i++) {
    var Dec = Math.random();
    var ranNum = Math.floor(Dec * 5);
    ranNum = (ranNum + 1);

    var fileName = dice[ranNum];
    box.push(fileName);

    //  console.log(box);
    // console.log(temp);
}
for(var i =0; i < choice; i++) {
    addrow(box);
}
 };


function addrow(box) {
var table = document.getElementById("dice_spread");
var row = table.insertRow();
var cell1 = row.insertCell();
var cell2 = row.insertCell();
var cell3 = row.insertCell();
var cell4 = row.insertCell();
var cell5 = row.insertCell();
var cell6 = row.insertCell();

cell1.innerHTML = "<img  src=images/" + box[0]+">";
cell2.innerHTML = "<img  src=images/" + box[1]+">";
cell3.innerHTML = "<img  src=images/" + box[2]+">";
cell4.innerHTML = "<img  src=images/" + box[3]+">";
cell5.innerHTML = "<img  src=images/" + box[4]+">";
cell6.innerHTML = "<img  src=images/" + box[5]+">";

box.splice(0, 6);
}



//
// updateList()
// addrow(temp)
//     }
// };

// document.getElementById("submit").onclick = randomnumber;
// };
//
//
// //function that takes in number of dice requested upon submittal and spits out random numbers 1-6
// function randomnumber () {
// var dicenumber = document.getElementById("dicenumber").value;
// var dicelist = []
//
// for (var i=0; i < dicenumber; i++) {
// var rando = Math.random();
// rando = Math.floor(rando * 6);
// rando = rando + 1;
// dicelist.push(rando);
// }
// updateList()
// addrow(dicelist)
// };
//
// function updateList() {
// document.getElementById("Dice").innerHTML = "";
