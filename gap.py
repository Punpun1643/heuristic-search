import random
from typing import List

def generateSol(numSol: int, N: int, M: int) -> List[List[int]]:
    """
    Generates a list of random solutions for a given problem.

    The function generates a specified number of random solutions, each consisting of N elements, where each element is
    an integer randomly chosen from the range [1, M].

    Parameters:
        numSol (int): The number of random solutions to generate.
        N (int): The number of elements in each generated solution.
        M (int): The upper limit for the range of integers to choose from for each element in the solutions.

    Returns:
        List[List[int]]: A list containing the randomly generated solutions. Each solution is represented as a list of N
                         integers randomly chosen from the range [1, M].

    Example:
        generatedSolutions = generateSol(100, 15, 5)
        # Returns a list of 100 solutions, each containing 15 integers randomly chosen from the range [1, 5].
        # Example output: [[4, 2, 1, 5, 3, 2, 4, 3, 1, 5, 4, 2, 5, 3, 1], ... , [3, 1, 2, 5, 4, 3, 2, 4, 5, 3, 1, 4, 2, 5, 1]]
    """
    randomSolutions = []
    for _ in range(numSol):
        randomSolutionArray = [random.randint(1, M) for _ in range(N)]
        randomSolutions.append(randomSolutionArray)
    return randomSolutions


generatedSolutions = generateSol(100, 15, 5)
print("Number of solution: ", len(generatedSolutions))
print("Number of element in each solution: ", len(generatedSolutions[0]))
print("Example of a solution: ", generatedSolutions[0])


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

exampleSolution = [4, 1, 1, 3, 3, 1, 3, 2, 4, 2, 3, 2, 4, 5, 5]

def calculateCost(solutionArr: List[int], costs: List[int]) -> int:
    """
    Calculates the total cost of a given task assignment to workers.

    This function takes a task assignment represented by a list of integers and a cost matrix.
    It calculates the total cost of the assignment based on the costs associated with assigning
    each task to a specific worker.

    Parameters:
        solutionArr (List[int]): A list representing the task assignment to workers.
            Each element of the list represents a task, and the value at that position
            represents the index of the worker to whom the task is assigned.
            (e.g., solutionArr[i] = j means task i is assigned to worker j+1.)
            The length of solutionArr should be equal to the number of tasks.
        costs (List[List[int]]): A 2D list representing the cost matrix for task assignments.
            It should have dimensions N x M, where N is the number of tasks and M is the
            number of workers. costs[i][j] represents the cost of assigning task i+1 to worker j+1.

    Returns:
        int: The total cost of the given task assignment.

    Example:
        solutionArr = [1, 2, 1, 3]
        costs = [
            [3, 2, 4],
            [5, 1, 6],
            [2, 3, 7],
            [8, 2, 3]
        ]
        calculateCost(solutionArr, costs)  # Returns 3 + 1 + 2 + 3 = 9
    """
    numElement = len(solutionArr)
    solutionCost = 0
    
    for i in range(numElement):
        taskId = i + 1
        workerId = solutionArr[i]
        costOfAssignment = costs[taskId - 1][workerId - 1]
        solutionCost += costOfAssignment
    return solutionCost

print("Solution: ", exampleSolution)
print("Solution cost: ", calculateCost(exampleSolution, costs))

def calculatePenalty(solutionArr: List[int], times: List[int], workerTimeLimits: List[int]) -> int:
    """
    Calculates the total penalty for a given task assignment to workers based on their time limits.

    This function takes a task assignment represented by a list of integers, a time matrix,
    and a list of worker time limits. It calculates the total penalty incurred by each worker
    due to exceeding their individual time limits.

    Parameters:
        solutionArr (List[int]): A list representing the task assignment to workers.
            Each element of the list represents a task, and the value at that position
            represents the index of the worker to whom the task is assigned.
            (e.g., solutionArr[i] = j means task i is assigned to worker j+1.)
            The length of solutionArr should be equal to the number of tasks.
        times (List[List[int]]): A 2D list representing the time matrix for task assignments.
            It should have dimensions N x M, where N is the number of tasks and M is the
            number of workers. times[i][j] represents the time taken by worker j+1 to complete task i+1.
        workerTimeLimits (List[int]): A list containing the time limits for each worker.
            Each element in the list represents the maximum allowed time for the corresponding worker.
            The length of workerTimeLimits should be equal to the number of workers.

    Returns:
        int: The total penalty incurred by the workers for the given task assignment.
            The penalty is the total time each worker exceeds their respective time limit.

    Example:
        solutionArr = [1, 2, 1, 3]
        times = [
            [3, 2, 4],
            [5, 1, 6],
            [2, 3, 7],
            [8, 2, 3]
        ]
        workerTimeLimits = [8, 5, 9]
        calculatePenalty(solutionArr, times, workerTimeLimits)  # Returns 0 (no time limit exceeded in this example)
    """
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

print("Solution penalty: ", calculatePenalty(exampleSolution, times, workerTimeLimits))

def calculateFitness(solutionArr: List[int], costFunction: callable, penaltyFunction: callable, costs: List[List[int]], times: List[List[int]], workerTimeLimits: List[int]) -> int: 
    """
    Calculates the fitness value of a given task assignment to workers.

    This function calculates the fitness value for a given task assignment to workers by combining
    the total cost of the assignment and the total penalty incurred by the workers for exceeding
    their individual time limits.

    Parameters:
        solutionArr (List[int]): A list representing the task assignment to workers.
            Each element of the list represents a task, and the value at that position
            represents the index of the worker to whom the task is assigned.
            (e.g., solutionArr[i] = j means task i is assigned to worker j+1.)
            The length of solutionArr should be equal to the number of tasks.
        costFunction (callable): A function that calculates the total cost of the task assignment.
            The function should take the task assignment (solutionArr) and the cost matrix (costs) as inputs.
        penaltyFunction (callable): A function that calculates the total penalty incurred by the workers
            for exceeding their individual time limits due to the task assignment.
            The function should take the task assignment (solutionArr), the time matrix (times),
            and the list of worker time limits (workerTimeLimits) as inputs.
        costs (List[List[int]]): A 2D list representing the cost matrix for task assignments.
            It should have dimensions N x M, where N is the number of tasks and M is the
            number of workers. costs[i][j] represents the cost of assigning task i+1 to worker j+1.
        times (List[List[int]]): A 2D list representing the time matrix for task assignments.
            It should have dimensions N x M, where N is the number of tasks and M is the
            number of workers. times[i][j] represents the time taken by worker j+1 to complete task i+1.
        workerTimeLimits (List[int]): A list containing the time limits for each worker.
            Each element in the list represents the maximum allowed time for the corresponding worker.
            The length of workerTimeLimits should be equal to the number of workers.

    Returns:
        int: The fitness value of the given task assignment, which is the sum of the total cost
            and the total penalty incurred by the workers.

    Example:
        solutionArr = [1, 2, 1, 3]
        costs = [
            [3, 2, 4],
            [5, 1, 6],
            [2, 3, 7],
            [8, 2, 3]
        ]
        times = [
            [3, 2, 4],
            [5, 1, 6],
            [2, 3, 7],
            [8, 2, 3]
        ]
        workerTimeLimits = [8, 5, 9]
        cost_fn = calculateCost  # Assuming this function calculates the total cost.
        penalty_fn = calculatePenalty  # Assuming this function calculates the total penalty.
        calculateFitness(solutionArr, cost_fn, penalty_fn, costs, times, workerTimeLimits)  # Returns the fitness value.
    """
    fitness = costFunction(solutionArr, costs) + 2 * penaltyFunction(solutionArr, times, workerTimeLimits)
    return fitness

print("Calculate fitness: ", calculateFitness(exampleSolution, calculateCost, calculatePenalty, costs, times, workerTimeLimits))

def isFeasibleSolution(penaltyFunction: callable, solutionArr: List[int], times: List[List[int]], workerTimeLimits: List[int]) -> bool:
    """
    Checks if a given task assignment to workers is feasible.

    This function checks whether a given task assignment to workers is feasible, i.e., if no worker
    exceeds their individual time limit due to the task assignment.

    Parameters:
        penaltyFunction (callable): A function that calculates the total penalty incurred by the workers
            for exceeding their individual time limits due to the task assignment.
            The function should take the task assignment (solutionArr), the time matrix (times),
            and the list of worker time limits (workerTimeLimits) as inputs.
        solutionArr (List[int]): A list representing the task assignment to workers.
            Each element of the list represents a task, and the value at that position
            represents the index of the worker to whom the task is assigned.
            (e.g., solutionArr[i] = j means task i is assigned to worker j+1.)
            The length of solutionArr should be equal to the number of tasks.
        times (List[List[int]]): A 2D list representing the time matrix for task assignments.
            It should have dimensions N x M, where N is the number of tasks and M is the
            number of workers. times[i][j] represents the time taken by worker j+1 to complete task i+1.
        workerTimeLimits (List[int]): A list containing the time limits for each worker.
            Each element in the list represents the maximum allowed time for the corresponding worker.
            The length of workerTimeLimits should be equal to the number of workers.

    Returns:
        bool: True if the task assignment is feasible (no worker exceeds their time limit),
            False otherwise.

    Example:
        solutionArr = [1, 2, 1, 3]
        times = [
            [3, 2, 4],
            [5, 1, 6],
            [2, 3, 7],
            [8, 2, 3]
        ]
        workerTimeLimits = [8, 5, 9]
        penalty_fn = calculatePenalty  # Assuming this function calculates the total penalty.
        isFeasibleSolution(penalty_fn, solutionArr, times, workerTimeLimits)  # Returns True or False.
    """
    return penaltyFunction(solutionArr, times, workerTimeLimits) == 0


print("Solution is feasible: ", isFeasibleSolution(calculatePenalty, exampleSolution, times, workerTimeLimits))


def whoExceedLimits(solutionArr: List[int], times: List[int], workerTimeLimits: List[int]) -> None:
    numWorkers = len(workerTimeLimits)
    workerTotalTime = [0 for i in range(numWorkers)]
    
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
        if (timeLimitExceed > 0):
            print("🚨 Worker ", j + 1, " exceeded time limit by: ", timeLimitExceed)


def outputSolution(solutions, costFunction, penaltyFunciton, costs, times, workerTimeLimits) -> None:
    solutions.append([4, 1, 1, 3, 3, 1, 3, 2, 4, 2, 3, 2, 4, 5, 5])
    for solution in solutions:
        solutionCost = costFunction(solution, costs)
        solutionPenalty = penaltyFunciton(solution, times, workerTimeLimits)
        solutionFitness = calculateFitness(solution, costFunction, penaltyFunciton, costs, times, workerTimeLimits)
        isFeasible = isFeasibleSolution(penaltyFunciton, solution, times, workerTimeLimits)
        
        print("Solution: ", solution)
        print("Cost: ", solutionCost)
        print("Penalty: ", solutionPenalty)
        print("Fitness: ", solutionFitness)
        if isFeasible:
            print("Solution is feasible ✅")
        else:
            print("Solution is not feasible ❌")
            whoExceedLimits(solution, times, workerTimeLimits)
        print("############################################\n")

outputSolution(generatedSolutions, calculateCost, calculatePenalty, costs, times, workerTimeLimits)
            

