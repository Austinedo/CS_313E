# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Austine Do

# Student UT EID: ahd589

# Course Name: CS 313E

# Unique Number: 52590

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist(self, other):
    return math.sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))


class Triangle (object):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.point_A = PointA
        self.point_B = PointB
        self.point_C = PointC

    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):
        self_sides = {self.point_A.dist(self.point_B), 
                      self.point_A.dist(self.point_C), 
                      self.point_B.dist(self.point_C)}
        
        other_sides = {other.point_A.dist(other.point_B), 
                       other.point_A.dist(other.point_C), 
                       other.point_B.dist(other.point_C)}
        
        if self_sides == other_sides:
           return True
        
        return False
        
    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
        a = self.point_A.dist(self.point_B)
        b = self.point_A.dist(self.point_C)
        c = self.point_B.dist(self.point_C)

        return (a + b > c) and (a + c > b) and (b + c > a)
           

    # return the area of the triangle:
    def area(self):
       return abs(((self.point_A.x * (self.point_B.y - self.point_C.y)) +
                         (self.point_B.x * (self.point_C.y - self.point_A.y)) + 
                         (self.point_C.x * (self.point_A.y - self.point_B.y))) / 2)

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
