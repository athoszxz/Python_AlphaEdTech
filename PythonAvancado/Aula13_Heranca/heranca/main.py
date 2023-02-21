from typing import List


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
            print("Triangle is equilateral")
            return (a ** 2 * 3 ** 0.5) / 4
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("Triangle is isosceles")
            s = sum(self.sides)/2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        else:
            print("Triangle is scalene")
            s = sum(self.sides)/2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def main():
    triangle = Triangle([5, 5, 5])
    print(triangle.display_sides())
    print(triangle.find_area())


if __name__ == '__main__':
    main()
