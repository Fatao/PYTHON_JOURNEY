
# calculating for the area of a triangle
def triangle_area(base, height):
    area = 1/2 * base * height
    return area

def area_triangle():
    """
    Calculates the area of a triangle with base of 4 and height of 6
    :return: The area of the triangle
    """
    base = 4
    height = 6
    
    area = 1/2 * base * height
    
    return area
    
print(area_triangle())
