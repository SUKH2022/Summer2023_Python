phoneDict = {"Madison":"705-111-2222", "Tim":"705-222-3333", "Stephanie":"705-333-4444"}

dictList = list(phoneDict.items())

for (key, value) in dictList:
    print(key, value)

phoneDict["Madison"] = "1-800-999-8888"

phoneDict["Bertha"] = "1-988-000-1222"

print(phoneDict["Stephanie"])

print("Tim" in phoneDict)

phoneDict.pop("Madison")
phoneDict.pop("Geralt", -1)

# Prints in an unknown order
for entry in phoneDict:
    print(phoneDict[entry])

summerClasses = ["COMP1111-01", "COMP1112-01", "COMP1112-02", "COMP1099-01", "COMP1011-01"]

summerClasses.append("COMP9999-09")

summerClasses.extend(["COMP8888-08", "COMP7777-07"])

summerClasses.insert(3, "COMP4040-04")

summerClasses.sort()

print(summerClasses[0])

print(summerClasses[4])

print(summerClasses[-1])

print(len(summerClasses))

print(summerClasses[1:3])

# Looping over a list and editing values requires you use an index to access the elements!
for i in range(len(summerClasses)):
    summerClasses[i] = "TEST"

lastValue = summerClasses.pop()
summerClasses.pop()
print(lastValue)

myString = "Hello"

myString[1] = "x"

myStringList = ['H', 'e', 'l', 'l', 'o']

myStringList[1] = 'x'