class DistanceConversion:
    print("Distance Converter")

    def __init__(self, meter):
        self.meter = float(input("Enter meter: "))

    def meter_to_Cm(self):
        return ((self.meter * 100))
    def meter_to_Km(self):
        return ((self.meter / 1000))
    def meter_to_In(self):
        return ((self.meter * 39.7))

    def display(self):
        print("Outputs : ")
        print('Inputted meter to Centimeter is :', self.meter_to_Cm() ,'cm')
        print('Inputted meter to Kilometer is :', self.meter_to_Km(), 'km')
        print('Inputted meter to Inches is :', self.meter_to_In(), 'in')

convert = DistanceConversion('meter')
convert.display()