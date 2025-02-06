


# Assume that the variables alpha, beta, and gamma have been declared, with each variable containing an arbitrary bool value.

#Print True if alpha, beta, and gamma are all True or if delta does not contain any vowels. Otherwise, print False.

alpha = True
beta = True
gamma = True
delta = "aeiou"

if (alpha and beta and gamma) or (not any(v in delta for v in "aeiou")):
    print(True)
else:
    print(False)


(a == 12) or (b != 5 and c <= 10)
(a == 12) or (b != 5) and (c <= 10)
(a == 12) or ((b != 5) and (c <= 10))
((a == 12) or (b != 5)) and (c <= 10)   # Correct   







