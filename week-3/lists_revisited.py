#!usr/bin/env python3
myFavouriteFruits = ["banana" , "cherry" , "apple" , "guava" , "orange" ,]
for fruit in myFavouriteFruits:
    print(fruit)
print(len(myFavouriteFruits))
friends = ["ferg" , "bobby" , "godzly" , "vague" , "noah" , "aerith"]
print(friends)
friends[0] = "kith"
print(friends)
print("                                 ")
new_friends = friends.copy()
print(new_friends)
print("                                 ")
new_friends.sort()
print(new_friends)
print("                                 ")
new_friends.pop()
print(new_friends)