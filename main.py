#!/usr/bin/env python3

import make_hamiltonian as mh
import make_instance as mi
import solve_problem as sop


if __name__ == '__main__':
    # set problem
    instance_data, feed_dict = mi.make_instance()
    # set costs & constraints
    problem = mh.make_hamiltonian()
    # solve problem with openjij
    result = sop.solve_problem(problem=problem, 
                                instance_data=instance_data, 
                                feed_dict=feed_dict)
    # count the number of feasible solutions
    num_feasible = 0
    for i in range(len(result)):
        if result[i]['penalty']['h1'] != 0.0:
            num_feasible += 1
    print(num_feasible) 
