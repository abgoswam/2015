# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 12:35:47 2015

@author: agoswami
"""

import pandas as pd

df = pd.read_csv(r'E:\datasets\12Dec\ReshapingData1_Q2.txt', sep = '\t')

bydatelanguageapp = df.groupby(['Date', 'LanguageTag', 'App'])
df_groupedmean = bydatelanguageapp['AcceptanceRate'].mean()

#Unstack the App
reshaped = df_groupedmean.unstack()

reshaped.to_csv(r'E:\datasets\12Dec\ReshapedData1_Q2_Python.txt', sep='\t')