class Battery():
    def __init__(self, size=70):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270
