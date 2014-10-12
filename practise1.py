# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 07:02:06 2014

@author: img-05
"""
import numpy as np
import matplotlib 
import matplotlib.pylab as plt
#the above modules are imported for plotting graph 

print 'hello world!'
print type(3.14)
print type('3')
# below are for int and float
print 5//2 #gives quotient
print 3**2 #3^2
print type(4==5) #type is bool
# order of operation PEMDAS
print len('neuroscience')
print 'neuroscience'[5]
print 'neuroscience'[1:len('neuroscience')-2]
title = "single quotes to work fine here !!" # can 't be a python reserved keyword!!
print title
print type(title)
x=2 
y=4
print x
print 'x=',x
#double assignment to swap the values or you can add and swap the values
x,y=y,x
print 'x=',x
print 'y=',y
print not(True)
print (x==4) and (x<5)
if x>0:
    print 'x is positive'
elif x<0:
    print 'x is negative'
else:
    print 'x is zero!'

#^ indenting and white spaces are important 
#loops below!
while x>0:
    print x
    x=x-1
print 'loop ended'    
#for loop!!
for x in range(2,5):
    print x #it will print 2 3 4
print 'for loop ended!' 
x=4   
for i in range(x):
    print i
    x=10 #this change of x doesn't effect the loop
#list below!!
mylist=[1,2,3]
print mylist    #[1,2,3]
list1 = range(0,10)
print list1
list2=[1,2,3,True] #a list can have any kind of datatype
print list2
name='abhishe dutt'
print name[1:5]
x=[1,2,3,4,5,6]
print x
y=[]
for val in x:
    y.append(val**2)
print y    
print y[-1] #last element of y list 
y[-1]=63
print y[-1]
y[0],y[-1]=y[-1],y[0] #swapping elements in a list
print y
print len(y)
print y+x  
print y*2 #repeat y
y.sort()
print y
#functions below!!
def print_hello(name):
    print 'hello!!'+name+'!!'
#print_hello    #it would just say that function existed as object    
print_hello('vicky') #this is function call

def median(datalist):
    datalist.sort()
    if (len(datalist)%2):
        print 'hi!!'
listA=[1,2,3,4,5]    
print listA    
median(listA)   #odd so print hii!!
#list are passed by reference so vaue changes
print listA
#python plotting!!!
#%matplotlib inline  .. write this in terminal
x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x))
plt.title('A sinewave')
plt.show()

print np
#%load url


  
    