
function longest_word_in(s) {
  // s is a string
  //
  // find the longest word within s,
  //
  // words consist of a string of alphanumerical characters + dashes
  // \w  means word, [a-zA-Z0-9_]
  // [\w-] means word + -
  //
  // suppose s = "The quick brown f0x jumped over the la-zy dog"
  // then words = ["The","quick","brown","f0x","jumped"
  //              ,"over","the","la-zy","dog"]
  //
  // for every word in words, find the length, and
  // keep track of the longest word found so far
  // if the current word is longer than the longest_word,
  // it becomes the new longest_word, and so on.

  var words = [],
      word_regex = /[-\w]+/g,
      longest_word = "",
      current_word = "" ;

  words = s.match(word_regex);

  for (var i = 0; i < words.length; i += 1) {
      current_word = words[i];
      if (   (! current_word.match(/\d/)) /* toss out digit-only words */
          && (current_word.length > longest_word.length)) {
         longest_word = current_word;
      }
  }
  return (longest_word);
};

function testfunction (t)  {
  // t is our input test string
  var lw = ""; // longest word
  console.log("Finding the longest sub string in:"
             , t);
  lw = longest_word_in(t);
  console.log("Result from longest_word_in:"
             , [lw, lw.length]);
}

// jumped, 6
testfunction("The quick brown fox jumped over the lazy dog");

// alphabetical, 12
testfunction("My favorite word is alphabetical. Second favorite is numerical.");

testfunction("Skip's favorite word is 8763871644919669423. Second favorite is numerical.");

testfunction("Ed's fourth favorite word is i18n. Thrird favorite is alphanumerical.");

testfunction("Carolyn's sixth favorite word is alpha-betical. Fifth favorite is cat-wearing-a-hat.");
