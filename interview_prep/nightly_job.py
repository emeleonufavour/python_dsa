import numpy as np
import random

def simulate_jobs(n: int):
    data = []
    
    for i in range(n):
        first_job = random.randint(0,300)
        second_job = random.randint(0,300)

        overlap = 0
        first_overlap = (first_job > second_job and first_job <= (second_job + 60))
        second_overlap = (second_job > first_job and second_job <= (first_job + 60))
        if first_overlap or second_overlap:
            overlap = 1
        data.append(overlap)
    
    cost = 365 * (np.mean(data)) * n
    return cost