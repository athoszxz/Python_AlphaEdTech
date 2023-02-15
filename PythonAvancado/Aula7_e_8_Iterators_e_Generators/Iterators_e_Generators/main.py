from typing import Generator


def count_up(x: int) -> Generator[int, None, None]:
    n = 1
    diff = 1
    while n < x:
        yield n
        n += n - (n - diff)
        diff += 1


for num in count_up(67):
    print(num)
