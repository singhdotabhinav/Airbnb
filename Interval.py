'''
Problem 1
We wish to train a machine learning algorithm on an array of floating-point numbers in the
interval [0.0, 1.0). The data is horribly unbalanced (not evenly distributed) and we wish to
filter the dataset to obtain a subset containing an equal number of values from each interval
[0, 0.2), [0.2, 0.4), ... [0.8, 1.0), throwing away as little data as possible.
1. Write a program which reads comma-separated floating-point numbers in a single
line from stdin and prints the filtered data to stdout in the same format.
2. Provide one automated test case for your program.
Trivial example:
$ echo 0.1,0.3,0.5,0.7,0.9 | /my-program
0.1,0.3,0.5,0.7,0.9
$ echo 0.1,0.3,0.5,0.7,0.9,0.5 | /my-program
0.1,0.3,0.5,0.7,0.9
$ echo 0.3,0.5,0.7,0.9,0.5 | /my-program
None
$ echo 0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77, 0.9,0.94 | /my-program
0.15,0.12,0.35,0.38,0.55,0.56,0.75,0.77,0.9,0.94
'''
'''
Solution : 
Step 1 : The first step is collecting the data from csv file, and then convert it into an array.
         This step is kind of data preprocessing where data is converted into more usable format.
Step 2 : Iterate through array to find the number in range
         We will be using five list and filling it with the required range values
Step 3 : Print the output 

'''
# Step 1 
import pandas as pd
import numpy as np
df=pd.read_csv('file.csv', sep=',',header=None)                            # Read csv file
n=df.values                                                                # Variable n will be storing numpy array
list=n.tolist()                                                            # Convert numpy array to list
arr=list[0]
a=np.array(arr)                                                            # Convert list to array 

# Step 2

def algo(arr):                                                             # Function which take input as array
    l=len(arr)                                                             # Find length of array
    l1=[]                                                                  # Initialize five empty lists
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    for i in range(l):                                                     # Iterate through the array and if any element lies within the range then append it to list
        if arr[i] >=0.0 and arr[i]<0.2:
            l1.append(arr[i])
        elif (arr[i]>=0.2 and arr[i]<0.4):
            l2.append(arr[i])
        elif (arr[i]>=0.4 and arr[i]<0.6):
            l3.append(arr[i])
        elif (arr[i]>=0.6 and arr[i]<0.8):
            l4.append(arr[i])
        elif (arr[i]>=0.8 and arr[i]<1.0):
            l5.append(arr[i])
             
        
        
    m=min(len(l1),len(l2),len(l3),len(l4),len(l5))                         # Find min size of all lists
    if m==0:                                                               # Min size can't be zero i.e, atleast a single element must be present within range
        print("None")                                                      
    else:
        l1=l1[:m]                                                          # We are asked to find equal and minimum number of values in each interval
        l2=l2[:m]                                                          # So, slice the list to min index and print the value
        l3=l3[:m]
        l4=l4[:m]
        l4=l4[:m]
        l5=l5[:m]
        
        print(l1)
        print(l2)
        print(l3)
        print(l4)
        print(l5)
