
function most_used_word (s) {
  var words;
  var word_count = {};
  words = s.split();
  for (i=0; i<words.length; i++) {
    w = words[i];
    if (word_count[w] >0) {
      word_count[w] += 1;
    } else {
    word_count[w] = 1;
  }
}


function testfunction (t, v) {
  var muw = 0;
  console.log("Finding the most-used word in a string:" , t);
  muw = most_used_word(t);
  console.log("Result from most_used_word:" , [muw]);
  if (muw === v) {
    console.log("test SUCCESS. (v equals muw)");
  } else {
    console.log("test FAILED. (v not equal to muw)");
  }
}

testfunction("The quick brown fox jumped over the lazy dog");
testfunction("Skip's favorite word is alphabetical. Second favorite is numerical.");
testfunction("Ed's fourth favorite word is il8n. Third favorite is alphanumerical.");
testfunction("Carolyn's sixth favorite word is alpha-betical. Fifth favorite is cat-wearing-a-hat.");
