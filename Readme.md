String Reversal Using Recursion

About

# This project implements a recursive function in Python to reverse a string.
# The goal is to demonstrate understanding of recursion and base cases.



# function

 def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0] 

    Explanation
	•	If the string has 0 or 1 character, return it.
	•	Otherwise:
	•	Remove the first character.
	•	Recursively reverse the remaining string.
	•	Add the first character to the end.



    Input:  "pen"
Output: "nep"


Complexity
	•	Time Complexity: O(n²)
	•	Space Complexity: O(n)

This project demonstrates recursive problem solving and complexity analysis in a clear and simple way. -->