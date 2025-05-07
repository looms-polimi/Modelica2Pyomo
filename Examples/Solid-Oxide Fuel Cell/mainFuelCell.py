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

modelica_model = r"./baseModelicaFuelCell.mo"
modelicaResults = r"./fuelCellRes.mat"
# pyomoModel = "SOFC02K_s.py"
pyomoModel = "SOFC06K_s.py"

modelName = "m"
solverName = "gams:conopt"


staticOrDynamic = "Dynamic"  # use either "Static" or "Dynamic"
initConditions = "FIX-STATES" # use either "FIX-STATES" or "KEEP-MODELICA"
initTrajectory = "Constant"  # use either "Constant" or "Dynamic"


tStart = 0
tEnd = 100


# Collocation
collocationOptions = dict()
collocationOptions["methodeName"] = "dae.collocation"
collocationOptions["nfe"] = "35"
collocationOptions["ncp"] = "3"
collocationOptions["scheme"] = "LAGRANGE-RADAU"


customLinesBeforeSettings = """
m.elCurrent2_y.unfix()

# maxLim = 0.2 * dt # This limit is active now, not like the 0.6*dt
maxLim = 0.6 * dt 

def _maxTpenVarU1(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_1_pen_T[t] - m.stack_module_1_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU1 = Constraint(m.time, rule = _maxTpenVarU1)

def _maxTpenVarL1(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_1_pen_T[t] - m.stack_module_1_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL1 = Constraint(m.time, rule = _maxTpenVarL1)

def _maxTpenVarU2(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_2_pen_T[t] - m.stack_module_2_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU2 = Constraint(m.time, rule = _maxTpenVarU2)

def _maxTpenVarL2(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_2_pen_T[t] - m.stack_module_2_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL2 = Constraint(m.time, rule = _maxTpenVarL2)

def _maxTpenVarU3(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_3_pen_T[t] - m.stack_module_3_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU3 = Constraint(m.time, rule = _maxTpenVarU3)

def _maxTpenVarL3(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_3_pen_T[t] - m.stack_module_3_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL3 = Constraint(m.time, rule = _maxTpenVarL3)

def _maxTpenVarU4(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_4_pen_T[t] - m.stack_module_4_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU4 = Constraint(m.time, rule = _maxTpenVarU4)

def _maxTpenVarL4(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_4_pen_T[t] - m.stack_module_4_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL4 = Constraint(m.time, rule = _maxTpenVarL4)

def _maxTpenVarU5(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_5_pen_T[t] - m.stack_module_5_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU5 = Constraint(m.time, rule = _maxTpenVarU5)

def _maxTpenVarL5(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_5_pen_T[t] - m.stack_module_5_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL5 = Constraint(m.time, rule = _maxTpenVarL5)

def _maxTpenVarU6(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_6_pen_T[t] - m.stack_module_6_pen_T[m.time.prev(t)] <= maxLim

m.maxTpenVarU6 = Constraint(m.time, rule = _maxTpenVarU6)

def _maxTpenVarL6(m,t):
    if t == m.time.first():
        return Constraint.Skip
    return m.stack_module_6_pen_T[t] - m.stack_module_6_pen_T[m.time.prev(t)] >= -maxLim

m.maxTpenVarL6 = Constraint(m.time, rule = _maxTpenVarL6)

def trap(points,timeSteps):
    # points: list of tuples (time, value)
    # timeSteps: list of time steps
    seq = []
    newPoints = []
    verts = []
    for point in points:
        listClosest = [abs(point[0]-ts) for ts in timeSteps]
        newPoint = timeSteps[listClosest.index(min(listClosest))]
        newPoints.append((newPoint, point[1]))
        verts.append(newPoint)
    for ts in timeSteps:
        if ts in verts:
            seq.append(newPoints[verts.index(ts)][1])
            continue
        tsPosInTimeList = [ts<point[0] for point in newPoints]
        t2index = tsPosInTimeList.index(1)
        t1index = t2index - 1
        t2 = verts[t2index]
        t1 = verts[t1index]
        y2 = newPoints[t2index][1]
        y1 = newPoints[t1index][1]
        if y1 == y2:
            seq.append(y1)
        else:
            val = (ts-t1)/(t2-t1)*(y2-y1)+y1
            seq.append(val)

    return seq


points = [(0,13.431508), (10,13.431508), (15,10), (50,10), (80, 15.5), (100,15.5)] # WORKING

powerProfile = trap(points,timeSteps)

m.obj = Objective(expr = 100*sum([(m.stack_pElStack[t]-ref)**2 for t,ref in zip(m.time,powerProfile)]) + 
                            185*sum([(m.elCurrent2_y[i]-m.elCurrent2_y[j])**2 for i, j in zip(timeSteps[1:len(timeSteps)],timeSteps[0:len(timeSteps)-1])]) +
                            10*sum([(m.stack_module_1_pen_T[i]-m.stack_module_1_pen_T[j])**2 for i, j in zip(timeSteps[1:len(timeSteps)],timeSteps[0:len(timeSteps)-1])]), 
                            sense=minimize)
"""


customLinesAfterSettings = """
m.obj.display()

import matplotlib.pyplot as plt

actualTimeSteps = []
noInd = 0
nfe = 3
for elem in timeSteps:
    if timeSteps.index(elem) == noInd:
        noInd+=nfe
    else:
        actualTimeSteps.append(elem)

power = [value(m.stack_pElStack[i]) for i in actualTimeSteps]
current = [value(m.elCurrent2_y[i]) for i in actualTimeSteps]
ToutAnode = [value(m.stack_module_6_anodeChannel_Tout[i]-273.15) for i in actualTimeSteps]
ToutCathode = [value(m.stack_module_6_cathodeChannel_Tout[i]-273.15) for i in actualTimeSteps]
currDens6 = [value(m.stack_module_2_pen_j[i]/10) for i in actualTimeSteps]

fig1 = plt.figure()
plt.plot(actualTimeSteps, power)
plt.plot(timeSteps, powerProfile)
plt.title("Power Step")
plt.xlabel("Time [s]")
plt.ylabel("Power [W]")

fig2 = plt.figure()
plt.plot(actualTimeSteps, current)
plt.title("Current variable")
plt.xlabel("Time [s]")
plt.ylabel("Current [A]")

fig3 = plt.figure()
plt.plot(actualTimeSteps, ToutAnode)
plt.title("T anode Out")
plt.xlabel("Time [s]")
plt.ylabel("Temp [C]")

fig4 = plt.figure()
plt.plot(actualTimeSteps, ToutCathode)
plt.title("T cathode Out")
plt.xlabel("Time [s]")
plt.ylabel("Temp [C]")

fig5 = plt.figure()
plt.plot(actualTimeSteps, currDens6)
plt.title("j vol 6")
plt.xlabel("Time [s]")
plt.ylabel("curr dens [mA/cm2]")

plt.show()


# from  scipy.io import savemat

# results06 = {"SOFCtimeSteps06":timeSteps, "SOFCactualTimeSteps06":actualTimeSteps, "SOFCToutCathode06":ToutCathode, "SOFCToutAnode06":ToutAnode, "SOFCcurrent06":current, "SOFCpower06":power, "SOFCpowerProfile06":powerProfile}
# savemat("sofcRes06.mat", results06)

# #results02 = {"SOFCtimeSteps02":timeSteps, "SOFCactualTimeSteps02":actualTimeSteps, "SOFCToutCathode02":ToutCathode, "SOFCToutAnode02":ToutAnode, "SOFCcurrent02":current, "SOFCpower02":power, "SOFCpowerProfile02":powerProfile}
# #savemat("sofcRes02.mat", results02)
"""


ps.m2p(modelica_model, pyomoModel, modelicaResults, modelName, solverName, staticOrDynamic = staticOrDynamic,
        initConditions = initConditions, initTrajectory=initTrajectory, customLinesBeforeSettings=customLinesBeforeSettings,
        customLinesAfterSettings=customLinesAfterSettings, tStart = tStart, tEnd = tEnd,
        bounds = True, subLog = True, dynTransfOpt=collocationOptions)
        
print("Compilation time:")
toc()