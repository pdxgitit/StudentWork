# write three classes.  The first class should have one method that converts
# from Celcius to Fahrenheit.  The socond class should convert from Fahrenheit to
# Celcius.  The third class should import the two classes and ask for user input
# to convert from one temperature to another.

class celfar():
    def convert(self, temp):
        temp *= 1.8
        return temp + 32

assert celfar.convert(0) == 32
