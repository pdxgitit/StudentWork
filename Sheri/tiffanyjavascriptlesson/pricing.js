/* We're gonna need:
  -list that stores our inventory
    - for each item
    - material
    -price
    -is it in stock
  -a function that adds to the list
  - a function that removes from the list
  - a function that adds stock
  - a function that removes stock of an item
  */

  // first thing: make an array that will store a list of objects for every item in our store
  //add event listener add it here because we want a window onload event
  //this is an anon button find it in dom by using its name we don't need getelementby
window.onload = function() {
    document.getElementById('add_button').onclick = addInventoryItem;
  } //normally youdon't use () because it will call the function instead of asssigning it

var inventory = [];

//define our object definition by making a constructor
//this is a constructor function for an inventory item

function makeInventoryItem(name, price, in_stock) {
  this.name = name;
  this.price =price;
  this.in_stock = in_stock;
}

// add inventory to the list
function addInventoryItem() {
  //create new Inventory object
  //get text out of the inputs
  //assign each input field's value to a variable
  //pass those valuse to the object constructor
  var name = document.getElementById('name').value;
  var price = document.getElementById("price").value;
  var in_stock = document.getElementById("in_stock").value;
  var newer_item = new makeInventoryItem(name, price, in_stock);
  //add new object to the inventory array
  inventory.push(newer_item);
  console.log(inventory);

  //update inventory displayed on web page
}
