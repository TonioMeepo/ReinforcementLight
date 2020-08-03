from matplotlib import pyplot as plt

f = open("log.txt", "r")
ours = []
for line in f.readlines():
    ours.append(-int(line))


f = open("baseline.txt", "r")
theirs = []
for line in f.readlines():
    theirs.append(int(line))

plt.figure()
plt.title("Traffic Light Performance \n(lower is better)")
plt.plot(ours,label = "RL Agent")
plt.plot(theirs, label = "Default semaphore")
plt.grid()
plt.legend()
plt.xlabel("steps")
plt.ylabel("number of veichles")
plt.savefig("firstPlot.jpg")
plt.show()