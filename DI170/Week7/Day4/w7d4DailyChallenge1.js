// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

let sentence = "He\'s not a bad guy, you might even like him!"

// Create a variable called wordNot where its value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

let wordNot = sentence.indexOf("not")

// Create a variable called wordBad where its value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

let wordBad = sentence.indexOf("bad")

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad !' 
//   --> the result is : 'This movie is good !'

//   Your string is : 'This dinner is bad !' 
//   --> the result is : 'This dinner is bad !'

if (wordNot < wordBad) {
    let notBad = sentence.substring(wordNot, wordBad + 3)
    let goodString = sentence.replace(notBad, "good")
    console.log(goodString)
} else {
    console.log(sentence)
}

