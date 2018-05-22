
import pandas as pd
import numpy as np
from random import randint
import random
from gen_data import *

size_data = 30000
initial_year = 1985
end_year = 2000
name_out_file = "data.csv"

disciplines = ["Literature", "Biology", "ComputerScience", "Economics", "PolScience", 
    "Medicine", "Physics"]

d = pd.DataFrame(0, index=np.arange(size_data), columns=["year", "discipline"])
weights = gen_weights(1985, 1985, 2000, disciplines)
dis = gen_disciplines(weights, disciplines, initial_year, end_year, size_data)
years = gen_years(1985, 2000, size_data)

d["year"] = years
d["discipline"] = dis

d.to_csv(name_out_file, index = None)

