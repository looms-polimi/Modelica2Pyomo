import idaes
from idaes.core.solvers.config import use_idaes_solver_configuration_defaults
from idaes.core.util import DiagnosticsToolbox
from pyomo.environ import (
    ConcreteModel,
    Var,
    PositiveReals,
    Objective,
    Constraint,
    ConstraintList,
    Suffix,
    Reals,
    log,
    exp,
    sqrt,
    sin,
    minimize,
    maximize,
    SolverFactory,
    TransformationFactory,
    value,
    summation)
from pyomo.core.expr import identify_variables
from pyomo.core.expr import differentiate
from pyomo.dae import (
    ContinuousSet,
    DerivativeVar)
import numpy as np
import re


m = ConcreteModel()

m.scaling_factor = Suffix(direction=Suffix.EXPORT)


numOfIntervals = 100
ncp = 3
tStart = 0
tEnd = 500
m.time = ContinuousSet(initialize = np.linspace(tStart,tEnd,numOfIntervals+1))
dt = tEnd/(numOfIntervals+1)/ncp

#m.time = ContinuousSet(bounds = (tStart,tEnd))
m.wCold_y = Var(m.time, initialize = 270.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.wCold_y] = 1/max(1.0,270.0)
m.wHot_y = Var(m.time, initialize = 62.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.wHot_y] = 1/max(1.0,62.0)
m.Pel_y = Var(m.time, initialize = 39798754.20477611, bounds = (None,None), within = Reals)
m.scaling_factor[m.Pel_y] = 1/max(1.0,39798754.20477611)
m.TIT_y = Var(m.time, initialize = 887.6766279651436, bounds = (None,None), within = Reals)
m.scaling_factor[m.TIT_y] = 1/max(1.0,887.6766279651436)
m.completeModel_pCold = Var(m.time, initialize = 25962033.45200394, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pCold] = 1/max(10000000.0,25962033.45200394)
m.completeModel_pHot = Var(m.time, initialize = 121550.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pHot] = 1/max(10000000.0,121550.0)
m.completeModel_pInCold = Var(m.time, initialize = 26083533.45200394, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pInCold] = 1/max(10000000.0,26083533.45200394)
m.completeModel_pInHot = Var(m.time, initialize = 123100.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pInHot] = 1/max(10000000.0,123100.0)
m.completeModel_pOutCold = Var(m.time, initialize = 25840533.45200394, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pOutCold] = 1/max(10000000.0,25840533.45200394)
m.completeModel_pOutHot = Var(m.time, initialize = 120000.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_pOutHot] = 1/max(10000000.0,120000.0)
m.completeModel_wCold_1 = Var(m.time, initialize = 270.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wCold_1] = 1/max(100.0,270.0)
m.completeModel_wCold_2 = Var(m.time, initialize = 270.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wCold_2] = 1/max(100.0,270.0)
m.completeModel_wCold_3 = Var(m.time, initialize = 270.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wCold_3] = 1/max(100.0,270.0)
m.completeModel_wHot_1 = Var(m.time, initialize = 62.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wHot_1] = 1/max(100.0,62.0)
m.completeModel_wHot_2 = Var(m.time, initialize = 62.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wHot_2] = 1/max(100.0,62.0)
m.completeModel_wHot_3 = Var(m.time, initialize = 62.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wHot_3] = 1/max(100.0,62.0)
m.completeModel_Tcold_1 = Var(m.time, initialize = 723.15, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Tcold_1] = 1/max(500.0,723.15)
m.completeModel_Tcold_2 = Var(m.time, initialize = 752.4603167676081, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Tcold_2] = 1/max(500.0,752.4603167676081)
m.completeModel_Tcold_3 = Var(m.time, initialize = 887.6766279651436, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Tcold_3] = 1/max(500.0,887.6766279651436)
m.completeModel_Thot_1 = Var(m.time, initialize = 1413.15, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Thot_1] = 1/max(500.0,1413.15)
m.completeModel_Thot_2 = Var(m.time, initialize = 866.365147115957, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Thot_2] = 1/max(500.0,866.365147115957)
m.completeModel_Thot_3 = Var(m.time, initialize = 747.8407094957905, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Thot_3] = 1/max(500.0,747.8407094957905)
m.completeModel_Twall_1 = Var(m.time, initialize = 739.5636459462451, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Twall_1] = 1/max(500.0,739.5636459462451)
m.completeModel_Twall_2 = Var(m.time, initialize = 828.180844653761, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_Twall_2] = 1/max(500.0,828.180844653761)
m.completeModel_wInCold = Var(m.time, initialize = 270.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wInCold] = 1/max(1.0,270.0)
m.completeModel_wInHot = Var(m.time, initialize = 62.0, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_wInHot] = 1/max(1.0,62.0)
m.completeModel_Pel = Var(m.time, initialize = 39798754.20477611, bounds = (None,None), within = Reals)
m.scaling_factor[m.completeModel_Pel] = 1/max(10000000.0,39798754.20477611)
m.completeModel_TIT = Var(m.time, initialize = 887.6766279651436, bounds = (0.0,None), within = Reals)
m.scaling_factor[m.completeModel_TIT] = 1/max(500.0,887.6766279651436)




m.DERcompleteModel_pCold = DerivativeVar(m.completeModel_pCold, initialize = 0)
m.scaling_factor[m.DERcompleteModel_pCold] = m.scaling_factor[m.completeModel_pCold]*dt
m.DERcompleteModel_pHot = DerivativeVar(m.completeModel_pHot, initialize = 0)
m.scaling_factor[m.DERcompleteModel_pHot] = m.scaling_factor[m.completeModel_pHot]*dt
m.DERcompleteModel_Tcold_2 = DerivativeVar(m.completeModel_Tcold_2, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Tcold_2] = m.scaling_factor[m.completeModel_Tcold_2]*dt
m.DERcompleteModel_Thot_2 = DerivativeVar(m.completeModel_Thot_2, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Thot_2] = m.scaling_factor[m.completeModel_Thot_2]*dt
m.DERcompleteModel_Twall_1 = DerivativeVar(m.completeModel_Twall_1, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Twall_1] = m.scaling_factor[m.completeModel_Twall_1]*dt
m.DERcompleteModel_Tcold_3 = DerivativeVar(m.completeModel_Tcold_3, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Tcold_3] = m.scaling_factor[m.completeModel_Tcold_3]*dt
m.DERcompleteModel_Thot_3 = DerivativeVar(m.completeModel_Thot_3, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Thot_3] = m.scaling_factor[m.completeModel_Thot_3]*dt
m.DERcompleteModel_Twall_2 = DerivativeVar(m.completeModel_Twall_2, initialize = 0)
m.scaling_factor[m.DERcompleteModel_Twall_2] = m.scaling_factor[m.completeModel_Twall_2]*dt



discretizer = TransformationFactory('dae.collocation')
discretizer.apply_to(m, nfe=numOfIntervals, ncp=ncp, scheme='LAGRANGE-RADAU')

timeSteps = [h for h in m.time]

m.wCold_y.fix(270.0)

m.wHot_y.fix(62.0)

def _constr1(m,t):
    return m.Pel_y[t] == m.completeModel_Pel[t]

m.constr1 = Constraint(m.time, rule = _constr1)

def _constr2(m,t):
    return m.TIT_y[t] == m.completeModel_TIT[t]

m.constr2 = Constraint(m.time, rule = _constr2)

def _constr3(m,t):
    return m.wCold_y[t] == m.completeModel_wInCold[t]

m.constr3 = Constraint(m.time, rule = _constr3)

def _constr4(m,t):
    return m.wHot_y[t] == m.completeModel_wInHot[t]

m.constr4 = Constraint(m.time, rule = _constr4)

def _constr5(m,t):
    return m.completeModel_wInCold[t] == m.completeModel_wCold_1[t]

m.constr5 = Constraint(m.time, rule = _constr5)

def _constr6(m,t):
    return m.completeModel_wInHot[t] == m.completeModel_wHot_1[t]

m.constr6 = Constraint(m.time, rule = _constr6)

m.completeModel_Tcold_1.fix(723.15)

m.completeModel_Thot_1.fix(1413.15)

m.completeModel_pOutHot.fix(1.2e5)

def _constr7(m,t):
    return m.completeModel_pInCold[t] - m.completeModel_pCold[t] == 450.0 * m.completeModel_wCold_1[t]

m.constr7 = Constraint(m.time, rule = _constr7)

def _constr8(m,t):
    return m.completeModel_pCold[t] - m.completeModel_pOutCold[t] == 450.0 * m.completeModel_wCold_3[t]

m.constr8 = Constraint(m.time, rule = _constr8)

def _constr9(m,t):
    return m.completeModel_pInHot[t] - m.completeModel_pHot[t] == 25.0 * m.completeModel_wHot_1[t]

m.constr9 = Constraint(m.time, rule = _constr9)

def _constr10(m,t):
    return m.completeModel_pHot[t] - m.completeModel_pOutHot[t] == 25.0 * m.completeModel_wHot_3[t]

m.constr10 = Constraint(m.time, rule = _constr10)

def _constr11(m,t):
    if t == 0:
        return Constraint.Skip
    return 26.0 / (188.92426903630442 * m.completeModel_Tcold_2[t]) * m.DERcompleteModel_pCold[t] == m.completeModel_wCold_1[t] - m.completeModel_wCold_2[t]

m.constr11 = Constraint(m.time, rule = _constr11)

def _constr12(m,t):
    if t == 0:
        return Constraint.Skip
    return 6646.0 / (285.9466663248131 * m.completeModel_Thot_2[t]) * m.DERcompleteModel_pHot[t] == m.completeModel_wHot_1[t] - m.completeModel_wHot_2[t]

m.constr12 = Constraint(m.time, rule = _constr12)

def _constr13(m,t):
    if t == 0:
        return Constraint.Skip
    return m.completeModel_pCold[t] / 188.92426903630442 / m.completeModel_Tcold_2[t] * 52.0 / 2.0 * 981.0757309636956 * m.DERcompleteModel_Tcold_2[t] == m.completeModel_wCold_2[t] * 1170.0 * (m.completeModel_Tcold_1[t] - m.completeModel_Tcold_2[t]) + 3400.0 * (m.completeModel_pOutCold[t] / 2.5e7) ** 0.5 * (m.completeModel_wCold_2[t] / 270.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_1[t] - (m.completeModel_Tcold_1[t] + m.completeModel_Tcold_2[t]) / 2.0)

m.constr13 = Constraint(m.time, rule = _constr13)

def _constr14(m,t):
    if t == 0:
        return Constraint.Skip
    return m.completeModel_pHot[t] / 285.9466663248131 / m.completeModel_Thot_2[t] * 13292.0 / 2.0 * 974.0533336751869 * m.DERcompleteModel_Thot_2[t] == m.completeModel_wHot_2[t] * 1260.0 * (m.completeModel_Thot_1[t] - m.completeModel_Thot_2[t]) + 90.0 * (m.completeModel_pOutHot[t] / 1.2e5) ** 0.5 * (m.completeModel_wHot_2[t] / 62.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_2[t] - (m.completeModel_Thot_1[t] + m.completeModel_Thot_2[t]) / 2.0)

m.constr14 = Constraint(m.time, rule = _constr14)

def _constr15(m,t):
    if t == 0:
        return Constraint.Skip
    return 6.8145e7 * m.DERcompleteModel_Twall_1[t] == -(3400.0 * (m.completeModel_pOutCold[t] / 2.5e7) ** 0.5 * (m.completeModel_wCold_2[t] / 270.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_1[t] - (m.completeModel_Tcold_1[t] + m.completeModel_Tcold_2[t]) / 2.0) + 90.0 * (m.completeModel_pOutHot[t] / 1.2e5) ** 0.5 * (m.completeModel_wHot_2[t] / 62.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_1[t] - (m.completeModel_Thot_3[t] + m.completeModel_Thot_2[t]) / 2.0))

m.constr15 = Constraint(m.time, rule = _constr15)

def _constr16(m,t):
    if t == 0:
        return Constraint.Skip
    return 26.0 / (188.92426903630442 * m.completeModel_Tcold_3[t]) * m.DERcompleteModel_pCold[t] == m.completeModel_wCold_2[t] - m.completeModel_wCold_3[t]

m.constr16 = Constraint(m.time, rule = _constr16)

def _constr17(m,t):
    if t == 0:
        return Constraint.Skip
    return 6646.0 / (285.9466663248131 * m.completeModel_Thot_3[t]) * m.DERcompleteModel_pHot[t] == m.completeModel_wHot_2[t] - m.completeModel_wHot_3[t]

m.constr17 = Constraint(m.time, rule = _constr17)

def _constr18(m,t):
    if t == 0:
        return Constraint.Skip
    return m.completeModel_pCold[t] / 188.92426903630442 / m.completeModel_Tcold_3[t] * 52.0 / 2.0 * 981.0757309636956 * m.DERcompleteModel_Tcold_3[t] == m.completeModel_wCold_3[t] * 1170.0 * (m.completeModel_Tcold_2[t] - m.completeModel_Tcold_3[t]) + 3400.0 * (m.completeModel_pOutCold[t] / 2.5e7) ** 0.5 * (m.completeModel_wCold_3[t] / 270.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_2[t] - (m.completeModel_Tcold_2[t] + m.completeModel_Tcold_3[t]) / 2.0)

m.constr18 = Constraint(m.time, rule = _constr18)

def _constr19(m,t):
    if t == 0:
        return Constraint.Skip
    return m.completeModel_pHot[t] / 285.9466663248131 / m.completeModel_Thot_3[t] * 13292.0 / 2.0 * 974.0533336751869 * m.DERcompleteModel_Thot_3[t] == m.completeModel_wHot_3[t] * 1260.0 * (m.completeModel_Thot_2[t] - m.completeModel_Thot_3[t]) + 90.0 * (m.completeModel_pOutHot[t] / 1.2e5) ** 0.5 * (m.completeModel_wHot_3[t] / 62.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_1[t] - (m.completeModel_Thot_2[t] + m.completeModel_Thot_3[t]) / 2.0)

m.constr19 = Constraint(m.time, rule = _constr19)

def _constr20(m,t):
    if t == 0:
        return Constraint.Skip
    return 6.8145e7 * m.DERcompleteModel_Twall_2[t] == -(3400.0 * (m.completeModel_pOutCold[t] / 2.5e7) ** 0.5 * (m.completeModel_wCold_3[t] / 270.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_2[t] - (m.completeModel_Tcold_2[t] + m.completeModel_Tcold_3[t]) / 2.0) + 90.0 * (m.completeModel_pOutHot[t] / 1.2e5) ** 0.5 * (m.completeModel_wHot_1[t] / 62.0) ** 0.8 * 3046.5 / 2.0 * (m.completeModel_Twall_2[t] - (m.completeModel_Thot_2[t] + m.completeModel_Thot_1[t]) / 2.0))

m.constr20 = Constraint(m.time, rule = _constr20)

def _constr21(m,t):
    return m.completeModel_wCold_3[t] == 0.0045 * m.completeModel_pOutCold[t] * sqrt( 0.0052931262092528525 / m.completeModel_Tcold_3[t]) * sqrt( 1.0 - (1.0 / (m.completeModel_pOutCold[t] / 8e6)) ** 2.0)

m.constr21 = Constraint(m.time, rule = _constr21)

def _constr22(m,t):
    return m.completeModel_Pel[t] == m.completeModel_wCold_3[t] * 0.843 * 1170.0 * m.completeModel_Tcold_3[t] * (1.0 - (8e6 / m.completeModel_pOutCold[t]) ** 0.1614737342190636) * 0.98 * 0.996

m.constr22 = Constraint(m.time, rule = _constr22)

def _constr23(m,t):
    return m.completeModel_TIT[t] == m.completeModel_Tcold_3[t]

m.constr23 = Constraint(m.time, rule = _constr23)



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

# Added after best
powerTable = [(0,39798754.20477611), (10, 39798754.20477611), (70,39798754.20477611*1.02), (200,39798754.20477611*1.02), (450, 39798754.20477611), (500, 39798754.20477611)]
powerProfile = trap(powerTable, timeSteps)


m.obj = Objective(expr = 100000000*sum([(m.TIT_y[i]-titProfile[j])**2 for i,j in zip(timeSteps, range(len(timeSteps)))])
                  + 1*sum([(m.Pel_y[i]-powerProfile[j])**2 for i,j in zip(timeSteps, range(len(timeSteps)))])
                  + 100000000*sum([(m.wHot_y[m.time.at(i+2)]-m.wHot_y[m.time.at(i+1)])**2 for i in range(len(m.time)-1)])
                  + 1*sum([(m.wCold_y[m.time.at(i+2)]-m.wCold_y[m.time.at(i+1)])**2 for i in range(len(m.time)-1)]), sense = minimize)

def _init(m):
    yield m.completeModel_pCold[0] == 25962033.45200394
    yield m.completeModel_pHot[0] == 121550.0
    yield m.completeModel_Tcold_2[0] == 752.4603167676081
    yield m.completeModel_Thot_2[0] == 866.365147115957
    yield m.completeModel_Twall_1[0] == 739.5636459462451
    yield m.completeModel_Tcold_3[0] == 887.6766279651436
    yield m.completeModel_Thot_3[0] == 747.8407094957905
    yield m.completeModel_Twall_2[0] == 828.180844653761
    yield ConstraintList.End

m.init_conditions = ConstraintList(rule=_init)




for constr in m.component_objects(Constraint, active=True):
    varList = list(identify_variables(constr[list(constr.keys())[0]].body))
    listF = []
    for var in varList:
        varName = re.sub(r'\[.*\]', '', str(var))
        varName = "m." + varName
        listF.append(abs(differentiate(constr[list(constr.keys())[0]].body, wrt=var)/m.scaling_factor[eval(varName)]))
    m.scaling_factor[constr] = 1/max(listF)
    
varList = list(identify_variables(m.obj))
listF = []
for var in varList:
    varName = re.sub(r'\[.*\]', '', str(var))
    varName = "m." + varName
    listF.append(abs(differentiate(m.obj, wrt=var)/m.scaling_factor[eval(varName)]))
    
if listF != []:    
    m.scaling_factor[m.obj] = 1/max(listF)




scaled_model = TransformationFactory('core.scale_model').create_using(m)
use_idaes_solver_configuration_defaults()
solver = SolverFactory("ipopt")
#solver = SolverFactory("gams:conopt")
results = solver.solve(scaled_model, tee=True, logfile="log.txt")
TransformationFactory('core.scale_model').propagate_solution(scaled_model, m)
  
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


#from  scipy.io import savemat

#results = {"HXtimeSteps":timeSteps, "HXactualTimeSteps":actualTimeSteps, "HXwCold":wCold, "HXwHot":wHot, "HXTIT":TIT, "HXPel":Pel, "HXpowerProfile":powerProfile}

#savemat("hxRes.mat", results)
