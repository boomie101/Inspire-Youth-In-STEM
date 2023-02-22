#mutable vs immutable
#mutable means you can edit a program eg you can add,remove,arrange elments in a list eg lists
#immutable means you cannot edit a program eg tuples
# 1)Lists are mutable
friends = ["Mudavadi", "Isaac" , "Alex"]
students = ["Joseph" , "Salman"]
friends.extend(students)
friends.append("Austin")
friends.sort()
print(friends)

# 2)Tuples are immutable
#tuples are a type of list that cannot be edited
stationerys = ("Pens" , "Ink" , "Sharpener" , "Rubber" "Pencil")
print(stationerys)
#you cannot edit a tuple but you can replace the whole of it
for stationery in stationerys:
    print(stationery)

# 3)Dictionaries aka dict
#they use key and value pair eg "name" is the key, "Nathaniel" is the value
student = {"name" : "Nathaniel", "age" : 18, "gender" : "Male"}
print(student["name"])
print(student["age"])
print(student["gender"])
#create a dictonary with friends:fav_colour,hobby,course,team,height,weight
friend = {"colour" : "Pink" , "hobby" : "reading" , "course" : "Architecture" , "team" : "Liverpool" , "height" : 189}
print(friend["colour"]) 
print(friend["hobby"]) 
print(friend["course"]) 
print(friend["team"]) 
print(friend["height"]) 
print(student.values())
print(student.keys())