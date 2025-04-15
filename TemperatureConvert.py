temp = 0

print("Please select temperature: ")
print("1: Celeius")
print("2: Fahrenheit")
num = int(input())

if num == 1:
    print("Please enter the number of degrees in Celeius")
    degree = int(input())
    temp = (1.8*degree) + 32
    print("New Temperature in Fahrenheit is: ", round(temp),"F")

else:
    print("Please enter the number of degrees in Fahrenheit")
    degree = int(input())
    temp = (degree - 32) * (5/9)
    print("New Temperature in Celeius is: ", round(temp),"C")
