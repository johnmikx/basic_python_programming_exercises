# Prog02: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program that asks for numbers until invalid input and displays the number with the most duplicates.
# - Scope: Continuous user input, frequency counting, and maximum frequency identification.

# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept numerical inputs from user until invalid input
#     - Count occurrences of each number
#     - Identify which number(s) occur most frequently
#     - Display the number with the most duplicates
#     - Terminate on invalid input

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.1. Print a message instructing the user to enter numbers
#        1.2. Create an empty `list` to store entered numbers
#     2. Start an infinite loop to continuously get user input
#        2.1. Try to:
#           2.1.1. Read user input and convert it to an integer
#           2.1.2. Add the number to the `list`
#        2.2. If a non-numeric input is entered:
#           2.2.1. Print "Invalid input. Program terminated."
#           2.2.2. Break the loop
#     3. Check if at least one number was entered
#        3.1. If numbers exist:
#           3.1.1. Create an empty dictionary to store number frequencies
#           3.1.2. Loop through the stored numbers and count occurrences
#           3.1.3. Identify the number with the highest occurrence
#           3.1.4. Print the most repeated number and its frequency
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
        # Get input from the user and convert it to an integer
        num = int(input("Enter a number: "))
        # Add the valid number to the list
        numbers.append(num)
    except ValueError:
        # Handle non-numeric input and terminate the program
        print("Invalid input. Program terminated.")
        break

# Check if at least one valid number was entered
if numbers:
    # Create a dictionary to store the frequency of each number
    frequency = {}

    # Count occurrences of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the number with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    max_count = frequency[most_frequent]

    # Display the most repeated number
    print(f"The number with the most duplicates is: {most_frequent} (appeared {max_count} times)")
else:
    print("No valid numbers were entered.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: One clear winner -> Should display the number with most duplicates
# Test Case 2: No inputs (immediate invalid) -> Should display message

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 4

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike