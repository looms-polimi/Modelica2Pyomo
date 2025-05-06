import time

def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)

tic()

import sys
sys.path.append(r"../..")
import modelica2pyomo as ps

modelica_model = r"./baseModelicaHXturb.mo"
modelicaResults = r"./hxTurbRes.mat"
pyomoModel = r"hxTurbpyomo.py"

modelName = "m"
solverName = "ipopt"

staticOrDynamic = "Dynamic"  # use either "Static" or "Dynamic"
initConditions = "FIX-STATES" # use either "FIX-STATES" or "KEEP-MODELICA"
initTrajectory = "Constant"  # use either "Constant" or "Dynamic"

tStart = 0
tEnd = 500

# Collocation
collocationOptions = dict()
collocationOptions["methodeName"] = "dae.collocation"
collocationOptions["nfe"] = "100"
collocationOptions["ncp"] = "3"
collocationOptions["scheme"] = "LAGRANGE-RADAU"


customLinesBeforeSettings = """

m.ssConstr = Constraint(expr = m.TIT_y[m.time.at(-1)] == m.TIT_y[m.time.at(-2)])

m.wCold_y.unfix()

m.wHot_y.unfix()

timeSteps = [h for h in m.time]

def trap(points,timeSteps):
    inputSeq = []
    newPoints = []
    verts = []
    for point in points:
        listClosest = [abs(point[0]-ts) for ts in timeSteps]
        newPoint = timeSteps[listClosest.index(min(listClosest))]
        newPoints.append((newPoint, point[1]))
        verts.append(newPoint)
    for ts in timeSteps:
        if ts in verts:
            inputSeq.append(newPoints[verts.index(ts)][1])
            continue
        tsPosInTimeList = [ts<point[0] for point in newPoints]
        t2index = tsPosInTimeList.index(1)
        t1index = t2index - 1
        t2 = verts[t2index]
        t1 = verts[t1index]
        y2 = newPoints[t2index][1]
        y1 = newPoints[t1index][1]
        if y1 == y2:
            inputSeq.append(y1)
        else:
            val = (ts-t1)/(t2-t1)*(y2-y1)+y1
            inputSeq.append(val)

    return inputSeq

titTable = [(0,887.6766279651436), (10, 887.6766279651436), (300,887.6766279651436), (500,887.6766279651436)]
titProfile = trap(titTable, timeSteps)

powerTable = [(0,39798754.20477611), (10, 39798754.20477611), (70,39798754.20477611*1.02), (200,39798754.20477611*1.02), (450, 39798754.20477611), (500, 39798754.20477611)]
powerProfile = trap(powerTable, timeSteps)


m.obj = Objective(expr = 100000000*sum([(m.TIT_y[i]-titProfile[j])**2 for i,j in zip(timeSteps, range(len(timeSteps)))])
                  + 1*sum([(m.Pel_y[i]-powerProfile[j])**2 for i,j in zip(timeSteps, range(len(timeSteps)))])
                  + 100000000*sum([(m.wHot_y[m.time.at(i+2)]-m.wHot_y[m.time.at(i+1)])**2 for i in range(len(m.time)-1)])
                  + 1*sum([(m.wCold_y[m.time.at(i+2)]-m.wCold_y[m.time.at(i+1)])**2 for i in range(len(m.time)-1)]), sense = minimize)

"""


customLinesAfterSettings = """  
import matplotlib.pyplot as plt

actualTimeSteps = []
noInd = 0
nfe = 3
for elem in timeSteps:
    if timeSteps.index(elem) == noInd:
        noInd+=nfe
    else:
        actualTimeSteps.append(elem)

wCold = [value(m.wCold_y[i]) for i in actualTimeSteps]
wHot = [value(m.wHot_y[i]) for i in actualTimeSteps]
TIT = [value(m.completeModel_TIT[i]) for i in actualTimeSteps]
Pel = [value(m.Pel_y[i]) for i in actualTimeSteps]

fig1 = plt.figure()
plt.plot(actualTimeSteps, wCold)
plt.title("wCold")
plt.xlabel("Time [s]")
plt.ylabel("Mass flow rate [kg/s]")


fig2 = plt.figure()
plt.plot(actualTimeSteps, wHot)
plt.title("wHot")
plt.xlabel("Time [s]")
plt.ylabel("Mass flow rate [kg/s]")

fig3 = plt.figure()
plt.plot(actualTimeSteps, Pel)
plt.plot(timeSteps, powerProfile)
plt.title("Power")
plt.xlabel("Time [s]")
plt.ylabel("Power [W]")

plt.show()


# from  scipy.io import savemat

# results = {"HXtimeSteps":timeSteps, "HXactualTimeSteps":actualTimeSteps, "HXwCold":wCold, "HXwHot":wHot, "HXTIT":TIT, "HXPel":Pel, "HXpowerProfile":powerProfile}

# savemat("hxRes.mat", results)
"""

ps.m2p(modelica_model, pyomoModel, modelicaResults, modelName, solverName, staticOrDynamic = staticOrDynamic,
        initConditions = initConditions, initTrajectory=initTrajectory, customLinesBeforeSettings=customLinesBeforeSettings,
        customLinesAfterSettings=customLinesAfterSettings, tStart = tStart, tEnd = tEnd,
        bounds = True, subLog = True, dynTransfOpt=collocationOptions)
        
print("Compilation time:")
toc()