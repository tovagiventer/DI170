// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

let star = []
for (let i = 0; i < 6; i++) {
    star.push("*")
    let aster = star.join(' ')
    console.log(aster)
}

let strix = ""
for (let i = 0; i < 6; i++)  {
    for (let j = 0; j < i + 1; j++){
    }
    strix += "* "
    console.log(strix)
}