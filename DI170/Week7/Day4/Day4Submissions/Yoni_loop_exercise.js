const arr = [8, 4, 16, 2]
let existingSum = 0 //any variable where loops results are saved must exist before the loop starts

for (let currentNum of arr) // "let [blank] of [array_name]" creates "blank" as a variable
{
    existingSum = existingSum + currentNum // this combines the values from the two variables; order matters!
    // existingSum += currentNum // this is the same thing as the line above
}
console.log(existingSum) // this must be outside the loop in order for all results of the loop to print on one line
