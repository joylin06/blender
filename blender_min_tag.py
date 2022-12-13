import bpy
import bmesh
import mathutils
import random
from math import degrees,pi


obj = bpy.context.edit_object
me = obj.data

bm = bmesh.from_edit_mesh(me)

area = dict()

for face in bm.faces:
    face.select = True
    bpy.ops.mesh.faces_select_linked_flat(sharpness=0.523599)
    group = [f for f in bm.faces if f.select]
    size = 0
    for f in bm.faces:
        if f.select:
            size += f.calc_area()
    if (size,group) not in list(area.values()):
        area[face] = (size,group)
    bpy.ops.mesh.select_all(action='DESELECT')

print(len(area))
print(area)

out = list(area.values())
out.sort(key=lambda y: y[0],reverse = True)
print(*out, sep = "\n")

bpy.ops.mesh.select_all(action='DESELECT')

def show_n_largest(out,n):
    """
    input: 
    out (list of tuples)
        n(int) representing the nth largest patch
    return: selected faces representing the nth largest patch of mesh faces
    """
    for face in out[n][1]:
        face.select = True
    bmesh.update_edit_mesh(me)
    
def min_marker(out,a):
    """
    input: 
        out(list of tuples)
        a(float) representing the minimum area of a patch
    output: returns an integer representing the number of minimum markers and sublist of out
    (calculated through determining the num of large patches of surface area)
    """
    if len(out) == 0:
        raise Exception("no grouped faces")
    val = []
    count = 0
    for i in out:
        if i[0] > a:
            count += 1
            val.append(i)
        else:
            return (count, val)
    return (count, val)

#for i in range(6):
show_n_largest(out,0)
    
#print(min_marker(out,1))


#x = (min_marker(out,0.8))
#for i in range(x[0]):
#    show_n_largest(out,i)