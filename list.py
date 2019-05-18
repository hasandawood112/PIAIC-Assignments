import random 

number = []

for num in range (100):
    n = random.randint(1, 1000)
    number.append(n)
print("This list is consist of 100 random numbers: ", number)

total = 0

for i in number :
    total += i
mean = total/100

maximum = max(number)
minimum = min(number)
maxInd = number.index(maximum)
minInd = number.index(minimum)

print("\n---------------------------------------------------------")
print("| Maximum number is : ", maximum, "\t Max Index : ", maxInd, "\t|")
print("| Minimum number is : ", minimum, "\t Max Index : ", minInd, "\t|")
print("---------------------------------------------------------")
