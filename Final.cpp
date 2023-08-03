#include<bits/stdc++.h>
using namespace std;
int main() {
    // Write C++ code here
    int N,k;
    cout<<"Enter number of Nodes: ";
    cin>>N;
    cout<<"Enter number of Base Stations: ";
    cin>>k;
    //breaking the nodes into clusters of 2^p where p=1,2,3.. 
    vector<int> v;
    int M=N;
    while(M>0)
    {
        int x=pow(2,floor(log2(M)));
        v.push_back(x);
        M-=x;
    }
    cout<<"The clusters will be of size each :"<<endl;
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    //calculating time taken by each cluster head to forward aggregated data to the 1st BS
    cout<<endl;
    vector<int> tm;
    for(int i=0;i<v.size();i++)
    {
        int k=log2(v[i])+1;
        tm.push_back(k);
    }
    cout<<"timeslots taken by each Cluster Head(CH) to forward aggregated data to the 1st BS"<<endl;
    for(int i=0;i<tm.size();i++)
        cout<<tm[i]<<" ";
    
    stack<int> st;
    for(int i=0;i<tm.size();i++)
    {
        st.push(tm[i]);
    }
    int time=0;
    int arr[k];
    for(int i=0;i<k;i++)
    {
        arr[i]=0;
    }
    cout<<endl;
    cout<<"Intially each base station is visited 0 times as shown: "<<endl;
    for(int i=0;i<k;i++)
    {
        cout<<arr[i]<<" ";
    }
    while(!st.empty())
    {
        time+=1;
        for(int i=1;i<k;i++)
        {
            if(arr[i]<arr[i-1])
            {
                arr[i]+=1;
            }
            else
                break;
        }
        if(st.top()==time)
        {
            arr[0]+=1;
            st.pop();
        }
    }
    for(int i=1;i<k;i++)
    {
        arr[i]+=1;
        time+=1;
    }
    cout<<endl;
    cout<<"All the base stations are visited by all the clusters(whose count is equal to the number of clusters) as shown "<<endl;
    for(int i=0;i<k;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<"Total time slots taken: "<<time;
    return 0;
}
