import numpy as np
import matplotlib.pyplot as plt

def graphing_min(x,y):
    
    i0 = min(y)
    for i in range(0,len(y)):
        if i0 == y[i]:
            break
    f0 = x[i]
    
    for i in range(len(y)):
        if y[i] < i0*np.sqrt(2):
            break
    y_min_index, y_nmin_index = i,i-1
    y_minute = np.linspace(y[y_min_index], y[y_nmin_index], 100000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] > i0*np.sqrt(2):
            break
    x_lminute, x_rminute = np.linspace(x[y_min_index],x[y_min_index-1],100000),np.linspace(x[y_min_index],x[y_min_index+1],100000)
    bandwidth = x_rminute[i] - x_lminute[i]

    plotting(x,y)
    return bandwidth

def graphing_max(x,y):
    
    i0 = max(y)
    for i in range(0,len(y)):
        if i0 == y[i]:
            break

    f0 = x[i]
    
    for i in range(len(y)):
        if y[i] > i0/np.sqrt(2):
            break
    y_max_index, y_nmax_index = i,i+1
    y_minute = np.linspace(y[y_max_index], y[y_nmax_index], 1000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] < i0/np.sqrt(2):
            break
    x_lminute, x_rminute = np.linspace(x[y_max_index],x[y_max_index-1],1000),np.linspace(x[y_max_index],x[y_max_index+1],1000)
    bandwidth = x_rminute[i] - x_lminute[i]

    
    plotting(x,y)
    return bandwidth

def graphing_decrease(x,y):
    i0 = max(y)
    for i in range(0,len(y)):
        if i0 == y[i] and y[i]!=y[i+1]:
            break
    print(i)
    f0 = x[i]
    
    for i in range(len(y)):
        if y[i] < i0/np.sqrt(2):
            break
    y_max_index, y_nmax_index = i, i+1
    y_minute = np.linspace(y[y_max_index], y[y_nmax_index], 1000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] < i0/np.sqrt(2):
            break
    print(i)
    x_minute = np.linspace(x[y_max_index],x[y_nmax_index],1000)
    bandwidth = x_minute[i]
    
    
    plotting(x,y)
    return bandwidth


def graphing_increase(x,y):
    i0 = max(y)
    for i in range(0,len(y)):
        if i0 == y[i] and y[i]==y[i+1]:
            break
    f0 = x[i]
    
    for i in range(len(y)):
        if y[i] > i0/np.sqrt(2):
            break
    y_max_index, y_nmax_index = i, i-1
    y_minute = np.linspace(y[y_max_index], y[y_nmax_index], 1000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] < i0/np.sqrt(2):
            break
    x_minute = np.linspace(x[y_max_index],x[y_nmax_index],1000)
    bandwidth = x_minute[i]
    
    
    plotting(x,y)
    return bandwidth



def graphing_dual(x,y):
    
    plotting(x,y)
    
    
    l_index, r_index = 0, 0
    for i in range(len(y)):
        if y[i]==y[i+1] and l_index==0:
            l_index = i
        if y[i]>y[i+1] and l_index!=0:
            r_index = i
            break
    
    i0 = max(y)
    for i in range(0,l_index):
        if y[i] > i0/np.sqrt(2):
            break
    y_max_index, y_nmax_index = i, i-1
    y_minute = np.linspace(y[y_max_index], y[y_nmax_index], 1000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] < i0/np.sqrt(2):
            break
    x_minute = np.linspace(x[y_max_index],x[y_nmax_index],1000)
    lf = x_minute[i]
    
    
    for i in range(l_index+1,r_index):
        if y[i] > i0/np.sqrt(2):
            break
    y_max_index, y_nmax_index = i, i+1
    y_minute = np.linspace(y[y_max_index], y[y_nmax_index], 1000)
    i=0
    for i in range(len(y_minute)):
        if y_minute[i] < i0/np.sqrt(2):
            break
    x_minute = np.linspace(x[y_max_index],x[y_nmax_index],1000)
    rf = x_minute[i]
    return rf - lf



def plotting(x,y):
    
    plt.loglog(x,y,color='blue')
    plt.scatter(x,y,color='red',lw=3)
    plt.title("Graph of frequency vs current")
    plt.grid(which="both")
    plt.xlabel("Frequency")
    plt.ylabel("Current")
    plt.show()

def main(x,y):
    y_max, y_min = max(y),min(y)
    count = 0
    
    for i in range(len(x)-1):
        if y[i] == y[i+1]:
                count = count+1
    if count!=0:
        if y[0] == y_max or y[-1] == y_max:
            if y[0] == y[1] or y[1]==y[2]:
                bandwidth = graphing_decrease(x,y)
            elif y[-1] == y[-2] or y[-2] == y[-3]:
                bandwidth = graphing_increase(x,y)
        else:
            bandwidth = graphing_dual(x,y)
    else:
        if y.index(y_max) !=0:
            bandwidth = graphing_max(x,y)
        else:
            bandwidth = graphing_min(x,y)
    return bandwidth
            
