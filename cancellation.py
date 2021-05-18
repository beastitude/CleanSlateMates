import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cleanerinfo = pd.read_csv("csm_cleaner info - Sheet1.csv", index_col= 0)

#select time arrived column
time_col = cleanerinfo["time_arrived"]
print(time_col)

#select a specific cleaner's info
print(cleanerinfo.loc[["NX"]])

#select a specific cleaner's column
print(cleanerinfo.iloc[[2,1]])

plt.plot(cleanerinfo.time_arrived,
         cleanerinfo.tasks)
plt.xlabel("time arrived")
plt.ylabel("tasks")
plt.show