

8 == (4 * 2)      # True: 8 is equal to (4 * 2), which is also 8
8 != 42           # True: 8 is not equal to 42
8 < 42            # True: 8 is less than 42
8 <= 42           # True: 8 is less than or equal to 42
8 > 4             # True: 8 is greater than 4
8 >= 4            # True: 8 is greater than or equal to 4
"A" < "Z"         # True: "A" is alphabetically smaller than "Z"
"hi" in "Moshiri" # True: "hi" is a substring of "Moshiri"
"I" not in "TEAM" # True: "I" is not a substring of "TEAM" 


def compare_values(x, y):
	print(x < 5)
	print(x > 5)
	print(x == 5)
	print(x != 5)   

	print(y in "apple stems")
	print(y not in "apple stems")

	print(x < 5 and y in "apple stems")
	print(x < 5 or y in "apple stems")

	print(not x < 5)


