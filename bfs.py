from typing import List
from collections import deque
import math

costs = [
    [19, 25, 16, 25, 25],
    [23, 24, 21, 24, 19],
    [24, 16, 25, 18, 21],
    [20, 21, 22, 19, 22],
    [20, 19, 24, 15, 20],
    [25, 17, 24, 18, 15],
    [16, 17, 16, 20, 20],
    [21, 19, 17, 22, 19],
    [24, 23, 15, 23, 18],
    [15, 21, 18, 18, 18],
    [17, 21, 15, 16, 17],
    [17, 23, 17, 19, 23],
    [20, 20, 18, 17, 17],
    [20, 15, 24, 15, 25],
    [20, 16, 18, 22, 25]
]

times = [
    [16, 16, 6, 18, 12],
    [12, 18, 20, 23, 17],
    [8, 19,	20,	25,	15],
    [20, 22, 5,	17, 25],
    [18, 13, 14, 25, 22],
    [10, 20, 12, 13, 5],
    [12, 9,	6, 23, 24],
    [8,	7, 15, 23, 19],
    [14, 25, 22, 13, 12],
    [23, 10, 18, 20, 25],
    [19, 20, 13, 20, 23],
    [14, 13, 23, 23, 21],
    [15, 11, 23, 17, 23],
    [15, 15, 18, 19, 19],
    [24, 16, 25, 24, 18]
]

workerTimeLimits = [36,	37,	38,	48,	44]


def calculatePenalty(solutionArr: List[int], times: List[int], workerTimeLimits: List[int]) -> int:
    numWorkers = len(workerTimeLimits)
    workerTotalTime = [0 for i in range(numWorkers)]
    totalPenalty = 0
    
    numElement = len(solutionArr)
    
    # get total time worked by each worker
    for i in range(numElement):
        taskId = i + 1
        workerId = solutionArr[i]
        timeOfAssignment = times[taskId - 1][workerId - 1]
        
        workerTotalTime[workerId - 1] += timeOfAssignment
    
    # calculate total penalty for the solution
    for j in range(numWorkers):
        timeLimitExceed = workerTotalTime[j] - workerTimeLimits[j]
        
        if timeLimitExceed > 0:
            totalPenalty += timeLimitExceed
    
    return totalPenalty


def calculateCost(solutionArr: List[int], costs: List[int]) -> int:
    numElement = len(solutionArr)
    solutionCost = 0
    
    for i in range(numElement):
        taskId = i + 1
        workerId = solutionArr[i]
        costOfAssignment = costs[taskId - 1][workerId - 1]
        solutionCost += costOfAssignment
    return solutionCost


def isFeasibleSolution(penaltyFunction: callable, solutionArr: List[int], times: List[List[int]], workerTimeLimits: List[int]) -> bool:
    return penaltyFunction(solutionArr, times, workerTimeLimits) <= 0


def generateFeasibleSol(penaltyFunction: callable, times: List[List[int]], workerTimeLimits: List[List[int]], firstNode: int, numTask: int) -> List[List[int]]:
    numWorker= 5
    currTask = 1
    queue = deque()
    
    # assign starting worker to task 1
    queue.append([firstNode])
    
    while queue is not None and currTask <= numTask:
        allSol = []
        print("currTask: ", currTask)
        lenFrontier = len(queue)
        
        for i in range(lenFrontier):
            currSol = queue.popleft()
            print("Curr sol: ", currSol)
            
            if len(currSol) == numTask:
                allSol.append(currSol)
          
            # add child nodes to queue  
            else:   
                for i in range(numWorker):
                    tempCurrSol = currSol.copy() 
                    tempCurrSol.append(i+1)
                    if isFeasibleSolution(penaltyFunction, tempCurrSol, times, workerTimeLimits):
                        queue.append(tempCurrSol)
        currTask += 1
      
    return allSol


def getOptimalSol(generator: callable) -> List[int]:
    bestCost = math.inf
    bestSol = None
    
    for i in range(5):
        sols = generator(calculatePenalty, times, workerTimeLimits, i + 1, 15)
        for sol in sols:
            currCost = calculateCost(sol, costs)
            if currCost < bestCost:
                bestCost = currCost
                bestSol = sol
    
    return (bestSol, bestCost)


def getAllOptimalSols(generator: callable) -> List[List[int]]:
    bestCost = math.inf
    bestSols = []
    
    for i in range(5):
        sols = generator(calculatePenalty, times, workerTimeLimits, i + 1, 15)
        for sol in sols:
            currCost = calculateCost(sol, costs)
            if currCost < bestCost:
                bestCost = currCost
          
                bestSols = [sol]
            elif currCost == bestCost:
                bestSols.append(sol)
    
    return bestSols

# generates a feasible solution
# print(getOptimalSol(generateFeasibleSol)) # output: ([3, 1, 1, 3, 4, 5, 3, 2, 5, 2, 3, 1, 5, 4, 2], 269)

# generates all optimal solutions
print(getAllOptimalSols(generateFeasibleSol)) # output: [[3, 1, 1, 3, 4, 5, 3, 2, 5, 2, 3, 1, 5, 4, 2], [3, 1, 1, 3, 4, 5, 3, 2, 5, 5, 3, 1, 2, 4, 2]]
