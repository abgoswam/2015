# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 16:59:30 2015

@author: agoswami

[1] http://chrisalbon.com/python/pandas_join_merge_dataframe.html

"""

import pandas as pd

df_userfeatures = pd.read_csv(r'E:\datasets\12Dec\UserFeatures.txt', sep='\t')
df_docfeatures = pd.read_csv(r'E:\datasets\12Dec\DocFeatures.txt', sep='\t')
df_labeleddata = pd.read_csv(r'E:\datasets\12Dec\LabeledData.txt', sep='\t')

byuseridfeatures = df_userfeatures.groupby(['UserId', 'FeatureName'])
bydocidfeatures = df_docfeatures.groupby(['DocId', 'FeatureName'])

df_byuserid_transpose = byuseridfeatures['FeatureValue'].mean().unstack().reset_index()
df_bydocid_transpose = bydocidfeatures['FeatureValue'].mean().unstack().reset_index()

df_joinintermediate = pd.merge(df_labeleddata, df_byuserid_transpose, left_on='UserId', right_on='UserId', how='left')
df_joined = pd.merge(df_joinintermediate, df_bydocid_transpose, left_on='DocId', right_on='DocId', how='left')

df_joined.to_csv(r'E:\datasets\12Dec\TransposeJoin_Python.txt', index=False, sep='\t')