import csv
import math
with open('Class1.csv', newline = '') as f:
    reader = csv.reader(f)
    fData = list(reader)
    data = fData[1]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

slist = []
for n in data:
    a = int(n) - mean(data)
    a = a **2
    slist.append(a)

sum = 0
for i in slist:
    sum += i
result = sum/len(data) - 1

std = math.sqrt(result)
print(std)