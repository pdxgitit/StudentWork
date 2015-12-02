
function most_used_word (s) {
  var words;
  // word_count["word"] = 3 means 3 occurances of 'word' in s
  var word_count = {};
  var muw = "";

  word_count[""] = 0;

  words = s.split(/ /);
  for (i=0; i<words.length; i++) {
    w = words[i];
    if (word_count[w] > 0) {
      word_count[w] += 1; // already in dict, increment it.
    } else {
      word_count[w] = 1; // first time around, initialize = 1.
    }
  }
  //console.log("word_count", word_count);

  for (w in word_count) {
    if (word_count[w] > word_count[muw]) {
      muw = w;
    }
  }
  return muw;
}

function testfunction (t, v)  {
  // t is our input test string
  // v is the expected return
  var muw = 0; // most-used word
  console.log("Finding the the most-used word in a string:" , t);
  muw = most_used_word(t);
  console.log("Result from most_used_word:" , [muw]);
  if (muw === v) {
    console.log("test SUCCESS. (v equals muw)");
  } else {
    console.log("test FAILED. (v not equal to muw)");
  }
}

testfunction("the the the the quick brown fox jumped over the lazy dog"
            ,"the");

testfunction("My favorite word is alphabetical. Second favorite is numerical."
            , "is");
            // TODO: SPEC. CHECK
            // there are two correct answers. What should we expect here????

testfunction("We are going to learn CSS to make websites."
            , "to");

// more test cases can be added here.....
