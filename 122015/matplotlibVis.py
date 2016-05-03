# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:44:43 2015

@author: agoswami
"""

import numpy as np
import matplotlib.pyplot as plt

def plot2():
    plt.plot([1,3,2,4])
    plt.ylabel('Intensity')
    plt.show()

def plot3():
    plt.plot([1,3,2,4], 'ro-' )
    plt.ylabel('Intensity')
    plt.show()

def plot4():  
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 4, 3, 6, 5]  
    plt.plot( x, y, ':rs' )
    plt.axis( [0, 10, 0, 6])
    plt.xlabel( "X values" )
    plt.ylabel( "Y values" )
    plt.show()

def plot5():
    data = [ (1, 0), (2, 0.1 ), (3, 1.1), (4, 1.2), (5, 2.3), 
                (6, 3.5), (7, 5.8) ]
    X = [ x for (x,y) in data ]
    Y = [ y for (x,y) in data ]
    
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 4, 3, 6, 5]  
    print X
    print Y

    plt.plot( X, Y, ':rs' )
    plt.scatter(x,y)
    plt.axis( [0, 8, 0, 6])
    plt.xlabel( "X values" )
    plt.ylabel( "Y values" )
    plt.show()

def plot6():
    t = np.arange(1, 10, 0.5)
    print t    
    plt.plot( t, t**2, 'r^--', t, 3*(t**2)-3, 'bs-' )
    plt.show()
    plt.plot( t, t**2, 'r^--')
    plt.show()

def plot7():    
    x1 =[ 1, 2, 5, 10, 15, 20]
    y1 =[ 1.5 * x**2 for x in x1 ]
    x2 = range( 5, 30)
    y2 = [ 0.3 * x**2 -5 for x in x2 ]
    plt.plot( x1, y1, "rs--", x2, y2, ":b^")
    plt.show()

def plot8():
    y = [ 3, 10, 7, 5, -3, 4.5, 6, 8.1]
    N = len( y )
    x = range( N )
    width = 1/1.5
    plt.bar( x, y, width, color="magenta" )
    plt.show()

def plot9():
    data = [ ("data1", 34), ("data2", 22),
            ("data3", 11), ( "data4", 28),
            ("data5", 57), ( "data6", 39),
            ("data7", 23), ( "data8", 98)]

    N = len( data )
    x = np.arange(1, N+1)
    y = [ num for (s, num) in data ]
    labels = [ s for (s, num) in data ]
    width = 1.0
    bar1 = plt.bar( x, y, width, color="y" )
    plt.ylabel( 'Intensity' )
    plt.xticks(x + width/2.0, labels )
    plt.show()

    
def plot11():
    t = np.arange( 0, 200, 1)
    N = len( t )
    
    y = np.random.rand( N )
    x = np.arange( 1, N+1 )

    labels = [ "data"+str(k) for k in range(1, N+1) ]
    samples = [ '' ] * N
    for i in range( 0, N, N/5 ):
        samples[i] = labels[i]
    width = 1.0
    
    plt.plot( x, y )
    plt.ylabel( 'Intensity' )
    plt.xticks(x + width/2.0, samples )
    plt.show()

def plot14():
    # the number of bins
    N = 20 

    # the samples
    samples = np.array([1, 1, 1, 3, 2, 5, 1, 50, 10, 8])

    plt.hist(samples)
#    n, bins, patches  = plt.hist( samples, N, facecolor="magenta", range=[1,N], normed=True)
#    n, bins, patches  = plt.hist( samples, N, facecolor="magenta", range=[1,N], normed=True, cumulative=True )
#    n, bins, patches  = plt.hist( samples, N, facecolor="magenta", range=[1,N], normed=False)

    plt.xlabel( 'bins' )
    plt.ylabel( 'Probability' )
    plt.show()

def plot15():
    N = 12
    samples1 = np.array([1, 1, 1, 3, 2, 5, 1, 10, 10, 8])
    samples2 = np.array([5,5,5,5,6,7,1,1,2,12,12,12,9,3,4])
    
    plt.figure( 1 )

    plt.subplot( 2, 1, 1 ) # 2 rows, 1 column, figure 1
    n1, bins1, patches1  = plt.hist( samples1, N, facecolor="m", range=[1,N], normed=True )
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Probability (magenta)' )
    
    plt.subplot( 2, 1, 2 )
    n2, bins2, patches2  = plt.hist( samples2, N, facecolor="y", range=[1,N], normed=True )
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Probability (yellow)' )
    
    plt.show()

def plot16():
    N = 12 # the number of bins
    samples1 = np.array([1, 1, 1, 3, 2, 5, 1, 10, 10, 8])
    samples2 = np.array([5,5,5,5,6,7,1,1,2,12,12,12,9,3,4])
    samples3 = np.array([1,2,3,4,5,6,6,7,8,9,10,10,11,12])
    samples4 = np.array([1,2,2,2,2,2,2,2,2,10,11,12])
    
    plt.figure( 1 )

    #--- top left ---
    plt.subplot( 2, 2, 1 ) 
    n1, bins1, patches1  = plt.hist( samples1, N, facecolor="m", range=[1,N], normed=True )
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Probability (magenta)' )
    plt.title( "Sample 1 Frequencies")
    
    #--- top right ---
    plt.subplot( 2, 2, 2 )
    n2, bins2, patches2  = plt.hist( samples2, N, facecolor="y", range=[1,N], normed=True )
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Probability (yellow)' )
    plt.title( "Sample 2 Frequencies")

    #--- bottom left ---
    plt.subplot( 2, 2, 3 )
    n3, bins3, patches3  = plt.hist( samples3, N, facecolor="grey", range=[1,N], normed=False )
    plt.title( "Sample 3 Counts")
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Count (grey)' )
    
    #--- bottom right ---
    plt.subplot( 2, 2, 4 )
    n4, bins4, patches4  = plt.hist( samples4, N, facecolor="r", range=[1,N], normed=False )
    plt.title( "Sample 4 Counts")
    plt.xlabel( 'Bins' )
    plt.ylabel( 'Count (red)' )

    plt.show()


plot2()
plot3()
plot4()
plot5()
plot6()
plot7()
plot8()
plot9()
plot11()
plot14()
plot15()
plot16()