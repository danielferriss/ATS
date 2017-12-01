from bisect import insort

###################
#   Midterm
#   Due: Tuesday, November 28 2017
###################

# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# You will lose points if your solution uses division.
# Your solution should run in O(n) time.
# Your solution should not allocate any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers. You may assume len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#

def array_almost_product(arr):
	outputarr = []
	for num in range(0, len(arr)):
		outputarr.append(1)
		for num2 in range(0, len(arr)):
			if num2 != len(outputarr) - 1:
				outputarr[len(outputarr) - 1] *= arr[num2]
	return outputarr


# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#

def pascals_triangle(i):
	line = [1]
	for k in range(max(i ,0)):
		line.append(int(line[k]*(i-k)/(k+1)))
	return line


# Alive People
#
# Write a function that, given a list of strings representing a person's birth year: age of death,
# will return the year that had the most people alive (inclusive). If there are multiple years that tie, return the earliest.
# You can think of a birthdate and a deathdate as a range of years. Of all the birth years in the list, find the one where the lastest
# amount of people in the list were still alive.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#

def alive_people(people):
	population = [list(int(y) for y in x.split(": ")) for x in people]
	for pair in population:
		pair[1] = pair[0] + pair[1]
	population = [tuple(l) for l in population]
	years_dict = dict()
	when_born = sorted(population, key=lambda x: -x[0])
	alive = []
	dead = []
	for item in range(when_born[-1][0], max(population, key=lambda x: x[1])[1] + 1):
		while when_born and when_born[-1][0] == item:
			insort(alive, -when_born.pop()[1])
		while alive and alive[-1] == -(item - 1):
			dead.append(-alive.pop())
		years_dict[item] = len(alive)
	return max(years_dict, key=years_dict.get)


# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurences of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But the person who wrote all of your homewokrs wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the homework creator made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# the_string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.

def string_my_one_true_love(the_string):
	if the_string is None:
		return None

	s = list(the_string)
	x = []

	for elem in s:
		x.append(s.count(elem))

	y = 0

	for i in range(0, len(x)):
		if y > 1:
			break
		for j in range(0, len(x)):
			if y > 1:
				break
			if x[j] != x[i]:
				x[j] = x[i]
				y += 1
				break
	if y > 1:
		return False
	return True


# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest Palindrome substring

def longest_palindrome_substring(word):
	upper = word.upper()
	maximum = 1
	start = 0
	length = len(upper)
	first = 0
	last = 0
	for current in range(1, length):
		first = current - 1
		last = current
		while first >= 0 and last < length and upper[first] == upper[last]:
			if last - first + 1 > maximum:
				start = first
				maximum = last - first + 1
			first -= 1
			last += 1
		first = current - 1
		last = current + 1
		while first >= 0 and last < length and upper[first] == upper[last]:
			if last - first + 1 > maximum:
				start = first
				maximum = last - first + 1
			first -= 1
			last += 1
	return word[start:start + maximum]

# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
# Do not consider case. Therefore, 'A' and 'a' are considered the same character
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "zzAabcdefFgg"
#
#   Output:
#   "abcdef"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring

def longest_unique_substring(word):
	S = word.lower()
	lastoccurrence = {} 
	longestlength = 0
	longestpos = 0
	currentpos = 0
	currentlength = 0

	for a, b in enumerate(S):
		l = lastoccurrence.get(b, -1)
		if l < currentpos: 
			currentlength += 1
		else:
			if currentlength > longestlength: 
				longestpos = currentpos
				longestlength = currentlength
			currentlength -= l - currentpos
			currentpos = l + 1
		lastoccurrence[b] = a
	if currentlength > longestlength:
		longestpos = currentpos
		longestlength = currentlength
	return word[longestpos:longestpos + longestlength]

# Three Sum
#
# Given an array S of n integers and constant 'target', are there elements a, b, c in S such that
# a+b+c = target? Find all unique triplets in the array which gives the sum of target.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.

def three_sum(arr, target):
	s = sorted(arr)
	output = []
	for k in range(len(s)):
		targeted = target - s[k]
		i,j = k+1, len(s)-1
		while i < j:
			sum_two = s[i] + s[j]
			if sum_two < targeted:
				i += 1
			elif sum_two > targeted:
				j -= 1
			else:
				addedarr = [s[k],s[i],s[j]]
				if addedarr not in output:
					output.append([s[k],s[i],s[j]])
				i += 1
				j -= 1
	return output


# Zero Sum
#
# Return True if a subarray (not any element) summed can create 0.
# Otherwise return False.
#
# Time Complexity
# ------------
# Optimal time complexity is O(n). You can assume the running time of updating a dictionary is O(1)
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr: array
#   array of numbers

def zero_sum(arr):
	dictionary = {}
	my_sum = 0
	i = 0
	while (i < len(arr)):
		my_sum = my_sum + arr[i]
		if (arr[i] == 0 or my_sum == 0 or my_sum in dictionary):
			return True
		dictionary[my_sum] = i
		i = i + 1
	return False



# Stair Stepping
#
# One day, Alice's power went out in her house.
# Because Alice is currently in 374, she decided to count how many distinct ways she can climb up her staircase (from the bottom to the last stair). Alice is able to skip some stairs because she has very long legs.
# Help Alice determine the number of distinct ways she can climb up the staircase given the number of stairs on the staircase (stairs) and the maximum number of stairs she can skip at each one of her steps (skip).
#
# Time Complexity
# ---------------
# Optimal time complexity is O(stairs).
# Example 1:
# stairs = 3
# skip = 0
#
#   #
#  ##
# ###
# 123
#
# Alice cannot skip any stairs, so there is only one way.
# BOTTOM -> 1 -> 2 -> 3
#
# Example 2:
# stairs = 3
# skip = 1
#
#   #
#  ##
# ###
# 123
#
# Alice can skip one stair at most, so there are 3 ways.
# BOTTOM -> 1 -> 2 -> 3
# BOTTOM -> 1 -> 3
# BOTTOM -> 2 -> 3
#
# Example 3:
# stairs = 5
# skip = 2
#
#     #
#    ##
#   ###
#  ####
# #####
# 12345
#
# Alice can skip two stairs at most, so there are 13 ways.
#
# BOTTOM -> 1 -> 2 -> 3 -> 4 -> 5
# BOTTOM -> 1 -> 2 -> 3 -> 5
# BOTTOM -> 1 -> 2 -> 4 -> 5
# BOTTOM -> 1 -> 3 -> 4 -> 5
# ...
# ...
# ...
# BOTTOM -> 3 -> 5
#
# Note that Alice must start at the "0th" step and finish exactly at the Nth step where N is the number of stairs.

def staircase_ways(stairs, skip):
	ways = [1] + [None] * stairs
	for i in range(1, stairs+1):
		ways[i] = sum(ways[max(0, i-(skip + 1)):i])
	return ways[stairs]


# Odd One Out
#
# Given an array of 2n + 1 integers where each integer except one is duplicated, return the number that only appears once in the array.
#
# Time complexity
# ---------------
# Optimal time complexity is O(n). Try to only use O(1) space/memory.
#
# Example 1:
# arr = [10]
# Answer is 10.
#
# Example 2:
#
# arr = [3, 2, 1, 3, 2, 4, 4]
# Answer is 1.
#
#
# Example 3:
# arr = [-1, 1, 0, 5, 0, 2, 1, 2, 5]
# Answer is -1.

def odd_one_out(arr):
	for element in arr:
		if arr.count(element) == 1:
			return element
	return None


# Circular Shift
#
# Given an array (arr) and a shift value (k), shift the array to the
# right by k. If the rightmost element will become out of bounds, move
# it to the front of the array (hence circular shift).
#
# Time complexity
# ---------------
# Optimal complexity is O(len(arr)). Try using only O(1) space/memory
#
# Example 1:
# arr = [1, 2, 3, 4, 5]
# k = 1
# Returns [5, 1, 2, 3, 4]
#
# Example 2:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Returns [4, 5, 1, 2, 3]
#
# Example 3:
# arr = [1, 2, 3]
# k = 10
# Returns [3, 1, 2]

def circular_shift(arr, k):
	if arr is None:
		return None
	if k == None:
		return None
	c = len(arr) - (k % len(arr))
	return arr[c:] + arr[:c]


# Reverse Linked List
#
# Given a linked list, reverse it in-place
#
# Time Complexity
# ---------------
# Optimal time complexity is O(n). Try to use only O(1) memory.

class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

def reverse_list(head):
	new_head = None
	while head:
		holder = head
		head = holder.next_node
		holder.next_node = new_head
		new_head = holder
	return new_head



