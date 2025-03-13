# Prog08: Create a program that print all the odd numbers starting 
# from 0 to 100. (Use while loop)

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to print all odd numbers from 0 to 100 using a `while loop`.
# - Scope: Loop implementation and odd number detection.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Print all odd numbers from 0 to 100
#     - Must use a `while loop`
# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize by 1
#        1.1 Use a `while loop` to iterate until counter exceeds 100
#     2. Increment counter by 2
#     3. Print the odd numbers

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

print("Odd numbers from 0 to 100:") # Title

# Initialize
num = 1

while num <= 100: # 0 to 100 inclusive, iterate until counter exceeds 100
    print(num, end=" ")
    num += 2 # Increment counter by 2 resulting in odd numbers

print() # Add a newline at the end

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Run the program -> Should display odd numbers from 0 to 100
# Test Case 2: Check first few values -> Should start with 1, 3, 5, 7, 9
# Test Case 3: Check last few values -> Should end with 91, 93, 95, 97, 99

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike