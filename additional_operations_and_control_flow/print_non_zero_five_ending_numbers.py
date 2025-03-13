# Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

# ------------------------------------------------------------------

# Phase 1: Planning

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to print all numbers from 0 to 100 except those ending in 0 or 5.
# - Scope: Loop implementation with filtering
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Print all numbers from 0 to 100
#     - Must exclude numbers ending in zero or five
#     - Numbers should be displayed in order

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Use a `for loop` from 0 to 100
#     2. Check if each number ends in zero or five using modulo operator
#     3. Print numbers that don't end in zero or five

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

print("Numbers from 0 to 100 except those ending in zero or five:") # Title

for num in range(0, 100): # 0 to 100 inclusive

    if num % 10 != 0 and num % 10 != 5: # Check if not ending in zero or five
        print(num, end=" ")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Run the program -> Should display all numbers not ending in 0 or 5
# Test Case 2: Check exceptions -> Should exclude 0, 5, 10, 15, 20, 25, etc.
# Test Case 3: Check examples -> Should include 1-4, 6-9, 11-14, 16-19, etc.

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike