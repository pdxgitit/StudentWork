/* We're gonna need:
    - a list that stores our inventory
      - material, price, in_stock
    - a function that adds to the list
    - a function that removes from the list
    - a function that adds stock of an item
    - a function that removes stock of an item
*/
var inventory = [];

window.onload = function() {
  document.getElementById('add_inv').onclick = add_new_item;
};


// Check to make sure input cells are not empty
function check_values() {
  if (!document.getElementById('material').value) {
    alert('Material cannot be blank.');
    return (true);
  } else if (!document.getElementById('price').value) {
    alert('Price cannot be blank.');
    return (true);
  } else if (!parseInt(document.getElementById('price').value)) {
    alert('Price must be a number!');
    return (true);
  }
  return (false);
}
// This is a constructor function for an inventory item
function inventory_item (material, price, in_stock) {
  this.material = material;
  this.price = price;
  this.in_stock = in_stock;
}

// This function adds an item to our list
function add_inventory (material, price, in_stock) {
  var new_item = new inventory_item (material, price, in_stock);
  inventory.push(new_item);
}
// This function appends a new item to the html
function append_table (material, price, in_stock) {
  var inv = document.getElementById('inventory'),
      new_tr = document.createElement('tr'),
      mat_td = document.createElement('td'),
      pri_td = document.createElement('td'),
      ins_td = document.createElement('td');
  mat_td.innerText = material;
  pri_td.innerText = price;
  if (in_stock) {
    ins_td.innerText = "Yes";
  } else {
    ins_td.innerText = "No";
  }
  new_tr.appendChild(mat_td);
  new_tr.appendChild(pri_td);
  new_tr.appendChild(ins_td);
  inv.appendChild(new_tr);
}
// This function pulls new item info from our form
function add_new_item (event) {
  var material = document.getElementById('material').value,
      price = '$' + document.getElementById('price').value,
      in_stock = document.getElementById('in_stock').checked;
  if (check_values()) {
    return;
  }
  add_inventory(material, price, in_stock);
  append_table(material, price, in_stock);
  document.getElementById('material').value = "";
  document.getElementById('price').value = "";
  document.getElementById('in_stock').checked = false;
}


// This function removes the first item from our list
