from cohenherbert import rect_surface_area

length = int(input("Enter the length of the object as an integer: "))
width = int(input("Enter the width of the object as an integer: "))
height = int(input("Enter the height of the object as an integer: "))

surface_area = rect_surface_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)