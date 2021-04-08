#!/usr/bin/env python3

import openjij as oj


def solve_problem(problem, instance_data, feed_dict):
    # convert to PyQUBO
    pyq = problem.to_pyqubo(placeholder=instance_data)
    # compile
    compiled = pyq.compile()
    # convert to bqm
    bqm = compiled.to_bqm(feed_dict=feed_dict)
    # solve with SA (OpenJij)
    sampler = oj.SASampler()
    response = sampler.sample(bqm, num_reads=1000, num_sweeps=100)
    # decode for analysis
    # decoded_lowest = problem.decode(response.lowest())
    decoded_all = problem.decode(response)
    # extract result
    result = decoded_all
    return result