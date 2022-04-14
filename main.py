from shapely.geometry import Polygon

def is_inside(polyA, polyB):
    return polyA.contains(polyB)

def perimeter(poly):
    return poly.length


# def is_concave():
    
p = Polygon([(0, 0), (0, 2), (2, 2), (2,0)])
o = Polygon([(0, 0), (0, 1), (1, 1)])

# print("Poligono: " + p.str)