
#Reference 
#https://www.geeksforgeeks.org/convex-hull-using-graham-scan/
import matplotlib.pyplot as plt
from math import atan2

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(points):
    n = len(points)
    if n < 3:
        return points

    pivot = min(points, key=lambda point: (point[1], point[0]))

    sorted_points = sorted(points, key=lambda point: (atan2(point[1] - pivot[1], point[0] - pivot[0]), point))

    stack = [pivot, sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])

    return stack

def plot_points_and_convex_hull(points, convex_hull):
    x, y = zip(*points)
    plt.scatter(x, y, color='blue', label='Puntos')
    
    x_hull, y_hull = zip(*convex_hull + [convex_hull[0]])  # Agregar el primer punto al final para cerrar el casco
    plt.plot(x_hull, y_hull, color='red', linestyle='-', linewidth=2, label='Casco Convexo')

    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


points = [(-19, -17), (-15, 3), (-12, 11), (-8, -5), (-7, 14), (-3, -9), (-1, 0), (2, 18), (4, -13), (6, 7),
          (9, -16), (11, 5), (13, -2), (16, 12), (18, -7), (-20, 6), (-14, -18), (-9, 9), (-4, -12), (-2, 15),
          (1, -14), (3, 10), (7, -8), (12, 19), (17, -4)]
convex_hull = graham_scan(points)
plot_points_and_convex_hull(points, convex_hull)
