# abc + abstractmethod + pass (abstract + override + virtual)

# from abc import ABC, abstractmethod
#
# class Shape(ABC):   # Abstract Base Class
#     @abstractmethod
#     def draw(self):  # Must be implemented in child
#         pass         # Placeholder
#
#     def info(self):  # Normal method
#         print("This is a shape.")
#
# class Circle(Shape):
#     def draw(self):
#         print("Drawing Circle.")

from abc import ABC, abstractmethod  # abc = Abstract Base Class

class Shape(ABC):  # Abstract class
    @abstractmethod
    def draw(self):
        pass

    def info(self):
        print("This is a shape.")


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")


shape = Circle()
shape.draw()  # Output: Drawing a Circle.
shape.info()  # Output: This is a shape.