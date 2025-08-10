class Train:
    fare = None
    totalSeats = None
    available = None

    def __init__(self, fare, totalSeats):
        self.fare = fare
        self.totalSeats = totalSeats
        self.available = totalSeats

    def bookSeat(self):
        if self.available:
            self.available -= 1

t1 = Train(500, 220)
t1.bookSeat()

print(t1.available)