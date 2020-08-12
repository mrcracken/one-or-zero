import random
from time import gmtime, strftime

arr01, arrRes = [0,1], []
sumOf0, sumOf1 = 0, 0

with open("input.txt", "r") as inputFile:
    count = inputFile.readline()

with open("logs.txt", "w") as f:
    for i in range (0, int(count)):
        arrRes.append(random.choice(arr01))
        f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ", i = " + str(i) + "\n")

for i in arrRes:
    if i == 0:
        sumOf0 = sumOf0 + 1 
    else:
        sumOf1 = sumOf1 + 1

with open("result.txt", "w") as resultFile:
    resultFile.write(strftime("Date: " + "%Y-%m-%d %H:%M:%S", gmtime()) + "\nCount = " + count + "\n")
    resultFile.write("Sum of 0 in % = " + str((100/int(count)) * sumOf0) + "\n")
    resultFile.write("Sum of 1 in % = " + str((100/int(count)) * sumOf1))
