import pandas as pd
import numpy as np
import time

s_time = time.time()
df = pd.read_csv("customerData.csv")
e_time = time.time()

print("Read without chunks: ", (e_time-s_time), "seconds") 
