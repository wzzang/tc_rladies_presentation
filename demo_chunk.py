#!/usr/bin/env python
# coding: utf-8

import pandas as pd
filename='~/Downloads/BJ_PM25.csv'
FileReader = pd.read_csv(filename, chunksize=100, sep = ',')
dfList=[]

for df in FileReader:
    dfList.append(df)

#concatenate all chunks
chunkdf = pd.concat(dfList,sort=False)

#chunkdf.head()
#chunkdf.shape 
