# REFERENCE https://www.geeksforgeeks.org/search-and-insertion-in-k-dimensional-tree/
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if len(points) == 0:
        return None

    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda x: x[axis])

    mid = len(points) // 2
    node = Node(points[mid], axis)

    node.left = build_kd_tree(points[:mid], depth + 1)
    node.right = build_kd_tree(points[mid + 1:], depth + 1)

    return node

points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(200)]
kd_tree = build_kd_tree(points)

ranges = [
    ([-1, 1], [-2, 2]),
    ([-2, 1], [3, 5]),
    ([-7, 0], [-6, 4]),
    ([-2, 2], [-3, 3]),
    ([-7, 5], [-3, 1])
]

colors = ['red', 'blue', 'green', 'orange', 'purple']

for i, point in enumerate(points):
    x, y = point

    if -1 < x < 1 and -2 < y < 2:
        plt.scatter(x, y, c=colors[0], label=f'Range 1' if i == 0 else '')
    elif -2 < x < 1 and 3 < y < 5:
        plt.scatter(x, y, c=colors[1], label=f'Range 2' if i == 0 else '')
    elif -7 < x < 0 and -6 < y < 4:
        plt.scatter(x, y, c=colors[2], label=f'Range 3' if i == 0 else '')
    elif -2 < x < 2 and -3 < y < 3:
        plt.scatter(x, y, c=colors[3], label=f'Range 4' if i == 0 else '')
    elif -7 < x < 5 and -3 < y < 1:
        plt.scatter(x, y, c=colors[4], label=f'Range 5' if i == 0 else '')
    else:
        plt.scatter(x, y, c='black', label='Outside Ranges' if i == 0 else '')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
