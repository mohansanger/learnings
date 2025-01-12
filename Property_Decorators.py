class celcius:
    def __init__(self, temp=0):
        self.temp=temp
    def farhenheit(self):
       return (self.temp*1.8)+32
    

human=celcius()
human.temp=30
print(human.temp)
print(human.farhenheit())
