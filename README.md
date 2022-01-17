# LeetCode-Backtracking

## Problem Set

[ProblemSet](https://seanprashad.com/leetcode-patterns/)

### Word Search 
[Problem](https://leetcode.com/problems/word-search/)
* Initially, find the letter on the board which corresponds to the given 1st letter of the word.
* From this letter, explore in the 4 different directions and try to find the remaining letters of the word recursively.
* If you reach the end of the word, return True...you have found a match
* If you have tried exploring all directions and cannot find the matching word, return False.
* If no letter starting with the first letter of the word yields a match, return False finally.

### Letter Case Permutation
[Problem](https://leetcode.com/problems/letter-case-permutation/)
* Start with an empty string
* Next, start adding characters one by one recursively to this string.
* If the character is not an alphabet, just add it to the string, else branch out into normal case and swapped version
* Finally, if a permutation equal in length to the original string is found, add it to the result

### Subsets
[Problem](https://leetcode.com/problems/subsets/)
* Start with an empty subset
* Branch into two permutations - one with the element at the current index, and the other without.
* Return if the current index exceeds the limit of the given list after adding the subset to the result

### Subsets 2
[Problem](https://leetcode.com/problems/subsets-ii/)
* Start with empty subset
* The idea is to branch into two permutations - one with the element at the current index and the other without, but in the latter, children cannot include the element at the current index.
* In order to achieve this, we sort he initial list and then loop till a new element is found and carry out expansion of the second branch, recursively.
* When starting index passes the length of the given list, add the combination to the result.

