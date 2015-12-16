/* We're gonna need:
    - a list that stores our inventory
      - material, price, in_stock
    - a function that adds to the list
    - a function that removes from the list
    - a function that adds stock of an item
    - a function that removes stock of an item
*/
var inventory = [];
inventory[0] = 0;

window.onload = function() {
  document.getElementById('add_inv').onclick = add_new_item;
  document.getElementById('add_stock').onclick = add_stock;
  document.getElementById('remove_stock').onclick = remove_stock;
  document.getElementById('remove_inv').onclick = remove_items;
};

// Unique id generator to uniquely identify list items
function id_gen() {
  inventory[0] += 1;
  return (String(inventory[0]));
}
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
function inventory_item (material, price, in_stock, uid) {
  this.material = material;
  this.price = price;
  this.in_stock = in_stock;
  this.uid = uid;
}

// This function adds an item to our list
function add_inventory (material, price, in_stock, uid) {
  var new_item = new inventory_item (material, price, in_stock, uid);
  inventory.push(new_item);
}
// This function appends a new item to the html
function append_table (material, price, in_stock, uid) {
  var inv = document.getElementById('inventory'),
      new_tr = document.createElement('tr'),
      chk_td = document.createElement('td'),
      chk_bx = document.createElement('input'),
      mat_td = document.createElement('td'),
      pri_td = document.createElement('td'),
      ins_td = document.createElement('td');
  // assign unique id to manipulate new items later
  new_tr.id = uid;
  // create a new check box element with appropriate values
  chk_bx.setAttribute('type', 'checkbox');
  chk_bx.setAttribute('name', 'select_item');
  // add the check box to the check box td
  chk_td.appendChild(chk_bx);
  // set up the value fields
  mat_td.innerText = material;
  pri_td.innerText = price;
  // check whether item is in stock to determine cell contents
  if (in_stock) {
    ins_td.innerText = "Yes";
    ins_td.classList.add('true');
  } else {
    ins_td.innerText = "No";
    ins_td.classList.add('false');
  }
  // add all items to the row
  new_tr.appendChild(chk_td);
  new_tr.appendChild(mat_td);
  new_tr.appendChild(pri_td);
  new_tr.appendChild(ins_td);
  // add row to the html
  inv.appendChild(new_tr);
}
// This function pulls new item info from our form
function add_new_item (event) {
  var material = document.getElementById('material').value,
      price = '$' + document.getElementById('price').value,
      in_stock = document.getElementById('in_stock').checked,
      uid;
  if (check_values()) {
    return;
  }
  uid = id_gen();
  add_inventory(material, price, in_stock, uid);
  append_table(material, price, in_stock, uid);
  document.getElementById('material').value = "";
  document.getElementById('price').value = "";
  document.getElementById('in_stock').checked = false;
}

// Determine which items are checked
// returns a list of IDs
function which_checked() {
  var all_inputs = document.getElementsByName('select_item'),
      checked_ids = [],
      i;
  // check each input to see if it is checked
  for (i in all_inputs) {
    if (all_inputs[i].checked) {
      // find the id of the current checked table row
      var current_tr = all_inputs[i].parentElement.parentElement;
      checked_ids.push(current_tr.id);
    }
  }
  return(checked_ids);
}
// Update in stock status for specific item
function update_stock(item_id, action) {
  var item_up = document.getElementById(item_id),
      in_stk = item_up.lastChild,
      i;
  // check the inventory array for the item we are looking for
  for (i = 1; i < inventory.length; i++) {
    if (inventory[i].uid === item_id) {
      if (!inventory[i].in_stock && action === 'add') {
        // add stock to the corresponding item in the inventory array
        inventory[i].in_stock = true;
        // update html to reflect new status
        in_stk.innerText = 'Yes';
        in_stk.classList.remove('false');
        in_stk.classList.add('true');
      } else if (inventory[i].in_stock && action === 'remove') {
        // remove stock from the corresponding item in the inventory array
        inventory[i].in_stock = false;
        // update html to reflect new status
        in_stk.innerText = 'No';
        in_stk.classList.remove('true');
        in_stk.classList.add('false');
      }
    }
  }
}

// Event handler to remove stock
function remove_stock(event) {
  var selected_stock = which_checked(),
      i;
  for (i = 0; i < selected_stock.length; i++) {
    update_stock(selected_stock[i], 'remove');
  };
}
// Event handler to add stock
function add_stock(event) {
  var selected_stock = which_checked(),
      i;
  for (i = 0; i < selected_stock.length; i++) {
    update_stock(selected_stock[i], 'add');
  };
}


// This function removes the an item from our list based on an id
function item_pop(item_id) {
  // retreive the html list for manipulation
  var inv = document.getElementById('inventory'),
      item_rem = document.getElementById(item_id),
      i;
  // remove the appropriate id from the html
  inv.removeChild(item_rem);
  // search the inventory object and remove the item
  for (i = 1; i < inventory.length; i++) {
    if (inventory[i].uid === item_id) {
      inventory.splice(i, 1);
    }
  }
}
// loop through selected stock and run remove function for each item
function remove_items(event) {
  var selected_stock = which_checked(),
      i;
  for (i = 0; i < selected_stock.length; i++) {
    item_pop(selected_stock[i]);
  };
}
