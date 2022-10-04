
class Temp:

    def getF(self):
        return self._temperatureF

    def setF(self, temp_fahrenheit):
        self._temperatureF = temp_fahrenheit
        self._temperatureC = (5/9) * (self._temperatureF - 32.0)

    def getC(self):
        return self._temperatureC

    def setC(self, temp_centigrade):
        self._temperatureC = temp_centigrade
        self._temperatureF = (9/5) * self._temperatureC + 32


    def __init__(self):
        self._temperatureF = None
        self._temperatureC = None

    temperatureF = property(getF, setF)
    temperatureC = property(getC, setC)

bob = Temp()
print(bob.temperatureF)
bob.temperatureF = 212
print(f'{bob.temperatureC} degrees Centigrade')
print(f'{bob.temperatureF} degrees Fahrenheit')


