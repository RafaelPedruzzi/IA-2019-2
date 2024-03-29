## -------------------------------------------------------- ##
#   Trab 1 IA 2019-2
#
#   Rafael Belmock Pedruzzi
#
#   simulatedAnnealing.py: implements the simulated annealing metaheuristic for the bag problem
#
#   Python version: 3.7.4
## -------------------------------------------------------- ##

import bagProblem as bp
import hillClimbing as hc
import priorityQ as pq
import random
import math
from time import time

# Remove and return a random item from the given list:
def take_Random(si):
    if si == []:
        return []
    return si.pop(random.randint(0,len(si)-1))

# Return a neightborhood of the given state
def neightborhood(s, T, OBJs):
    neig = []
    for i in bp.state_Expansion(s): # add all valid states from the expansion of the given state
        if bp.state_Verify(i, T, OBJs):
            neig.append(i)
    # for i in neig:                    # adding all valid retractions of each state currently in the neightborhood
    #     for j in bp.state_Retract(i):
    #         if bp.state_Verify(j, T, OBJs):
    #             neig.append(j)
    for i in bp.state_Retract(s): # add all valid states from the retraction of the given state
        if bp.state_Verify(i, T, OBJs):
            neig.append(i)
    return neig

# Simulated Anneling:
def sim_Annealing(T, OBJs, execTime, *args):
    temp = args[0]
    alpha = args[1]
    niter = args[2]
    s = [0]*len(OBJs)
    bs = s # best state found
    start = time()
    while temp > 1:
        if time() - start > execTime:
            break
        si = neightborhood(s, T, OBJs)
        for _ in range(niter):
            sn = take_Random(si)
            oValue = bp.state_Value(sn, OBJs)
            if oValue > bp.state_Value(s, OBJs):
                s = sn
                si = neightborhood(s, T, OBJs) # updating neightborhood
                if oValue > bp.state_Value(bs, OBJs):
                    bs = sn
            else:
                p = math.exp((oValue - bp.state_Value(s, OBJs))/temp)
                if random.random() < p:
                    s = sn
                    si = neightborhood(s, T, OBJs) # updating neightborhood
        temp *= alpha
    return bs

# T = 19 # bag size
# OBJs = [(1,3), (4,6), (5,7)] # object list (v,t)
# temp = 10 # initial temperature
# alpha = random.random()
# iter = 50 # number of iterations

# print(sim_Annealing(T,OBJs,temp,alpha,iter))
