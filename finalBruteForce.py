from typing import List
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

def calculateCost(solutionArr: List[int], costs: List[int]) -> int:
    numElement = len(solutionArr)
    solutionCost = 0
    
    for i in range(numElement):
        taskId = i + 1
        workerId = solutionArr[i]
        costOfAssignment = costs[taskId - 1][workerId - 1]
        solutionCost += costOfAssignment
    return solutionCost


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
        
        # fix
        if timeLimitExceed > 0:
            totalPenalty += timeLimitExceed
    
    return totalPenalty


def calculateFitness(solutionArr: List[int], costFunction: callable, penaltyFunction: callable, costs: List[List[int]], times: List[List[int]], workerTimeLimits: List[int]) -> int: 
    fitness = costFunction(solutionArr, costs) + 2 * penaltyFunction(solutionArr, times, workerTimeLimits)
    return fitness


def isFeasibleSolution(penaltyFunction: callable, solutionArr: List[int], times: List[List[int]], workerTimeLimits: List[int]) -> bool:
    return penaltyFunction(solutionArr, times, workerTimeLimits) <= 0


def generateCombination(curr, n, k, output_file):
    ans = []
    
    if len(curr) == k:
        if isFeasibleSolution(calculatePenalty, curr, times, workerTimeLimits):
            solFitness = calculateFitness(curr, calculateCost, calculatePenalty, costs, times, workerTimeLimits)
            output_file.write("Sol: {}\tFitness: {}\n".format(curr, solFitness))

        print(curr)
        ans.append(curr[:])
        return 
    
    for i in range(1, n + 1):
        curr.append(i)
        generateCombination(curr, n, k, output_file)
        curr.pop()
        
    return ans

# generateCombination([], 5, 15, )
with open("output.txt", "w") as output_file:
    generateCombination([], 5, 15, output_file)

# import math

# bestSol = None

# def generateCombination(curr, n, k, output_file):
#     global bestSol

#     ans = []
#     minFitness = math.inf
    
#     if len(curr) == k:
#         if isFeasibleSolution(calculatePenalty, curr, times, workerTimeLimits):
#             print("✅")
#             solFitness = calculateFitness(curr, calculateCost, calculatePenalty, costs, times, workerTimeLimits)
#             if solFitness < minFitness:
#                 bestSol = curr
#                 minFitness = solFitness
#         print("Best sol: ", bestSol)
#         print(curr)
    
#         output_file.write("Best sol: {}\n".format(bestSol))
#         output_file.write("{}\n".format(curr))
#         ans.append(curr[:])
#         return
    
#     for i in range(1, n + 1):
#         curr.append(i)
#         generateCombination(curr, n, k, output_file)
#         curr.pop()
# def findBestSol():
#     def generateCombination(curr, n, k, output_file, bestSol, minFitness):

#         ans = []
        

#         if len(curr) == k:
#             if isFeasibleSolution(calculatePenalty, curr, times, workerTimeLimits) and calculateFitness(curr, calculateCost, calculatePenalty, costs, times, workerTimeLimits) < minFitness:
#                 print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
#                 bestSol = curr
#                 minFitness = calculateFitness(curr, calculateCost, calculatePenalty, costs, times, workerTimeLimits)
#                 if bestSol:
#                     output_file.write("Best sol: {}\n".format(bestSol))
#                     output_file.write("{}\n".format(curr))
#             print("Best sol: ", bestSol)
#             print(curr)
#             ans.append(curr[:])
#             return
        
#         for i in range(1, n + 1):
#             curr.append(i)
#             generateCombination(curr, n, k, output_file, bestSol, minFitness)
#             curr.pop()
#     # Example usage
#     with open("output.txt", "w") as output_file:
#         generateCombination([], 5, 15, output_file, bestSol, minFitness)

# findBestSol()

# print("Best solution found:", bestSol)