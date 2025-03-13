# Prog02: Create a program that ask user to input 10 numbers. 
# Display all numbers. 
# For numbers with duplicate, display only the first entry.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks user to input 10 numbers and displays all numbers with duplicates shown only once.
# - Scope: User input processing and duplicate elimination.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Display all numbers in the order they were entered
#     - For numbers with duplicates, display only the first occurrence

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Create an empty list
#        1.2. Use a loop (for loop) to get ten numbers
#        1.3. Convert to integers (coz it reads as 'string')
#     2. Identify unique numbers
#        2.1. Create an empty `set` to track seen numbers
#        2.2. Loop through the stored numbers
#        2.3. If a number has not been seen before, print it and add it to the `set`
#     3. Display the result with duplicates shown only once

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Initialize
numbers = []

# Ask user for inputs
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display all numbers with duplicates shown only once
print("All numbers (with duplicates shown only once):")
seen = set()
for num in numbers:
    if num not in seen:
        print(num, end=" ")
        seen.add(num)

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All unique numbers -> Should display all 10 numbers
# Test Case 2: All duplicate numbers -> Should display only one occurrence of each number
# Test Case 3: Mix of unique and duplicate numbers -> Should display first occurrence of each number

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 3

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike