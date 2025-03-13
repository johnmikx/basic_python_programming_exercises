# Prog05: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks for numbers until invalid input and displays them sorted from lowest to highest.
# - Scope: Continuous user input and sorting functionality.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept numerical inputs from user until invalid input
#     - Store all valid inputs
#     - Sort the numbers from lowest to highest
#     - Display the sorted list at the end
#     - Terminate on invalid input

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Print a message instructing the user to enter numbers
#        1.2. Create an empty `list` to store entered numbers
#     2. Start an infinite loop to continuously get user input
#        2.1. Try to:
#           2.1.1. Read user input and convert it to a float
#           2.1.2. Add the number to the `list`
#        2.2. If a non-numeric input is entered:
#           2.2.1. Print "Invalid input. Program terminated."
#           2.2.2. Break the loop
#     3. Check if at least one number was entered
#        3.1. If numbers exist:
#           3.1.1. Sort the list in ascending order
#           3.1.2. Print "Numbers sorted from lowest to highest:"
#           3.1.3. Loop through the sorted list and print each number
#        3.2. Otherwise, print "No valid numbers were entered."

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs until a non-number is entered
print("Enter numbers (enter a non-number to stop):")

# Create an empty list to store entered numbers
numbers = []

# Start an infinite loop to continuously get user input
while True:
    try:
        # Get input from the user and convert it to a float
        num = float(input("Enter a number: "))
        # Add the valid number to the list
        numbers.append(num)
    except ValueError:
        # Handle non-numeric input and terminate the program
        print("Invalid input. Program terminated.")
        break

# Check if at least one valid number was entered
if numbers:
    numbers.sort() # Sort the numbers in ascending order

    # Display the sorted numbers
    print("Numbers sorted from lowest to highest:")
    for num in numbers:
        print(num, end=" ") # Print numbers on the same line with spaces
    print() # Move to the next line after printing all numbers
else:
    # Handle case where no valid numbers were entered
    print("No valid numbers were entered.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Already sorted inputs -> Should display in same order
# Test Case 2: Reverse sorted inputs -> Should display in reverse of input order
# Test Case 3: Random order inputs -> Should display in sorted order
# Test Case 4: Duplicate numbers -> Should include all duplicates in sorted order
# Test Case 5: No inputs (immediate invalid) -> Should display message
# Test Case 6: Decimal inputs -> Should sort decimals correctly

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 3

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike