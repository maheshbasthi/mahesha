# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:32:48 2023

@author: SPTINT-16
"""
import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-16/Desktop/dataset/Iris.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["PetalWidthCm"])
print(data.info())
print(data.dtypes)
print(data.count())

