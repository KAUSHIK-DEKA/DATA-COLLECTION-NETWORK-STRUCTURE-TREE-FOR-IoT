# N is incremented in steps of 15 till N+1 while K is kept constant

# Proposed Model
import math
import matplotlib.pyplot as plt

N=int(input("Enter number of Nodes = "))
k=int(input("Enter number of Base Stations = "))

mx=[]
timing=[]
for m in range(30,N+1,15):
    mx.append(m)
    li=[]
    while m>0:
        x=math.pow(2,math.floor(math.log2(m)))
        li.append(x)
        m-=x

    tm=[]
    for i in range(0,len(li)):
        y=(math.log2(li[i]))+1
        tm.append(y)

    arr=[]
    for i in range(0,k):
        arr.append(0)

    st = []
    for i in range(0,len(tm)):
        st.append(tm[i])

    time=0
    while st:
        time+=1
        for i in range(1,k):
            if arr[i]<arr[i-1]:
                arr[i]+=1
            else:
                break
        if st[-1]==time:
            arr[0]+=1
            st.pop()

    for i in range(1,k):
        arr[i]+=1
        time+=1
    timing.append(time)

print(mx) 
print("TimeSlots for Proposed Model")
print(timing)

# CDCT

m=[]
jj=[]
um=[]
alphar=[]
betar=[]
tauA=[]
tauB=[]
T=[]
#algorithm
for i in range(30,N+1,15):
        m.append(i)
        umax=math.floor(math.fabs(i)/k) #calculate Umax
        if(umax==0 or umax==1):
            alphar.append('0')
            betar.append('0')
            tauA.append(1)
            tauB.append(0)
            T.append(1)
        elif(umax%2==0 and umax>=4):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tauA.append(t1)
            tauB.append(t2)
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
            tauA.append(t1)
            tauB.append(t2)
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
            tauA.append(t1)
            tauB.append(t2)
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
            tauA.append(t1)
            tauB.append(t2)
            t=t1+t2
            T.append(t)
            nalpha=(umax-3)/2
            alphar.append(nalpha)
            betar.append('1')
        um.append(umax)
print("TimeSlots for CDCT")
print(T)


# Time Optimal CDCT         
m1=[]
um1=[]
alphar1=[]
betar1=[]
tau1=[]
tau2=[]
T1=[]
for i in range(30,N+1,15):
        m1.append(i)
        #Compute the value of umax from equation
        umax=math.floor(math.fabs(i)/k)
        if(umax % 3 == 0):
          nbeta=umax/3
          nalpha=0
          betar1.append(nbeta)
          alphar1.append('0')
        elif(umax %3 ==1):
          nbeta=math.floor(umax/3)-1
          nalpha=2
          betar1.append(nbeta)
          alphar1.append('2')
        else:
          nbeta=math.floor(umax/3)
          nalpha=1
          betar1.append(nbeta)
          alphar1.append('1')
        if(umax==0 or umax==1):
            alphar1.append('0')
            betar1.append('0')
            tau1.append(1)
            tau2.append(0)
            T1.append(1)
        elif(umax == 2 or umax == 4):
            t1=math.floor((2*(math.fabs(i)-umax)/umax)+1)
            temp2=math.fabs(i)-(t1*(umax/2))
            if(temp2>0):
                t2=math.floor(math.log2(temp2))+1
            else:
                t2=0
            tau1.append(t1)
            tau2.append(t2)
            t=t1+t2
            T1.append(t)
        else:
            x=nalpha*2*k+nbeta*3*k
            r=i-x
            if(nbeta>=1):
              nbetamin=3*k+math.floor(r/nbeta)
              t1= math.ceil(math.fabs(nbetamin)/2)-1
              if(nbeta<nalpha and (umax%3)==0):
                temp2=math.fabs(i)-(t1*(math.ceil(umax+nbeta)/2))
                if(temp2>0):
                  t2=math.floor(math.log2(temp2))+1
                else:
                  t2=0
              else:
                temp2=math.fabs(i)-(t1*(math.ceil(umax+nalpha)/2))
                if(temp2>0):
                  t2=math.floor(math.log2(temp2))+1
                else:
                  t2=0
              tau1.append(t1)
              tau2.append(t2)
              t=t1+t2
              T1.append(t)
        um1.append(umax)
print("TimeSlots for Time Optimal CDCT")
print(T1)

plt.plot(mx,timing,"-b", label="Proposed Model")
plt.plot(mx,T,"-g", label="CDCT")
plt.plot(mx,T1,"-r", label="TOCDCT")
plt.legend(loc="upper left")
plt.xlabel("Number of Nodes")
plt.ylabel("Time Slot")
plt.show()