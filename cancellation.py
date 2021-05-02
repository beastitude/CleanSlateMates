import pandas as pd
import numpy as np

cleanerinfo = pd.read_csv("/Users/macos/Library/Mobile Documents/com~apple~CloudDocs/python/clean slate mates/csm_cleaner info - Sheet1.csv", index_col= 0)

#select time arrived column
time_col = cleanerinfo["time arrived"]
print(time_col)

#select a specific cleaner's info
print(cleanerinfo.loc[["NX"]])

#select a specific cleaner's column
print(cleanerinfo.iloc[[2,2]])