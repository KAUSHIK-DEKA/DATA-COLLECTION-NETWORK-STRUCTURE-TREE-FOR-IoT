#import libraries
import pandas as pd
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
from matplotlib import cm
from scipy.interpolate import griddata
data=pd.DataFrame()
data1=pd.DataFrame()

n=int(input("Enter number of nodes: "))#take input of nodes 
k=int(input("Enter value of k: ")) #number of data streams or base stations
ni=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ii=[]
m=[]
jj=[]
um=[]
alphar=[]
betar=[]
tau1=[]
tau2=[]
T=[]
#algorithm
for i in range(30,n+1,15):
    m.append(i)
    for j in range(1,k+1):
        ii.append(i)
        jj.append(j)
        umax=math.floor(math.fabs(i)/j) #calculate Umax
        if(umax==0 or umax==1):
            alphar.append('0')
            betar.append('0')
            tau1.append(1)
            tau2.append(0)
            T.append(1)
        elif(umax%2==0 and umax>=4):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tau1.append(t1)
            tau2.append(t2)
            t=t1+t2
            T.append(t)
            nalpha=umax/2
            alphar.append(nalpha)
            betar.append('0')
        elif(umax==2):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tau1.append(t1)
            tau2.append(t2)
            t=t1+t2
            T.append(t)
            alphar.append('2')
            betar.append('0')
        elif(umax==3):
            t1=math.floor((2*(math.fabs(i)-umax)/(umax+1))+1)
            temp2=math.fabs(i)-(t1*((umax+1)/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tau1.append(t1)
            tau2.append(t2)
            t=t1+t2
            T.append(t)
            betar.append('1')
            alphar.append('0')
        elif(umax%2!=0 and umax>=5):
            t1=math.floor((2*(math.fabs(i)-umax)/(umax+1))+1)
            temp2=math.fabs(i)-(t1*((umax+1)/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tau1.append(t1)
            tau2.append(t2)
            t=t1+t2
            T.append(t)
            nalpha=(umax-3)/2
            alphar.append(nalpha)
            betar.append('1')
        um.append(umax)

data['N']=ii
data['k']=jj
data['umax']=um
data['Alpha Rings']=alphar
data['Beta Rings']=betar
data['Tau 1']=tau1
data['Tau 2']=tau2
data['T']=T

data.to_csv('col2.csv', index=False)
fig = plt.figure()
ax = fig.gca(projection = '3d')
X=np.array(ni)
Y=np.array(T)
Z=np.array(m)
Y=np.reshape(Y, (19,10))
x, z= np.meshgrid(X, Z)

surf=ax.plot_surface(x, z, Y, color=None,cmap=cm.jet)
ax.set_xlabel('Data Streams (k)')
ax.set_ylabel('Nodes (N)')
ax.set_zlabel('Time Slots (T)')
plt.show()