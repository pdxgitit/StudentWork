// Return the length of the longest word in the provided sentence.
// Your response should be a number.

var stringA = "The quick brown fox jumped over the lazy dog"
var stringB = "I ATE A CHICKEN."

function find_longest_word_in(string) {
    
    var words, longestword; 
        
    words = string.split(/\W+/);

    longestword = " ";

    for (var i = 0; i < words.length; i += 1){
       if (words[i].length >= longestword.length) {
           longestword = words[i];
        }
    };

    return longestword
};
    
console.log(find_longest_word_in(stringA));
console.log(find_longest_word_in(stringB));
