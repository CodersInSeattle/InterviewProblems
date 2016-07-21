1. [Rank from Stream] Imagine you are reading in a stream of integers. Periodically, you wish to be able
to look up the rank of a number `x` (the number of values less than or equal to `x`).  
Implement the data structures and algorithms to support these operations. That is, implement the method
`track(int x)`, which is called when each number is generated, and the method `getRankOfNumber(int x)`,
which returns the number of values less than or equal to `x` (not including `x` itself).

2.  Given an array `A` of `n` distinct integers, design an algorithm to find a local minimum: an index `i` such that `A[i-1] < A[i] < A[i+1]`.
3. Given an `n * n` matrix `A` of `n^2` numbers, find a pair `(i, j)` such that `A[i][j] < A[i+1][j]`, `A[i][j] < A[i][j+1]`, `A[i][j] < A[i-1][j]`, and `A[i][j] < A[i][j-1]`.

4. [Distance Maximizing] Given an array `A`, find the maximum `j - i` such that `A[j] > A[i]`.
5. [[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)] Given an array `A`, find the maximum `A[j] - A[i]` such that `j > i`.

6. [Sparse Search] Given a sorted array of strings that is interspersed with empty strings, write a function to find the location of a given string.

7. [[Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)] Divide two integers without using multiplication, division and mod operator.

8. You are given an array whose elements are weakly monotonically increasing and then weakly monotonically decreasing. Find the max element in this array.  
Note: Duplicates are allowed.

9. Given a matrix `A` of size `X * Y`, filled with integers. Rows and columns of the matrix are sorted in ascending order. Find the number of zeros in the matrix.

10. [[Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)] You have a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.  
What is the maximum number of envelopes can you Russian doll? (put one inside other)  
Example:
Given envelopes = `[[5, 4], [6, 4], [6, 7], [2, 3]]`, the maximum number of envelopes you can Russian doll is `3` `([2, 3] => [5, 4] => [6, 7])`.
