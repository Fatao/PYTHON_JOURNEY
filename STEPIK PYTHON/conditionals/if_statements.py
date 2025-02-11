'''

#  You're planning to take a trip to CodeLand to watch your favorite computer scientist participate in a coding competition (what an opportunity!). CodeLand is exactly distance miles away, and the show starts in time hours. You know that, regardless of speed limits, the fastest your car can drive is exactly max_speed miles per hour.

Assume that the variables distance, time, and max_speed have already been defined, with each variable containing an arbitrary int value.

Write a Python program that prints Yes if you can make it to the show on time, and No otherwise. The program should print the result using the print() function.    

'''


distance, time, max_speed = map(int, input().split())

max_distance = max_speed * time

if max_distance >= distance:
    print("possible")
else:
    print("impossible")
