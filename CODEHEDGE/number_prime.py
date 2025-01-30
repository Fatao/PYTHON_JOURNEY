# Check if a given natural number is prime

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 1:
    print("Yes")
else:
    print("No") 
    
