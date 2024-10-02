#Brentley Dorsainvil
#U19000123
#User will input numbers that will be used to find the perimeter and area of a polygon


import math

class Polygon:
    def __init__(self):
        self.__side = 0
        self.__length = 0.0

    def getside(self):
        return self.__side

    def getlength(self):
        return self.__length

    def setside(self,side):
        self.__side = side

    def setlength(self,length):
        self.__length =  length

    def Perimeter(self):
        return self.__side * self.__length

 


    def area(self):
        return  (self.__side * self.__length ** 2) / (4 * math.tan(math.pi / self.__side))
        

def main():
    polygon = Polygon()

    while True:
        userinput = float(input('Enter the number of sides (>=3):'))

        if userinput >= 3:
            break
        print('Invalid entry. Re-enter the number of sides (>=3):')

    polygon.setside(userinput)
    


    while True:
        user_length = float(input('Enter the length of each side (>=0.1): '))
        if user_length >= 0.1:
            break
        print('Invalid entry. Re-enter the length of each side (>=0.1).')

    polygon.setlength(user_length)

    print(f'The polygon has {polygon.getside()} sides. Each side is {polygon.getlength()} units in length.')
    print(f'The perimeter of the polygon is {polygon.Perimeter():.3f} units and its area is {polygon.area():.3f} square units.')


main()
    
    
    






























        
        
