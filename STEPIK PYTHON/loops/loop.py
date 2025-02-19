password = input()

# Checking character categories
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

# Count the number of satisfied categories
category_count = sum([has_upper, has_lower, has_digit, has_symbol])

# Check password security
if len(password) >= 7 and category_count >= 3:
    print("secure")
else:
    print("insecure")
