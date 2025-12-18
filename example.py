import sys

pathParser = "" # Here assign the complete path of the parser.py file

sys.path.append(pathParser)

import modelica2pyomo as ps

# PATHS
modelicaModelPath = "" # String containing the path of the BaseModelica file obtained instantiating the Modelica file with exampleInstantiation.mos

modelicaResultsPath = "" # String containing the path of the results file from a simulation of the Modelica model to initialize the optimization problem

pyomoModelPath = "" # String containing the path to the newly created Pyomo file

# MODEL AND SOLVER
modelName = "m"
solverName = "ipopt"

# Static or Dynamic problem
staticOrDynamic = "Dynamic"  # use either "Static" or "Dynamic"
initConditionsOption = "FIX-STATES" # use either "FIX-STATES" or "KEEP-MODELICA"
initialGuessTrajectoryOption = "Dynamic"  # use either "Constant" or "Dynamic"

# TIME DISCRETIZATION FOR DYNAMIC PROBLEM
tStart = 0
tEnd = 60

# Collocation
collocationOptions = dict()
collocationOptions["methodeName"] = "dae.collocation"
collocationOptions["nfe"] = "10" # Number of finite elements for collocation as string
collocationOptions["ncp"] = "3" # Number of collocation points in finite element as string
collocationOptions["scheme"] = "LAGRANGE-RADAU"

# Finite differences
# finiteDiffOptions = dict()
# finiteDiffOptions["methodeName"] = "dae.finite_difference"
# finiteDiffOptions["nfe"] = "10" # Number of finite elements for finte differences as string
# finiteDiffOptions["scheme"] = "BACKWARD"

customLinesBeforeSettings = """
# Objective function of the optimization problem
m.obj = Objective(expr = 1, sense = minimize)
"""

customLinesAfterSettings = """
"""



ps.m2p(modelicaModelPath, pyomoModelPath, modelicaResultsPath, modelName, solverName, staticOrDynamic = staticOrDynamic, 
        initConditionsOption = initConditionsOption, initialGuessTrajectoryOption = initialGuessTrajectoryOption, customLinesBeforeSettings = customLinesBeforeSettings, 
        customLinesAfterSettings=customLinesAfterSettings, tStart = tStart, tEnd = tEnd,
        bounds = True, subLog = True, useResultsForTables = False, dynTransfOpt=collocationOptions)

# Input description:
    # - modelicaModelPath: string containing the path of the modelica model to translate into a Pyomo model
    # - pyomoModelPath: string containing path of the Pyomo model to be generated
    # - modelicaResultsPath: string containing path of the optional modelica results file
    # - modelName = string containing the name of the Pyomo model instance (for example m.)
    # - solverName = string containing the name of the optimization solver to be called with Pyomo with the SolverFactory object
    # - staticOrDynamic = string that is either "Static" or "Dynamic" to tell the compiler if the optimization problem is either static or dynamic
    # - initConditionsOption = string that is either "KEEP-MODELICA" or "FIX-STATES" to tell the compiler if it should keep the initial equations of the 
    #                       Modelica model or use the results file to fix the values of the variables appearing in the der() operator
    #                       at time instant zero
    # - customLinesBeforeSettings: string containing the 
    # - customLinesAfterSettings: string containing the 
    # - tStart: float containing the start time of the dynamic simulation
    # - tEnd: float containing the end time of the dynamic simulation
    # - initialGuessTrajectoryOption: string specifying either the initialization follows a "Constant" or "Dynamic" trajectory (options="Constant" or "Dynamic").
    # - bounds: boolean (True or False). If True enforce bounds through the "bounds" keyword in the Var declaration *based on min and max attributes of 
    #               Base Modelica model. If False, do not use "bounds" keyword
    # - subLog: boolean (True or False). If true perform log substitution with equivalent exponential expression
    # - useResultsForTables: boolean (True or False). If True, table entries are retrieved from the Modelica result file; if False, the BaseModelica code is translated
    # - dynTransfOpt: dictionary with options for the collocation or finite difference discretization.
    #                       Example for collocation:
    #                           dynTransfOpt = dict()
    #                           dynTransfOpt["methodeName"] = "dae.collocation"
    #                           dynTransfOpt["nfe"] = "10" # Number of finite elements for collocation as string
    #                           dynTransfOpt["ncp"] = "3" # Number of collocation points in finite element as string
    #                           dynTransfOpt["scheme"] = "LAGRANGE-RADAU"
    #
    #                       Example for finite difference (no "ncp" for finite difference):
    #                           dynTransfOpt = dict()
    #                           dynTransfOpt["methodeName"] = "dae.finite_difference"
    #                           dynTransfOpt["nfe"] = "10" # Number of finite elements for finte differences as string
    #                           dynTransfOpt["scheme"] = "BACKWARD"