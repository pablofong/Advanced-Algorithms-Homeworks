#https://homepages.math.uic.edu/~jan/mcs481/rangesearch.pdf
import random

class RangeTree:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def build_range_tree(points, dimension=0):
    if not points:
        return None

    points.sort(key=lambda p: p[dimension])
    
    mid = len(points) // 2
    node = RangeTree(points[mid])
    
    next_dimension = (dimension + 1) % len(points[0])
    
    node.left = build_range_tree(points[:mid], next_dimension)
    node.right = build_range_tree(points[mid + 1:], next_dimension)
    
    return node

def range_query(node, start, end, dimension=0, result=[]):
    if node is None:
        return result

    point = node.point

    if start <= point[dimension] <= end:
        result.append(point)

    if start < point[dimension]:
        range_query(node.left, start, end, (dimension + 1) % len(point), result)
    if end > point[dimension]:
        range_query(node.right, start, end, (dimension + 1) % len(point), result)

    return result

random_values = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(2000)]
bottom_up_range_tree = build_range_tree(random_values)

search_ranges = [(-10, -9.3) , (-5, -4) , (-1, -0.5), (2, 4), (9, 9.5)]

for start, end in search_ranges:
    result = range_query(bottom_up_range_tree, start, end)
    print(f"Values in range ({start}, {end}):\n{result}\n")
