from shapely.geometry import Polygon

def is_inside(polyA, polyB):
    return polyA.contains(polyB)

def perimeter(poly):
    return poly.length

def coordinates(poly):
    return poly.exterior.coords[:-1]

def cross_product(A):
    # Stores coefficient of X
    # direction of vector A[1]A[0]
    X1 = (A[1][0] - A[0][0])
    # Stores coefficient of Y
    # direction of vector A[1]A[0]
    Y1 = (A[1][1] - A[0][1])
    # Stores coefficient of X
    # direction of vector A[2]A[0]
    X2 = (A[2][0] - A[0][0])
    # Stores coefficient of Y
    # direction of vector A[2]A[0]
    Y2 = (A[2][1] - A[0][1])
    # Return cross product
    return (X1 * Y2 - Y1 * X2)
def get_shape_type(polygon):
    # Stores count of
    # edges in polygon
    points = coordinates(polygon)
    N = len(points)
 
    # Stores direction of cross product
    # of previous traversed edges
    prev = 0
 
    # Stores direction of cross product
    # of current traversed edges
    curr = 0
 
    # Traverse the array
    for i in range(N):
        
        # Stores three adjacent edges
        # of the polygon
        temp = [points[i], points[(i + 1) % N],
                           points[(i + 2) % N]]
 
        # Update curr
        curr = cross_product(temp)
 
        # If curr is not equal to 0
        if (curr != 0):
            # If direction of cross product of
            # all adjacent edges are not same
            if (curr * prev < 0):
                return "concavo"
            else:
                # Update curr
                prev = curr
 
    return "convexo"

def input_poly():
    try:
        n = int(input("Introduce el número de puntos: "))
        points = []
        for i in range(n):
            x = int(input("Introduce la coordenada x" + str((i+1)) + ": "))
            y = int(input("Introduce la coordenada y" + str((i+1)) + ": "))
            points.append((x,y))
        return Polygon(points)
    except ValueError:
        print("Puntos no válidos")
        exit(0)

def choose_operation():
    print("Crea un polígono:")
    poly1 = input_poly()
    print()

    while(True):
        print("Elige una operación:")
        print("1) Calcular perimetro")
        print("2) Concavo/Convexo")
        print("3) Contiene")
        print("4) Salir")
        operacion = input()
        print()

        if operacion == "1":
            print("Perímetro: " + str(perimeter(poly1)))
        elif operacion == "2":
            print("El polígono es: " + get_shape_type(poly1))
        elif operacion == "3":
            print("Crea otro polígono:")
            poly2 = input_poly()
            contiene = is_inside(poly1, poly2)
            print()

            if contiene:
                print("El polígono1 contiene el polígono2")
            else:
                print("El polígono1 no contiene el polígono2")
        else:
            print("Saliendo...")
            exit(0)
        print()

#p = Polygon([(0, 0), (0, 2)])
# o = Polygon([(0, 0), (0, 1), (1, 1)])

choose_operation()