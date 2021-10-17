import os
import sys
import json

class Fraction:
    minimum_balance = 50000

    def __init__(self, nr, dr):
        self.nr = nr
        self.dr = dr
        
    @property
    def nr(self):
        return self._nr

    @property
    def dr(self):
        return self._dr

    @nr.setter
    def nr(self, nr):
        self._nr = nr
        
    @dr.setter
    def dr(self, dr):
        if dr == 0:
            raise ValueError("Dr không hợp lệ, Dr phải khác 0")
        elif dr < 0:
            dr = abs(dr)
            self.nr = -self.nr
        self._dr = dr

    def display(self):
        if self.nr == 0: 
            print(0)
        elif self.dr == 1:
            print(self.nr)
        else:
            print(f"{self.nr}/{self.dr}")

    def hcf(self):
        x, y = abs(self.nr), abs(self.dr)
        hcf = x if x < y else y

        while hcf > 0:
            if x % hcf == 0 and y % hcf == 0:
                break

            hcf -= 1

        return hcf if hcf > 0 else None


    def reduce(self):
        n = self.hcf()

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)

   

fr = Fraction(2, -6)
fr.display()
fr.reduce()
fr.display()

