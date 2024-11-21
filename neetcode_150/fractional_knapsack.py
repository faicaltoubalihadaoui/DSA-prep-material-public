def fractionalknapsack(val, wt, capacity=50):

    ratios = list(zip(val, wt))
    ratios.sort(key=lambda x: x[0] / x[1], reverse=True)

    final_value = 0

    for val, wt in ratios:
        if wt <= capacity:
            capacity -= wt
            final_value += val

        else:
            final_value += val * capacity / wt

    return final_value


result = fractionalknapsack([60, 100, 120], [10, 20, 30], 50)
print(result)

# Greedy Approach
#  Greedy choice property : choosing the best possible option at each step  => best overall solution
#  Optimal substructure   : Break the problem down into smaller parts, solving these smaller parts =>helps solve the overall problem
#
# DP require overlapping subproblems
# DP can't be solved without previous states of problems
#
#
#
#
#
#
#
