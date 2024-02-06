# import relevant
# modules
from scipy.optimize import minimize

# 1) define the utility
# function
def utility(x, alpha):
    # NOTE: the objective function
    # objective_fns is multiplied by
    # -1 as the minimize function, well,
    # minimizes
    objective_fns = -1 * (x[0]**alpha * x[1]**(1-alpha))
    return objective_fns

# 2) define the budget
# constraint as a linear function
def budget_constraint(x, p1, p2, income):
    # I: income
    # x: a vector of goods
    # p1 p2 Price of good 1 and good 2
    return income - ((p1*x[0]) + (p2*x[1]))


# TODO: Define it as class-object to reduce the amount of functions!