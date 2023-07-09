class Car():
    """description of the car"""

    def __init__(self, color, horsepower):
        """car properties"""
        self.color = color
        self.horsepower = horsepower

    def start(self):
        """car starts"""
        print(f'{self.color} car with {self.horsepower} horsepower started up')


Car1 = Car('black', 612)

Car1.start()
