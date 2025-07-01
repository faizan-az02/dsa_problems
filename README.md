# LEETCODE PROBLEMS REPOSITORY
Problem 1:<br>
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1.

Problem 2:<br>
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
Return the smallest index i at which either a row or a column will be completely painted in matrix.

Problem 3:<br>
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Problem 4:<br>
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Problem 5:<br>
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Return a boolean array answer, where answer[j] is the answer to the jth query.

Problem 6:<br>
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
A land cell if grid[r][c] = 0, or a water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:<br>
-Catch all the fish at cell (r, c).<br>
-Move to any adjacent water cell.<br>
A fisher can start at any water cell (r, c) and can do the following operations any number of times:<br>
-Catch all the fish at cell (r, c).<br>
-Move to any adjacent water cell.<br>
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Problem 7:<br>
In this problem, a tree is an undirected graph that is connected and has no cycles.<br>
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.<br>
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Problem 8:<br>
An array is considered special if the parity of every pair of adjacent elements is different. In other words, one element in each pair must be even, and the other must be odd.<br>
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

Problem 9:<br>
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.<br>
There may be duplicates in the original array.<br>
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

Problem 10:<br>
Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.<br>
A subarray is defined as a contiguous sequence of numbers in an array.

Problem 11:<br>
You are given a string s.<br>
Your task is to remove all digits by doing this operation repeatedly:<br>
Delete the first digit and the closest non-digit character to its left.<br>
Return the resulting string after removing all digits.<br>
Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

Problem 12:<br>
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:<br>
Find the leftmost occurrence of the substring part and remove it from s.<br>
Return s after removing all occurrences of part.<br>
A substring is a contiguous sequence of characters in a string.

Problem 13:<br>
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].<br>
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.

Problem 14:<br>
You have n  tiles, where each tile has one letter tiles[i] printed on it.<br>
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Problem 15:<br>
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].<br>
Return the total number of bad pairs in nums.

Problem 16:<br>
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.<br>
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.<br>
Note that 0 is neither positive nor negative.

Problem 17:<br>
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

Problem 18:<br>
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.<br>
A pair (i, j) is fair if:<br>
0 <= i < j < n, and<br>
lower <= nums[i] + nums[j] <= upper

Problem 19:<br>
You are given an integer n.<br>
We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.<br>
Return the number of groups that have the largest size, i.e. the maximum number of elements.

Problem 20:<br>
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Problem 21:<br>
Given an array nums of integers, return how many of them contain an even number of digits.

Problem 22:<br>
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Problem 23:<br>
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

Problem 24:<br>
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n^2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Problem 25:<br>
You are given a 0-indexed integer array nums.
Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].