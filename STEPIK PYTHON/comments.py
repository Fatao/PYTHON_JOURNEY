x, y, z = 2, 5, 7
print(str(x + y * z) + " is not the same as " + str((x + y) * z))  # Operator precedence

print(str(float(x)) + " is not the same as " + str(x))  # float vs int

# Print numbers 1 to 3, one on each line :This is a single line comment
print(1)
print(2)
print(3)

# Print digit in one's place of num

num = 123
print(num % 10)
print(num % 10) # Print digit in one's place of num



'''
This is a multiline comment
Show equality of multiline string and single-line string
'''
mls = "Hello, " \
"how are you?"
sls = "Hello, how are you?"

print(mls == sls)


'''
Calculate percentage of wall covered by new wallpaper
'''
# Calculate wall dimensions
height = 8
long_wall = 13
short_wall = 10.5
total_wall = (height * (long_wall + short_wall))

# Calculate new wallpaper dimensions
height_covered = 5
l_w_covered = 8
s_w_covered = 7
total_covered = height_covered * (l_w_covered + s_w_covered)

# Print coverage as percentage
print("Coverage: " + str(total_covered / total_wall))

# Declare messages
greeting = "Welcome to this program!"
work_in_progress = "We are almost ready to release this program, thank you for your patience."
closing = "Hope to see you back soon!"

# Print messages to stdout
print(greeting)
print(work_in_progress)
print(closing)



# Declare messages
greeting = "Welcome to this program!"
work_in_progress = "We are almost ready to release this program, thank you for your patience."
closing = "Hope to see you back soon!"

# Print messages to stdout
print(greeting)
print(work_in_progress)
print(closing)