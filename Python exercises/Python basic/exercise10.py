# calculate the sum of number from user n + nn + nnn
num = int(input("Entert a number: "))

num1 = int("%d" %num)
num2 = int("%d%d" %(num, num))
num3 = int("%d%d%d" %(num, num, num))

calculate = num1 + num2 + num3

print("Your caculate " + str(num1) + " + " + str(num2) + " + " + str(num3) + " = " + str(calculate))
