/**
* Carolyn, it looks like the error you were getting says that you're trying to
* GET a file called "undefined", which doesn't exist. Since both your HTML and
* Javascript files are loading, I figured it must be an image file that you're
* trying to access. But somewhere along the way, the file name didn't make it
* into your new_roll function and ended up putting undefined into your image src
* instead of an actual file name.
* I changed three things:
* - I think you meant to pass dice_one and dice_two into the new_roll function,
*   instead of die_one and die_two. Since you're already calling x.num_showing
*   inside new_roll, passing die_one/two (which is already the result of calling
*   num_showing) didn't make sense.
* - I added parentheses to every call to num_showing (e.g "num_showing()").
*   Because it's a method, which is just a function, you have to put parentheses
*   after the name to actually call it.
* - I added a return statement to num_showing, so that the function actually
*   returns the filename. Everything inside the function is destroyed when the
*   function ends, unless you return something. A function without a return
*   statement will return undefined! So, that was a big part of the problem.
*
*   Your next steps should be: find everywhere your calling a method and make
*   sure you have parentheses after it. Does your num_showing method do what you
*   intended? or rather, is that a good name for it? Right now it returns a
*   different random number each time you call it. That sounds like rolling the
*   dice to me.
*   Everywhere you use snake_case names should be camelCase instead. Python uses
*   snake_case_variable_names and Javascript uses camelCaseNames.
*
*   Document your code with comments above each function and global variable!
*/

window.onload = function() {
};
var dice_one = new CreateDice();
var die_one = dice_one.num_showing;
var dice_two = new CreateDice();
var die_two = dice_two.num_showing;

var el = document.getElementById('Save_die_one');
  el.addEventListener('click', function(){
    Save_die(die_one);
  }, false);

var elem = document.getElementById('Save_die_two');
  elem.addEventListener('click', function(){
    Save_die(die_two);
  }, false);

var ellie  = document.getElementById('ROLL');
  ellie.addEventListener('click', function(){
    new_roll(dice_one, dice_two);
  }, false);

var dice = ["1.png", "2.png", "angry.png", "4.png", "5.png", "6.png"]

function CreateDice() {
  this.num_showing = function(){
    rolled_dice = []
      if(this.held === false) {
        for(var i=1; i>0; i--){
          var num = Math.random();
            num = Math.floor(num*5);
            num = num+0;
        rolled_dice.push(dice[num]);
    };
    };
    return rolled_dice[0];
  };
  this.held = false;
};

function Save_die(x) {
  if(this.num_showing === '6.png'){
    this.held = false;
  }
  else {
    this.held = true;
  }
};

function new_roll(x, y) {
    var one = document.getElementById('dice_image_one');
    var dieimg = document.createElement('img');
    dieimg.src = x.num_showing();
    one.appendChild(dieimg);

    var two = document.getElementById('dice_image_two');
    var diceImage = document.createElement('img');
    diceImage.src = y.num_showing();
    two.appendChild(diceImage);
};
//   document.getElementById("ROLL").onclick = rollDice;
//   // document.getElementById('Save_die_one').onclick = Save_dice;
// };
//
//
// // function Save_die(){
// //
// // };
//
// function rollDice(){
//   rolled_dice = []
//     for(var num_of_dice = 1; num_of_dice > 0; num_of_dice --) {
//       var num = Math.random();
//         num = Math.floor(num*5);
//         num = num+0;
//       rolled_dice.push(dice[num]);
//     }
//     printingDice(rolled_dice);
//     // console.log(rolled_dice[0]);
// };
//
// function printingDice(rolled_dice){
//   var die_one = rolled_dice[0];
//   console.log(die_one);
//     var die_img_one = document.getElementById('dice_image_one');
//     // die_img_one.appendChild(die_one);
//   var die_two = rolled_dice[1];
//   console.log(die_two);
//     var die_img_two = document.getElementById('dice_image_two');
//     // die_img_two.appendChild(die_two)
//   var sum_of_dice = (die_one + die_two)
//
//   Stage_One(sum_of_dice);
//   };
//
// function Stage_One(sum_of_dice){
//   if(sum_of_dice === 3 ){
//     document.write('Stage One COMPLETE!')
//   }
// };
//
// function Dice(FirstDice, SecondDice, Stage){
//   this.FirstDice = die_one;
//   this.SecondDice = die_two;
//   this.Stage = Stage;
// };
