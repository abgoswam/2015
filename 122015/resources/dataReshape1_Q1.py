# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 12:11:14 2015

@author: agoswami
"""

import pandas as pd

df = pd.read_csv(r'E:\datasets\12Dec\ReshapingData1_Q1.txt', sep = '\t')

byidyear = df.groupby(['ID', 'Year'])
reshaped = byidyear['Value'].mean().unstack()

reshaped.to_csv(r'E:\datasets\12Dec\ReshapedData1_Q1_Python.txt', sep='\t')