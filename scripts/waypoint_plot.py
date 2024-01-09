# Script to plot the numpy waypoints (route file) in Blender to validate the
# position of the waypoints against the visual track.
# 
# Load file into Script tab in Blender, change path below and run.
#
# Script provided by Jason K.

import bpy
import numpy as np

# Load data from file
data = np.load('<path to NUMPY>')
# Extract vertices of triangles
vertices = data.reshape(-1, 3, 2)
vertices = np.concatenate(
    (vertices, np.zeros((vertices.shape[0], 3, 1))), axis=2)
# Create mesh and object
mesh = bpy.data.meshes.new("MyMesh")
obj = bpy.data.objects.new("MyObject", mesh)
# Create vertices and faces
verts = vertices.reshape(-1, 3)
faces = np.arange(len(verts)).reshape(-1, 3)
# Set vertex positions
mesh.from_pydata(verts.tolist(), [], faces.tolist())
# Create a small sphere at each vertex location
for vert in verts:
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.02, enter_editmode=False, location=vert)
    # Get the material for the sphere
    mat = bpy.data.materials.new(name="MyMaterial")
    mat.diffuse_color = (1, 0, 0, 1)  # Set the color to red
    # Assign the material to the sphere
    sphere = bpy.context.object
    sphere.data.materials.append(mat)
# Link object to scene
bpy.context.scene.collection.objects.link(obj)
