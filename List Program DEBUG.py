current = []
power = []
resistors = []
CurrentSum = 0
PowerSum = 0
resistance = [16, 27, 39, 56, 81]
for i in range(5):
    currentAmount = eval(input("Enter current value: "))
    current.append(currentAmount)
    powerAmount = resistance[i] * current[i]**2
    power.append(powerAmount)
    print("Resistance \t Current \t Power")
    print(resistance[i], "\t", current[i], "\t", power[i])

for x in range(5):
    print(resistance[x], "\t\t", current[x], "\t\t", power[x], "\n")
    CurrentSum += current[x]
    PowerSum += power[x]
    print("Total: \t\t", CurrentSum, "\t\t", PowerSum)
