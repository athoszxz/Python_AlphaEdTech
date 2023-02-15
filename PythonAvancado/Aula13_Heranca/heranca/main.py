from typing import List
import math


class Polygon:
    def __init__(self, sides: List[float]):
        self.sides = sides

    def display_sides(self) -> List[float]:
        return self.sides


class Triangle(Polygon):
    def __init__(self, sides: List[float]):
        super().__init__(sides)

    def find_area(self) -> float:
        a, b, c = self.sides
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid triangle sides')
        if a == b == c:
            return (a ** 2 * 3 ** 0.5) / 4
        else:
            s = sum(self.sides)
            return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    triangle = Triangle([5, 5, 7])
    print(triangle.display_sides())
    print(triangle.find_area())


if __name__ == '__main__':
    main()
