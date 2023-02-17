age = 60
gender = "Male"
if (age < 18):
    print("You are still young")
else:
    print("You should get an ID")

#compound / multiple conditions
if((age > 30) & (gender == "Male")): 
    print("You qualify for a loan") 
else:
    print("No loan for you") 

fav_colour = "Blue"
age = 26
if (fav_colour == "Green") | (age <= 20):
    print("You can be my friend")
else:
    print("You are not my friend")