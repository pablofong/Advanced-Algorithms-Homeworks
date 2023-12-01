import numpy as np

points3D = np.array([[0, 0.71934, 0.694658], [-0.71934, 0, 0.694658], [0, 0, 1], [0.71934, 0, 0.694658],
                     [0, -0.71934, 0.694658], [-0.587427, -0.808524, -0.0348995], [0, -0.999391, -0.0348995],
                     [0.587427, -0.808524, -0.0348995]])

# Function to calculate the angle between two vectors
def calculate_angle(u, v):
    cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    return angle_deg

# Calculate angles between consecutive vectors
angles = []
for i in range(len(points3D) - 1):
    angle = calculate_angle(points3D[i], points3D[i + 1])
    angles.append(angle)

# Print the angles
for i, angle in enumerate(angles, start=1):
    print(f"Angle between points {i} and {i + 1}: {angle:.2f} degrees")
