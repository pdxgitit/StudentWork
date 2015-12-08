testfunction("The quick brown fox jumped over the lazy dog")
testfunction("My favorite word is alphabetical. Second favorite is numerical.")
testfunction("The quick brown fox jumped 986986875864754 over the lazy dog")
testfunction("The quick brown fox jumped-over the lazy dog")

function testfunction (t) {
  console.log("Finding the longest sub string in:",
              t);
  console.log("Longest word is:",
              longest_word_in(t));
};

function longest_word_in (s) {
  // s is a string
  // find the longest word in s
  var words = s.match(/[-\w]+/g),
      longest = "";
  for (var word = 0; word < words.length; word += 1) {
    if ( (! words[word].match(/\d+/))
      && (words[word].length > longest.length)) {
      longest = words[word];
    };
  };
  return ([longest, longest.length]);
};
