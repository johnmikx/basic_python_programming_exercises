# Prog03: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks for numbers until invalid input and indicates if each input is unique or duplicate.
# - Scope: Continuous user input, duplicate detection, and immediate feedback.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept numerical inputs from user until invalid input
#     - Check if each input is a duplicate of previous inputs
#     - Display "Unique" for first occurrence of a number
#     - Display "Duplicate" for repeated numbers

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Print a message instructing the user to enter numbers
#        1.2. Create an empty `set` to track seen numbers
#     2. Start an infinite loop to continuously get user input
#        2.1. Try to:
#           2.1.1. Read user input and convert it to an integer
#           2.1.2. If the number is in the `set`, print "Duplicate"
#           2.1.3. Otherwise, print "Unique" and add the number to the `set`
#        2.2. If a non-numeric input is entered:
#           2.2.1. Print "Invalid input. Program terminated."
#           2.2.2. Break the loop
#     3. Print "Program ended." and exit

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs until a non-number is entered
print("Enter numbers (enter a non-number to stop):")

# Create an empty set to track seen numbers
seen = set()

# Start an infinite loop to take user inputs
while True:
    try:
        # Get input from the user and convert it to an integer
        num = int(input("Enter a number: "))
        
        # Check if the number has been entered before
        if num in seen:
            print("Duplicate") # Indicate that the number is a duplicate
        else:
            print("Unique") # Indicate that the number is unique
            seen.add(num) # Add the number to the set
    except ValueError:
        # Handle non-numeric input and terminate the program
        print("Invalid input. Program terminated.")
        break
    
print("Program ended.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All unique inputs -> Should display "Unique" for each
# Test Case 2: Some duplicate inputs -> Should display "Duplicate" for repeats
# Test Case 3: Immediate duplicate -> Should display "Duplicate"
# Test Case 4: Invalid input -> Should terminate program

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 3

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike