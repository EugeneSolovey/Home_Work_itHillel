from __future__ import annotations


coord_1 = (2, 3)
coord_2 = (-1, 5)


error_message = "can not divide by zero"

#print("Error:", error_message)

# Concatenation
#print("Error: " + error_message)

# Formatting
#print("Error: ({}) {}".format(type(error_message), error_message))
#print(f"Error: ({type(error_message)}) {error_message}")


# to add in procedural paradygm:
# (coord_1[0] + coord_2[0]) + (coord_1[1] + coord_2[1])


# in OOP

# pep8 specifies class name in CamelCase (but variables in snake_case)

class Point2D(object):

    def __init__(self, x_value: int, y_value: int) -> None:
        self.x = x_value  # x = x_value
        self.y = y_value  # y = y_value

    def __repr__(self) -> str:
        return f"Point2D({self.x=}, {self.y=})"

    def __add__(self, other) -> Point2D:
        try:
            new_x = self.x + other.x
            new_y = self.y + other.y
        except AttributeError:
            return NotImplemented
        return Point2D(x_value=new_x, y_value=new_y)

    # Less than ...
    def __lt__(self, other) -> bool:
        return self.x < other.x or self.y < other.y

    # def __str__(self) -> str:
    #     pass

    def draw(self, color: str) -> None:
        print(f'Point2D ({self.x}, {self.y}) is drawn in {color}')


zero_point = Point2D(0, 0)
# print(zero_point, type(zero_point))
#print(f"{zero_point.x} {zero_point.y}")

one_point = Point2D(1, 1)
print(one_point)

print(f"{one_point.x} {one_point.y}")

half_point = zero_point + one_point
print(f"{half_point = }")

print(Point2D(10, 5) + Point2D(5, 10))

point_list = [zero_point, half_point, one_point]
print(sorted(point_list, reverse=True))


class Point3D:

    def __init__(self, x: int, y: int, z: int = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other) -> Point3D:
        try:
            new_x = self.x + other.x
            new_y = self.y + other.y
        except AttributeError:
            return NotImplemented
        try:
            return Point3D(x=new_x, y=new_y, z=(self.z + other.z))
        except AttributeError:
            return Point3D(x=new_x, y=new_y, z=self.z)

    def __repr__(self) -> str:
        return f"Point3D({self.x=}, {self.y=}, {self.z=})"

point_3d = Point3D(5, 10, -5)
print(f'{zero_point + point_3d = }')
print(f'{point_3d + zero_point = }')


# Unsupported type error:
# 2 objects :
# - NotImplemented - object
# - NotImplementedError - exceptions

#print(zero_point + 4)
#print(zero_point + "abracadabra")


class Car:

    def tow(self, towing_vehicle) -> None:
        print(f"Towed by {towing_vehicle}!")
