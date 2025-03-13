# Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks user to input 10 numbers and displays all numbers that have duplicates.
# - Scope: User input processing and duplicate detection.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Identify numbers that appear more than once
#     - Display only the numbers with duplicates

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Create an empty list
#        1.2. Use a loop (for loop) to get ten numbers
#        1.3. Convert to integers (coz it reads as 'string')
#     2. Identify duplicate numbers
#        2.1. Create an empty list
#        2.2. Loop through the stored numbers
#        2.3. If a number appears more than once and is not already in the duplicate list:
#           2.3.1. Add it to the duplicate list
#     3. Display the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Initialize
numbers = []

# Ask user for inputs
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
# Create an empty list to store duplicate numbers
duplicates = []

# Loop through the list to check for duplicates
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
    
# Display the result
if duplicates:
    print("Numbers that have duplicates:")
    for num in duplicates:
        print(num, end=" ")
else:
    print("No duplicate numbers were found.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All unique numbers -> Should display "No duplicate numbers found"
# Test Case 2: All duplicate numbers -> Should display all distinct numbers
# Test Case 3: Mix of unique and duplicate numbers -> Should display only duplicate numbers

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 4

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike