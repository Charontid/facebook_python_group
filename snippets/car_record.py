#Just a Small Example for the DataModel methods:
#__str__
#__repr__

def main():
    s = "2009'ABC123'"

    car = CarRecord(s)
    print(car.__str__())
    print(car.__repr__())


class CarRecord:
    def __init__(self, s):
        self.production_year = None
        self.vin = None


        year, vin, _ = s.split("'")
        self.production_year = year
        self.vin = vin


    def __str__(self):
        return f"Year: {self.production_year}, VIN: {self.vin}"

    def __repr__(self):
        s = f"{self.production_year}'{self.vin}'"
        return f"CarRecord({s})"


if __name__ == '__main__':
    main()
