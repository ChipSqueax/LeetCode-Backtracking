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

