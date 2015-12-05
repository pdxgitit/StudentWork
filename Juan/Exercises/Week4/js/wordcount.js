testfunction("The quick brown fox fox fox jumped over the lazy dog")
testfunction("My favorite word is alphabetical. Second favorite is numerical.")
testfunction("The quick brown fox jumped 986986875864754 over the lazy dog")
testfunction("The quick brown fox jumped-over the lazy dog")

function testfunction (t) {
  console.log("Finding the longest sub string in:",
              t);
  console.log("Most used word is:",
              most_used_word(t));
};

function most_used_word (s) {
  var words = s.split(" "),
  //words = s.match(/[-\w]+/g),
      word_count = {"" : 0},
      muw = "";
  console.log(words);
  for (var w = 0; w < words.length; w += 1) {
    if (word_count[words[w]] > 0) {
      word_count[words[w]] += 1;
    } else {
      word_count[words[w]] = 1;
    };
  };
  console.log(word_count);
  for (var w = 0; w < words.length; w += 1) {
    var curr_word = word_count[words[w]];
    if (curr_word > word_count[muw]){
      muw = words[w];
    } else if () {

    };
  };
  return (muw);
};
