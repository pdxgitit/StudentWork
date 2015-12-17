// Angry dice
/*
List of components:
  Die object constructor
  Game object
  Populate HTML roll space function
  Roll button click handler
  IMG element click handler
*/

// Die object constructor
function die() {
  this.held = false;
  this.val = 0;
  // change the value if die is not held
  this.roll = function () {
    if (this.held) {
      return;
    }
    this.val = Math.floor(Math.random() * 6) + 1;
  };
}

// Game object constructor
function game(dice){
  // stage will be 1, 2, or 3
  this.stage = 1;
  // dice will be an array of two die objects
  this.dice = dice;
  // table defining valid holds for each stage
  this.validHolds = {
    1 : [1, 2],
    2 : [2, 3],
    3 : [5]
  };
  // table defining pass conditions for each stage
  this.winStates = {
    1 : [[1, 2], [2, 1]],
    2 : [[2, 3], [3, 2]],
    3 : [[5, 6], [6, 5]]
  };
  // function to hold a specific die
  this.hold = function (die_index) {
    var clickedDie = this.dice[die_index].val,
        validStageHolds = this.validHolds[this.stage];
    // check to make sure the die has a value that can be held in this stage
    if (clickedDie === validStageHolds[0]
    || clickedDie === validStageHolds[1]) {
      this.dice[die_index].held = true;
    }
  };

  // function to reset hold state of both dice
  this.resetHold = function () {
    this.dice[0].held = false;
    this.dice[1].held = false;
  };

  // function to roll both dice in the dice array
  this.roll = function () {
    this.dice[0].roll();
    this.dice[1].roll();
  };

  // function to evaluate the state of the game object
  this.evalState = function () {
    var diceArray = [this.dice[0].val, this.dice[1].val],
        winState = this.winStates[this.stage];
    // if 2 angry dice
    if (diceArray === [3, 3]) {
      // reset to stage 1
      this.stage = 1;
      // reset held condition
      this.resetHold();
      // empty dice area
    } else if (diceArray === winState[0] || diceArray === winState[1]) {
    // else if passing conditions
      // if stage 3
      if (this.stage === 3) {
        // win!
      } else {
        // advance stage
        this.stage += 1;
        // reset held condition
        this.resetHold();
      }
    }
  };
}

// Function to populate HTML


// Function to handle roll button click


// Function to handle IMG element click

// Initialize the game object
// Add event listeners
