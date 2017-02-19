import numpy
import stl
from stl import mesh
import math

def rotate(filename):
    """rotates an stl mesh 90 degrees about the x axis"""

    main_body = mesh.Mesh.from_file(filename)

    main_body.rotate([0.5, 0.0, 0.0], math.radians(90))

    main_body.save('rotated_' + filename)

if __name__ == '__main__':
    rotate('tea_stuff.stl')
