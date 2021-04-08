#!/usr/bin/env python3

import jijmodeling as jm


def make_hamiltonian():
    # set problem
    problem = jm.Problem('knapsack_test')
    # define variables
    objects = jm.PlaceholderArray('objects', dim=2)
    capacity = jm.Placeholder('capacity')
    num_o = objects.shape[0]
    x = jm.BinaryArray('x', shape=(num_o))
    coeff = jm.PlaceholderArray('coeff', dim=1)
    num_coeff = coeff.shape[0]
    y = jm.BinaryArray('y', shape=(num_coeff))
    # y = jm.LogEncInteger('y', lower=0, upper=capacity)
    # set constraint of capacity
    tmp = capacity - jm.Sum({'i': num_o}, objects['i', 1]*x['i']) - jm.Sum({'i': num_coeff}, coeff['i']*y['i'])
    # tmp = capacity - jm.Sum({'i': num_o}, objects['i', 1]*x['i']) - y
    const = jm.Constraint('h1', tmp**2)
    # set objective function
    obj = - jm.Sum({'i': num_o}, objects['i', 0]*x['i'])
    # compute total hamiltonian
    problem += obj + const
    return problem
