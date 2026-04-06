def rect_area(length, width):
    return length * width

def rect_surface_area(length, width, height):
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))