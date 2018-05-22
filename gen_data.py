
import pandas as pd
import numpy as np
from random import randint
import random

def gen_weights(year, base_year, end_year, disciplines):
    '''
    '''

    weights = []

    for i in range(base_year, end_year + 1):
        w_year = []
        for j in range(len(disciplines)):
            w = (i - base_year) * (j * .03) + 0.1
            w_year.append(w)

        weights.append(w_year)

    return weights


def gen_disciplines(weights, disciplines, base_year, end_year, size_data):
    '''
    '''
    portion = int((size_data / ((end_year - base_year) + 1)) // 1)

    all_compilation  = []

    for i, year in enumerate(range(base_year, end_year + 1)):
        per_year = random.choices(disciplines, weights[i], k=portion)
        all_compilation += per_year

    return all_compilation


def gen_years(base_year, end_year, size_data):
    
    portion = int((size_data / ((end_year - base_year) + 1)) // 1)

    all_years = []
    for i in range(base_year, end_year + 1):
        y = [i] * portion
        all_years += y

    return all_years




