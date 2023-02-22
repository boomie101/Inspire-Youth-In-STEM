#using for_loop draw a diamond,triange and pascals triangle
diamonds = ["   *   " , "  * * " , " * * *" , "* * * *"]
for diamond in diamonds:
    print(diamond)
diamonds.pop()
diamonds.reverse()
for diamond in diamonds:
    print(diamond)
print("                                               ")
#triangle
triangles = ["   *   " , "  * * " , " * * *" , "* * * *"]
for triangle in triangles:
    print(triangle)