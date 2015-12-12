

/* We're gonna need:
- list that stores inventory
    - material, price, in_stock
- need function that adds to list
- need function that removes from list
- need function that adds stock of an item
- need function that removes stock of an item
*/

//
// var marker = {
//     color: "maroon",
//     type: "dry erase",
//     ink_level: .5,
//     write: function(text) {
//         console.log(text);
//     }
// };
window.onload = function() {
    document.getElementById("add_item").onclick = addInventoryItem;
};

var inventory = [];

 // constructor functioi for an inventory item

function makeInventoryItem(name, price, in_stock) {
    this.name = name;
    this.price = price;
    this.in_stock = in_stock;
 }

 function addInventoryItem() {
     var name  = document.getElementById("name").value;
     var price = document.getElementById("price").value;
     var in_stock = document.getElementById("in_stock").value;
     var new_item = new makeInventoryItem(name, price, in_stock);

inventory.push(new_item);
console.log(inventory);


}


    //  create new inventory item object
/* list = [wood,corgi,hamster]

   list.unshift(new_thing)
   list.shift

   list.push(new_thing) - IN
   list.pull OUT
   */

    /*add new object to the inventory array
        get the text out of the inputs
        assign each input field's value to a variable
        pass those values to the object constructor
        */

    // Update inventory displayed on web page



// var wood = new makeInventoryItem("wood", 15, true);


 // make inventory to list
