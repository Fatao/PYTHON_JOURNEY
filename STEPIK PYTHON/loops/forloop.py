# Assuming name is already defined with a string value
name = "John"  # Replace with your actual name
message = f"Hello, {name}! Welcome to Intro to Python! :)"

# Calculate the total width needed (message length + 2 spaces + 2 asterisks)
width = len(message) + 4

# Print top row of asterisks
print("*" * width)

# Print empty row
print("*" + " " * (width - 2) + "*")

# Print message row with spaces and asterisks
print(f"* {message} *")

# Print empty row
print("*" + " " * (width - 2) + "*")

# Print bottom row of asterisks
print("*" * width)