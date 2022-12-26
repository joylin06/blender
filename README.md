# Identifying Optimal Tracker locations for 360 Camera View

The goal is to identify the largest group of faces that are “similar” to one another. 
Two faces are to be considered “similar” if the angle of their normal vectors differs within a certain degree or radians. 
This degree can be changed, but I discovered that a difference of 30 degrees (0.523599 radians) is an appropriate measure.

Intuitively, it would make sense to add a tracker onto large areas of similar faces.
However, depending on the marker shape, one would later determine what areas are deemed most effective.

An example of this code working is shown below: 

https://youtu.be/X00ZEfOocXA
