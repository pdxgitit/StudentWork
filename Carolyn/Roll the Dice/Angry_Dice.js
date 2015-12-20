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
    new_roll(die_one, die_two);
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
    dieimg.src = x.num_showing;
    one.appendChild(dieimg);

    var two = document.getElementById('dice_image_two');
    var diceImage = document.createElement('img');
    diceImage.src = y.num_showing;
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
