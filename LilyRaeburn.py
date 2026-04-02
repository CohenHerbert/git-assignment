#define the rect_surface_area
def rect_surface_area(length, width, height):
#call on the rect_area function
    l_w = rect_area(length, width)
    l_h = rect_area(length, height)
    w_h = rect_area(width, height)
    surface_area = 2 * (l_w + l_h + w_h)
    return surface_area
#ask for user input of integers
length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
#calculate surface area with the user input
final_ans = rect_surface_area(length, width, height)
#print the user's inputs for length, width, and height
print(f"Length: {length}\nWidth: {width}\nHeight: {height}")
#print the final answer of surface area
print(f"Surface Area: {final_ans}")
