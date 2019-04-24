#Jwaun Huntley
#4/16/19
#Problem 6

try:
    with open('file.log')as file:
        read_data = file.read()
except FileNotFoundError:
    print("File not found")
