import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

points = np.array([[9, 7], [1, 3], [7, 2], [1, 9], [5, 4]])

triangulation = Delaunay(points)

# Delaunay
plt.triplot(points[:,0], points[:,1], triangulation.simplices, color='blue')
plt.plot(points[:,0], points[:,1], 'o', color='red', label='Points')
plt.title('Triangulacion Delaunay')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

# Voronoi 
vor = Voronoi(points)

voronoi_plot_2d(vor, show_vertices=False, line_colors='blue', line_width=2, line_alpha=0.6, point_size=10, show_points=True)
plt.title('Diagrama Voronoi')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()