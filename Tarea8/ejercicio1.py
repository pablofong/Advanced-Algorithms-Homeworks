#Reference 
#https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/
#https://www.geeksforgeeks.org/angle-between-a-pair-of-lines/
import matplotlib.pyplot as plt
from math import atan

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayPoint(self):
        print(f"({self.x}, {self.y})")


def lineLineIntersection(A, B, C, D):
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1 * (A.x) + b1 * (A.y)

    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2 * (C.x) + b2 * (C.y)

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return Point(10**9, 10**9)
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return Point(x, y)


def plot_line(p1, p2, color='blue'):
    x_values = [p1.x, p2.x]
    y_values = [p1.y, p2.y]
    plt.plot(x_values, y_values, marker='o', color=color)

def findAngle(M1, M2):
    PI = 3.14159265
    if 1 + M1 * M2 == 0:
        print("Error: Division by zero. Cannot calculate angle.")
        return None
    angle = abs((M2 - M1) / (1 + M1 * M2))
    ret = atan(angle)
    val = (ret * 180) / PI
    return round(val, 4)

# Given points
points = [
    [(5, 2), (3, 2)],
    [(-2, 3), (1, 2)],
    [(-2, -2), (3, 4)],
    [(10, 1), (2, 5)],
    [(3, 4), (5, 8)],
    [(-7, 3), (3, 5)],
    [(14, 4), (-14, 4)],
    [(8, 7), (3, 3)],
    [(-1, -1), (2, 5)],
    [(5, 4), (-3, 1)]
]

intersections = []

for i, (p1, p2) in enumerate(points):
    plot_line(Point(*p1), Point(*p2), color='blue')
    if i < len(points) - 1:
        intersection = lineLineIntersection(Point(*p1), Point(*p2), Point(*points[i + 1][0]), Point(*points[i + 1][1]))
        if intersection.x != 10**9 and intersection.y != 10**9:
            intersections.append(intersection)
            plt.plot(intersection.x, intersection.y, marker='x', color='red')

            slope1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
            slope2 = (points[i + 1][1][1] - points[i + 1][0][1]) / (points[i + 1][1][0] - points[i + 1][0][0])

            angle = findAngle(slope1, slope2)
            print(f"Angle between lines {i+1} and {i+2}: {angle} degrees")

print("Intersection Points:")
for point in intersections:
    point.displayPoint()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)
plt.show()

