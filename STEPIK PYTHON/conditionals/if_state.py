# Read input
meal, fullness_level, is_on_diet = input().split()
fullness_level = float(fullness_level)
is_on_diet = is_on_diet == "True"  # Convert string to boolean

# Decision-making using if-elif-else
if meal == "Breakfast":
    print("Ice cream isn't for breakfast.")
elif (meal == "Lunch" or meal == "Dinner") and fullness_level <= 3.5 and not is_on_diet:
    print("Yes, please! I'd love some!")
elif meal != "Breakfast" and fullness_level <= 6.0:
    print("No, that's too heavy for me. I do have room for an apple, though!")
else:
    print("None for me, thanks.")
