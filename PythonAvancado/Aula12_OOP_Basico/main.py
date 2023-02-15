class Trip:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

    def __add__(self, other: "Trip") -> "Trip":
        return Trip(self.start, other.end)

    def __str__(self):
        return f"Trip from {self.start} to {self.end}"


if __name__ == "__main__":
    trip1 = Trip("London", "Paris")
    trip2 = Trip("Paris", "Berlin")
    trip3 = Trip("Berlin", "Rome")
    trip3 = trip1 + trip2 + trip3
    print(trip3)
