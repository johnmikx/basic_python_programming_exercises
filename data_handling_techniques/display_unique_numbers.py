# Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that don't have duplicate.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks user to input 10 numbers and displays all numbers that don't have duplicates.
# - Scope: User input processing, duplicate detection, and unique number identification.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Identify numbers that appear only once (no duplicates)
#     - Display only the non-duplicate numbers

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Create an empty list
#        1.2. Use a loop (for loop) to get ten numbers
#        1.3. Convert to integers (coz it reads as 'string')
#     2. Identify unique numbers
#        2.1. Create an empty list
#        2.2. Loop through the stored numbers
#        2.3. Check if the number appears only once in the list using `count()`
#           2.3.1. If yes, add it to the unique numbers list
#     3. Display the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Initialize
numbers = []

# Ask user for inputs
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
# Find numbers that don't have duplicates
unique_numbers = []

# Loop through the stored numbers
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)
    
# Display the result
if unique_numbers:
    print("Numbers with no duplicates:")
    for num in unique_numbers:
        print(num)
else:
    print("No unique numbers found.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All unique numbers -> Should display all 10 numbers
# Test Case 2: All duplicate numbers -> Should display "No unique numbers found."
# Test Case 3: Mix of unique and duplicate numbers -> Should display only unique numbers

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 3

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike