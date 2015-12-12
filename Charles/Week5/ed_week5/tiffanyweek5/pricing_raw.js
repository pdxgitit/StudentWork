/* we are going to need:
 - list that stores our inventory
    -material, price, in-stock
 - function that adds to the list from a form
 - function that can remove from the list

 */
window.onload = function() {
  document.getElementById("add_item").onclick = addinventoryitem;
};


 var inventory = [];
 // constructor function for an inventory item

// dont add the () after function for event listenr
 function makeinventoryitem(name, price, in_stock) {
   this.name = name;
   this.price = price;
   this.in_stock = in_stock;
 }



 //add inventory item to list
 function addinventoryitem() {
var name = document.getElementById("name").value;
var price = document.getElementById("price").value;
var in_stock = document.getElementById("price").value;

var generic = new makeinventoryitem(name, price, in_stock);


inventory.push(generic);
console.log(inventory);

// create new inventory item object

// add new object to the inventory array

//update inventory displayed on web page
 }
