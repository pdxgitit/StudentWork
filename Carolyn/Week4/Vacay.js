function sleep_in(weekday,vacay) {
  if(weekday === vacay){
    return(true);
  } else if(weekday === true){
    return(false);
  } else{
    return(true);
  }
}

console.log(sleep_in(false, false));
console.log(sleep_in(true, false));
console.log(sleep_in(false, true));
