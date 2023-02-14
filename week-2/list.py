names = ["Nathaniel" , "Njenga" , "Änne" , "Marie"] 
#accessing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
fruits = ["Mango" , "Banana" , "Pomagranate" , "Apple" , "Guava" , "Pawpaw" , "Orange" , "Kiwi"]
print(fruits)
print(fruits[3])
print("My favourite fruit is :",(fruits[3].upper()))
vegetables = ["spinach" , "managu" , "cauliflower" , "lettuce"]
stationery = ["pens" , "ink" , "paper" , "glue" , "scissors" , "rubber"]
shoppings = vegetables + stationery
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("My name is " + names[0] + "and my favourite fruit is " + fruits[3])