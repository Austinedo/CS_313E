import math

##################################################
###########        Point           ###############
##################################################

class Point:
    # constructor with default values
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance(self, other):
        self.dist =  math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))
        return self.dist

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__(self, other):
        tol = 1.0 * (10 ** -6)
        return((abs(self.x - other.x) < tol) and \
               (abs(self.y - other.y) < tol) and \
               (abs(self.z - other.z) < tol))


##################################################
###########        Sphere          ###############
##################################################

class Sphere:
    
    # constructor with default values
    def __init__(self, x=0,y=0, z=0, radius = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(self.x, self.y, self.z)
        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return 'Center: (' + str(self.center ) + '), Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
    def area(self):
        return math.pi * 4 * (self.radius ** 2)

  # compute volume of a Sphere
  # returns a floating point number
    def volume(self):
        return math.pi * (4/3) * (self.radius ** 3)

  # determines if a Point is strictly inside the Sph    ere
  # p is Point object
  # returns a Boolean
    def is_inside_point(self, p):
        # Checks each individual dimension (x, y, z)
        if(self.center.distance(p) < self.radius):
            return True
        else:
            return False
                                                                        
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere(self, other):
        dist_centers = self.center.distance(other.center)
        if((dist_centers + other.radius) < self.radius):
            return True
        else:
            return False



##################################################
###########        Cube            ###############
##################################################

class Cube:
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
    def __init__(self, x = 0, y = 0, z = 0, side = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(self.x, self.y, self.z)
        self.side = float(side)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
    def __str__(self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + \
               '), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
    def area(self):
        return 6 * (self.side ** 2)

  # compute volume of a Cube
  # returns a floating point number
    def volume(self):
        return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
    def is_inside_point(self, p):
        if(self.center.distance(p) < self.side / 2):
            return True
        else:
            return False

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        dist_centers = self.center.distance(a_sphere.center)
        if(dist_centers + a_sphere.radius < self.side / 2):
            return True
        else:
            return False


#TODO! Here you do Test-Driven Implementation. First we have the tests and then we implement the actual methods. 
#  


# Implement this Method

  # determine if other Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
    def is_inside_cube(self, other):
         # implement here ...
        dist_center =  self.center.distance(other.center)
        max_dist = (self.side - other.side) / 2
        if dist_center + (other.side / 2) <= max_dist:
            return True
        else:
            return False


# Implement this Method
# Checks if two shapes, cubes or sphere have the same volume
    def has_same_volume(self, other) -> bool:
        # implement here ...
        shape1_volume = self.volume()
        shape2_volume = 0

        if isinstance(other, Cube):
            shape2_volume = other.volume()
        elif isinstance(other, Sphere):
            shape2_volume = other.volume()
        else: 
            raise ValueError('Not a supported shape type')
        
        if abs(shape1_volume - shape2_volume) <= 1e-6:
            return True
        else:
            return False
