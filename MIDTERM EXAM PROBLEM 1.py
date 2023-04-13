class Circle():

    def radius(self,radius):
        rad = radius
    def area(self,rad):
        area = 3.142*rad*rad
        print("Area of the circle is: ", area)
    def peri(self,rad):
        peri = 2*3.14*rad
        print("Perimeter of the circle is: ",peri)

c = Circle()
radius = int(input("Enter the radius of circle: "))
c.area(radius)
c.peri(radius)