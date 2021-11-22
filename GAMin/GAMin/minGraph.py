
import matplotlib.pyplot as plt
import numpy as np
import csv
global Gen
global N
global Pop
global MUTRATE
global MUTSTEP

with open("DataMin.csv", "r") as csv_file1:
    csvData = []
    csv_reader1 = csv.reader(csv_file1)
    csvData = list(csv_reader1)

    N = csvData[0][0]
    Pop = csvData[0][1]
    MUTRATE = csvData[0][2]
    MUTSTEP = csvData[0][3]
    Gen = csvData[0][4]

    csvData[0].pop(0)
    csvData[0].pop(0)
    csvData[0].pop(0)
    csvData[0].pop(0) 
    csvData[0].pop(0)
    csvData[0].pop()
    
with open("DataMinMean.csv", "r") as csv_file1:
    csvDataMean = []
    csv_reader1 = csv.reader(csv_file1)
    csvDataMean = list(csv_reader1)

    csvDataMean[0].pop()

def popGen():
    data = []
    for i in range(0, int(Gen)):
        data.append(i)
    return data

print(csvData[0])
print("N: " + N)
print("POP: " + Pop)
print("MUTRATE: " + MUTRATE)
print("MUTSTEP: " + MUTSTEP)
print("GEN: " + Gen)

plt.figure(figsize=(20,10))
plt.figtext(0.5, 0.01, "N: " + N + " / " + "POP: " + Pop + " / " + "MUTRATE: " + MUTRATE + " / " + "MUTSTEP: " + MUTSTEP + " / " + "GEN: " + Gen + " ",horizontalalignment = "center",  fontsize=20, bbox={"facecolor":"white", "alpha":0.5, "pad":10, })

plt.xlabel("Generation", fontsize=15)
plt.ylabel("Min fitness",  fontsize=15)



ypoints = np.array(csvData[0][::-1])
zpoints = np.array(csvDataMean[0][::-1])


plt.plot(ypoints)
plt.plot(zpoints,color="red")
#plt.plot(zpoints ,color="red")
plt.show()