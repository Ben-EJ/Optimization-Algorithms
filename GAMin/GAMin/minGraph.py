import matplotlib.pyplot as plt
import numpy as np
import csv

GenMin = 0
GenMax = 50

def popGen():
    data = []
    for i in range(GenMin, GenMax):
        data.append(i)
    return data[::-1]

def csvIn():
    with open("DataMin.csv", "r") as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        csvData = list(csv_reader1)
        csvData[0].pop()
    return csvData[0][::-1]

xpoints = np.array(popGen())
ypoints = np.array(csvIn())

plt.plot(xpoints, ypoints)
plt.show()