# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 07:14:40 2015

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot(title = 'Plot random values by Date.')
plt.ylabel('random number')
plt.show()
print "Fig 0 -----------------"

df1 = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df1 = df1.cumsum()
df1[['A', 'B']].plot();
plt.show()
print "Fig 1 -----------------"

df2 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df2['A'] = pd.Series(range(len(df2)))
df2.plot(y='B')
#df3.plot(x='A', y='B')
plt.show()
print "Fig 2 -----------------"

dates = pd.date_range('20130101', periods=6)
df3 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df3.plot(kind='bar');
plt.show()
print "Fig 3 -----------------"

df4 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df4.plot(kind='bar');
plt.show()
print "Fig 4 -----------------"

df5 = df3[['A', 'B']]
df5.plot(kind='bar')
plt.show()
print "Fig 5 -----------------"

values = [[1, 2, 1.5], [2, 5, 3]]
df6 = pd.DataFrame(values, columns=['Type A', 'Type B', 'Type 3'], index=['Index 1','Index 2'])
df6.plot(lw=2,colormap='jet',marker='.',markersize=10,title='Video streaming dropout by category')
plt.show()
print "Fig 6 -----------------"

df7 = pd.DataFrame({
    'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),'c': np.random.randn(1000) - 1})
df7['a'].plot(kind='hist', alpha=0.5)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
print "Fig 7 (a) -----------------"

plt.hist(df7['a'])
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
print "Fig 7 (b) -----------------"

df7.hist(color='k', alpha=0.5, bins=50)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
print "Fig 7(c) -----------------"

df7['a'].hist()
plt.xlabel('X Label')
plt.ylabel('Y Label')
print "Fig 7(d) -----------------"




