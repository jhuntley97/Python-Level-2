#Jwaun Huntley
#04/23/2019


def fac(number):
    if number <1:
        return 1
    else:
        return number * fac(number - 1)

print(fac(9))
