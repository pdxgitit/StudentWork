

function find_longest_word_in(s) {
  var words = [],
    word_regex = /[-\w]+/g,
    longest_word = "",
    current_word = "" ;
  words = s.match(word_regex);
  // return (words);
  for (var i = 0; i < words.length; i += 1){
    current_word = words[i];
    if (   (! current_word.match(/\d+/))
        && (current_word.length > longest_word.length)) {
      longest_word = current_word;
    }
  }
  return ([longest_word, longest_word.length]);
};


function testfunction (t) {
  var lw = "";
  console.log("Finding the longest substring in:"
              , t);
  lw = find_longest_word_in(t);
  console.log("Result from find_longest_word_in:"
              , find_longest_word_in(t));
}

testfunction("The quick brown fox jumped over the lazy dog");
testfunction("My favorite word is alphabetical. Second favorite is numerical.");
testfunction("My fourth favorite word is il8n. Third favorite is alphanumerical.")
testfunction("My sixth favorite word is alpha-betical. Fifth favorite is cat-wearing-a-hat.")
