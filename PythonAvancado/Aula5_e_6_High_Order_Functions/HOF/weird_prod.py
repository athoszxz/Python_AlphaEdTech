from functools import reduce
from typing import List


def weird_prod(numbers: List[int]) -> int:
    """Return the product of the first and the square of the next and the cube
    of the next and so on."""
    return reduce(lambda x, y: x * y ** (numbers.index(y) + 1), numbers, 1)


print(weird_prod([1, 2, 3, 4, 5]))
