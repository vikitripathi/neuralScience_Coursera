# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 04:52:27 2014

@author: img-05
"""

#import these modules, use  the documentation to learn more about these modules mainly numpy ,scipy ,pandas and matplotlib
import numpy as np
from scipy import optimize,polyfit
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd

#data=np.random.rand(1000)
#p.plot(data)
#p.hist(data)
#datan=np.random.randn(1000)
#p.hist(datan,20,cumulative=True)#here random nos are from normal distributions(bell curve)
# ^ control random nos
#help(p.hist)
#p.xlabel('bla ')
#p.title('lol')
x=np.arange(0,360,45)
print x
spike=np.random.rand(8)*20 #8 RANDOM NO B/W 0 AND 1 MULTIPLIED BY 20 EACH
#p.bar(x,spike,width=45)
print spike
#p.polar(spike)
spike2=np.append(spike,spike[0])
theta=np.arange(0,361,45)
#plt.polar(theta*np.pi/180,spike2)
#fit curve
jitter_amp=4.0
x=np.linspace(0,10,50)
jitter=jitter_amp * (np.random.random(50)-.5) 
y=x+jitter
#plt.plot(x,y,'o')
m,b=polyfit(x,y,1)
print [m,b]#m is the slope and b is the intercept
#plt.plot(x,y,'o',hold=True)
#t=np.array([0,10])
#plt.plot(t,m*t+b)
#print t
# or use optimize

def fit_func(t,m,b):
    return m*t+b
p,cov=optimize.curve_fit(fit_func,x,y)
#plt.plot(x,y,'o',hold=True)
t=np.array([0,10])    
#plt.plot(t,p[0]*t+p[1])
#labels and titles
mean=0.0
var=1.0
sigma=np.sqrt(var)
x=np.linspace(-4,4,80)
#plt.plot(x,mlab.normpdf(x,mean,sigma))

#non linear fit
#use optimize

"""
-------------Data Frames--------------
"""
a=np.random.randint(0,100,10)
b=np.random.rand(10)
c=['male','female']*5
print b
print c
df=pd.DataFrame({'ints':a,'floats':b,'gender':c})
print df
#df is an object
print df.describe()
print df[['ints']]

#add images to plot using  matplotlib
