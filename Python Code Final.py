#!/usr/bin/env python
# coding: utf-8

# In[23]:


import math


# In[24]:


N=int(input("Enter number of Nodes = "))
k=int(input("Enter number of Base Stations = "))


# In[25]:


li=[]
m=N


# In[26]:


while m>0:
    x=math.pow(2,math.floor(math.log2(m)))
    li.append(x)
    m-=x
print("The cluster will be of size each = ")


# In[27]:


for i in range(len(li)):
    print(li[i],end=" ")
print()


# In[28]:


tm=[]
#k=0
for i in range(0,len(li)):
    y=(math.log2(li[i]))+1
    tm.append(y)

print("Timeslots taken by each Cluster Head(CH) to forward aggregated data to the 1st BS")
for i in range(0,len(tm)):
    print(tm[i],end=" ")


# In[29]:



arr=[]
for i in range(0,k):
    arr.append(0)
print("Intially each base station is visited 0 times as shown: -")
for i in range(0,k):
    print(arr[i],end=" ")


# In[30]:


for i in range(0,len(tm)):
    print(tm[i],end=" ")


# In[31]:


st = []
for i in range(0,len(tm)):
    st.append(tm[i])
print(len(st))
print(len(tm))


# In[32]:


print(st)


# In[33]:


time=0


# In[34]:


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


# In[35]:


for i in range(1,k):
    arr[i]+=1
    time+=1


# In[36]:


print(time)


# In[ ]:




