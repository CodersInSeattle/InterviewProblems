1. [Palindrome Permutatino] Given a string, write a function to check if it is a permutation of a palindrome.

2. [[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)] Given an input string, reverse the string word by word.

3. [[Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/)] The API: `int read4(char *buf)` reads 4 characters at a time from a file.  
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.  
By using the read4 API, implement the function `int read(char *buf, int n)` that reads `n` characters from the file.  
Note: The read function may be called multiple times.

4. [[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)] Implement regular expression matching with support for '.' and '\*'.  
'.' Matches any single character.  
'\*' Matches zero or more of the preceding element.  
The matching should cover the entire input string (not partial).

5. [[Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)] Given a string `S`, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

6.[yelp movie] 题目是：给一串movie，假定每个movie都是一个小时，并且都在整点播放；给你一个List的movies，让你安排播放时间，如果没有答案throw一个exception。

比如 电影A: 14, 15, 16, 17

电影B: 14, 15, 16

电影C: 14, 15

电影D: 14, 15, 17.

返回一个解就行，比如 A 14, B 16, C 15, D 17。 如果你要 A 14, B 15, 后面 C就没法看了。
