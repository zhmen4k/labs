from typing import Self
import math

class Complex:
    def __init__(self, _re: float = 0., _im: float = 0.) -> None:
        self.__re = _re
        self.__im = _im


    @property
    def real(self) -> float:
        return self.__re

    @real.setter
    def real(self, val: float) -> None:
        self.__re = val

    @property
    def imaginary(self) -> float:
        return self.__im

    def __str__(self) -> str:
        return f"{self.real} {'+' if self.imaginary >= 0 else '-'} {abs(self.imaginary)}*i"

    def __add__(self, other: Self) -> Self:
        return Complex(self.__re + other.real, self.__im + other.imaginary)

    def __iadd__(self, other: Self) -> Self:
        self.__re += other.real
        self.__im += other.imaginary
        return self

    def __sub__(self, other: Self) -> Self:
        return Complex(self.__re - other.real, self.__im - other.imaginary)

    def __isub__(self, other: Self) -> Self:
        self.__re -= other.real
        self.__im -= other.imaginary
        return self


    def __mul__(self, other: Self) -> Self:
        return Complex(self.__re * other.real - self.__im * other.imaginary, self.__re * other.imaginary + self.__im * other.real)

    def __imul__(self, other: Self) -> Self:
        re = self.__re * other.real - self.__im * other.imaginary
        im = self.__re * other.imaginary + self.__im * other.real
        self.__re = re
        self.__im = im
        return self

    def __truediv__(self, other: Self) -> Self:
        return Complex((self.__re * other.real + self.__im * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
                       (self.__im * other.real - self.__re * other.imaginary) / (other.real ** 2 + other.imaginary ** 2))

    def __itruediv__(self, other: Self) -> Self:
        re = (self.__re * other.real + self.__im * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        im = (self.__im * other.real - self.__re * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        self.__re = re
        self.__im = im
        return self


    def __abs__(self) -> float:
        return math.sqrt(self.__re ** 2 + self.__im ** 2)

    def __eq__(self, other: Self) -> bool:
        return self.__re == other.real and self.__im == other.imaginary

    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)

