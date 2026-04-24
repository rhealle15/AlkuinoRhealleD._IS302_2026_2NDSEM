import math

class Shape_rda:
    def area_rda(self_rda):
        pass  # Placeholder for polymorphism

class Rectangle_rda(Shape_rda):
    def __init__(self_rda, width_rda, height_rda):
        self_rda.width_rda = width_rda
        self_rda.height_rda = height_rda

    def area_rda(self_rda):
        return self_rda.width_rda * self_rda.height_rda

class Circle_rda(Shape_rda):
    def __init__(self_rda, radius_rda):
        self_rda.radius_rda = radius_rda

    def area_rda(self_rda):
        return math.pi * self_rda.radius_rda ** 2

class Triangle_rda(Shape_rda):
    def __init__(self_rda, base_rda, height_rda):
        self_rda.base_rda = base_rda
        self_rda.height_rda = height_rda

    def area_rda(self_rda):
        return 0.5 * self_rda.base_rda * self_rda.height_rda

# Example usage
rectangle_rda = Rectangle_rda(10, 5)
circle_rda = Circle_rda(5)
triangle_rda = Triangle_rda(8, 6)

print(f"Rectangle Area: {rectangle_rda.area_rda()}")
print(f"Circle Area: {circle_rda.area_rda():.1f}")
print(f"Triangle Area: {triangle_rda.area_rda()}")
