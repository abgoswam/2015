# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 12:13:42 2015

@author: agoswami

Reference(s): 
[1] http://chrisalbon.com/python/pandas_apply_operations_to_groups.html

"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'bucket': ['0', '1', '0', '0', '1', '1', '0', '0','0', '1', '2', '2'],
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
    'clicks': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'impressions': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

           
df = pd.DataFrame(raw_data)

#Group By regiment and bucket
groupbyregimentbucket = df.groupby(['regiment', 'bucket'])

print "[Grouping by regiment and bucket, and aggregating #of clicks]"
print groupbyregimentbucket['clicks'].aggregate(np.sum)

#Without the hierarchical indexing
print "[Unstacking]"
regimentbucketclicksum =  groupbyregimentbucket['clicks'].aggregate(np.sum).unstack()
print regimentbucketclicksum

regimentbucketclicksum.plot(kind = 'bar', title = ' by Regiment, Bucket')
plt.ylabel('clicks')
plt.show() 
