function find_longest_word_in(s) {
  // s is a string
  // find the longest word within s, words separated by spaces
  // suppose s = "The quick brown fox jumped over the lazy dog"
  // then words = ["The","quick","brown","fox","jumped"
  //              ,"over","the","lazy","dog"]
  // words is an array of sub-strings, with spaces removed.
  // for every word in words, find the length, and
  // keep track of the longest word found so far
  // if the current word is longer than the longest,
  // it becomes the new  longest, and its length becomes the new longest_length

  var words = [],
      longest_word = "",
      current_word = "" ;
  words = s.split(" ");

  for (var i = 0; i < words.length; i += 1) {
      current_word = words[i];
      // compare length of current word to longest word
      if (current_word.length > longest_word.length) {
         longest_word = current_word;
      }
  }
  return (longest_word);
};

function testfunction (imreallybadwithnames)  {
  console.log("Finding the longest sub string in:");
  console.log(imreallybadwithnames);
  console.log("Result from find_longest_word_in:");
  console.log(find_longest_word_in(imreallybadwithnames));
}

// jumped, 6
testfunction("The quick brown fox jumped over the lazy dog");

// alphabetical, 12
testfunction("My favorite word is alphabetical. Second favorite is numerical.");
