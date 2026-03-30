#variables
#H
try:
    length = int(input("Enter the length of the the object as a integer: "))
    width = int(input("Enter the width of the the object as a integer: "))
    height = int(input("Enter the height of the the object as a integer: "))
except:
    ValueError
    print("Invalid Input")

#Function 1
# Returns Area of Rectangle
#H
def rect_area(length, width):
    a = length*width
    return a


#Function 2
# Returns Surface Area of Rectangular Solid


# Request the dimension of a solid rectangular object
#H
try:
    print (f"Length = {length} Width = {width} Height = {height}")
    print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
    print("Area of the rectangle: " + str(rect_area(length, width)))
except:
    NameError
    
