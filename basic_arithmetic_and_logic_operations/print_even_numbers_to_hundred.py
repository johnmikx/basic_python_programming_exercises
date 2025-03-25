# Prog09: Create a program that print all the even numbers starting 
# from 0 to 100. (Use for loop)

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to print all even numbers from 0 to 100 using a `for loop`.
# - Scope: Loop implementation and even number detection.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Print all even numbers from 0 to 100
#     - Must use a `for loop`

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Use a `for loop` from 0 to 100
#     2. Using range function (start, stop, skip)
#     3. Print the even numbers

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

print("Even numbers from 0 to 100:") # Title

for num in range(0, 101, 2): # 0 to 100 inclusive
    print(num, end=" ")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Run the program -> Should display even numbers from 0 to 100
# Test Case 2: Check first few values -> Should start with 0, 2, 4, 6, 8, 10
# Test Case 3: Check last few values -> Should end with 90, 92, 94, 96, 98, 100

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike