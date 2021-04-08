#!/usr/bin/env python3


def make_instance():
    objects = []
    capacity = 60
    with open('instance_generator/d.in', 'r') as f:
        num_objects = f.readline()
        for i in range(int(num_objects)):
            line = f.readline()
            line = line.split()
            # dictionary of objects = {object number: (value, weight)}
            objects.append([int(line[1]), int(line[2])])
    # set coeff for slack variables
    coeff = [1, 2, 4, 8]
    instance_data = {'objects': objects, 
                        'capacity': capacity, 
                        'coeff': coeff}
    # set hyperparameters
    feed_dict = {'h1': 1.0}
    return instance_data, feed_dict
    