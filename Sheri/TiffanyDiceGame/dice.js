//make a function for the form
//make an event listener for when someone enters something in the field and clicks enter
window.onload = function() {
    document.getElementById('roll').onclick = displayDice;
};

//we need variables for the dice:
var die1 = "1.png";
var die2 = "2.png";
var die3 = "3.png";
var die4 = "4.png";
var die5 = "5.png";
var die6 = "6.png";

/*we're going to need a function that creates html elements with id's for each dice.
We'll might need a global list to keep the id's for each dice, at least if I do the
bonus of keeping all the dice up and re-rolling a subset.

/*make a function that randomizes the number on each die
and corelates each number to its png and displays it.
*/
// this is a dice function in JavaScript
var die_value = function();
    value = Math.random();
    value = Math.floor(die_value * 6);
    value = value + 1;

    }
