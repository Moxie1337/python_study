class Temperature:
    def __init__(self):
        self._temp_fahr = 0

    @property # make instance can be find
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9

    @temp.setter # make instance variable changeable
    def temp(self, new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32


t = Temperature()
print(t._temp_fahr)

print(t.temp)

t.temp = 34

print(t._temp_fahr)

print(t.temp)