import random
import time
import matplotlib.pyplot as plt
import numpy

def merge(left, right):
    """
    merge 2 list as a sorted list with mergesort algorithm
    """

    ## if the list is empty
    if not len(left) or not len(right):
        return left or right

    ## merge the list in sorted manner
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result


def arstar(RL):
    """
    Go through the list to break the list into sorted segements. Merge the
    segmented sorted slices to a sorted list works in a similar way as
    mergesort. Best case will bigO(n). Worst case bigO(nlogn)
    """
    l = len(RL)
    if l > 1:
        ## go through the list to break it into sorted slices
        prev = RL[0]
        DL = []
        i = 0
        for indx, item in enumerate(RL):
            if item < prev:
                DL += [RL[i:indx]]
                i = indx
                
            prev = item
        DL += [RL[i:]]

        ## merge the list into single sorted list
        i = 0
        while len(DL[-1]) < l:
            a = DL[i]
            DL[i] = []  ## Reduce the RAM requirement
            i += 1
            b = DL[i]
            DL[i] = []  ## Reduce the RAM requirement
            i += 1
            DL.append(merge(a,b))
            
        return DL[-1]

    else:
        return RL

###############################################
    ######  Auxilary Code          ######
###############################################
def get_unsorted_list(size,MaxN=1000,MinN=0):
    """
    Initialize code
    get random unsorted list of size specified with numbers between min
    number and max number specified
    """
    return [random.randint(MinN,MaxN) for i in xrange(size)]

def is_sorted_list(list_):
    """
    verifies if a list is sorted or not
    """
    prev = -1
    for item in list_:
        if item < prev:
            return False
        prev = item
    return True

def plot(values1, values2):
    """
    Function to plot log log 
    """
    plt.loglog(values1.keys(),values1.values(),'bs',basex=10,basey=10, label ='Code')
    plt.loglog(values2.keys(),values2.values(),'yo',basex=10,basey=10, label ='Python Builtin')
    plt.legend(loc=2)
    plt.title('MergeSort LogLog Plot')
    plt.xlabel('Input Size  (N)')
    plt.ylabel('Running Time (T)')
    plt.show()

def get_average(numbers):
    """
    Calculates the average of the items  of the list
    """
    return sum(numbers)/float(len(numbers))


###############################################
    ####  Test code                    ####
###############################################
a=[]
print a
a_s = arstar(a)
print a_s
print is_sorted_list(a_s)

b= [1]
print b
b_s = arstar(b)
print b_s
print is_sorted_list(b_s)

c= [1,2,3,4,5,6,7,89]
print c
c_s = arstar(c)
print c_s
print is_sorted_list(c_s)

d = [9,8,7,6,5,4,3,2,1]
print d
d_s = arstar(d)
print d_s
print is_sorted_list(d_s)

e = [1,1,1,2,2,3,4,4,4,4,5,6,9,8]
print e
e_s = arstar(e)
print e_s
print is_sorted_list(e_s)

g = [3,2,4,1]
print g
g_s = arstar(g)
print g_s
print is_sorted_list(g_s)
       
f = get_unsorted_list(10)
print f
f_s = arstar(f)
print f_s
print is_sorted_list(f_s)


##############################################
    ######  BenchMark            ######
##############################################


def benchmark(MaxN,TestN=100):
    """
    Benchmark and timing
    """
    size = 2
    values1 = {}
    values2 = {}
    file = open("codeTiming.csv", "w")   
    while size <= MaxN:
        
        #Dictionaries to hold average runnign times (code, Python Builtin)
        temp1 = []
        temp2 = []
        
        # Loop to create average sorting times
        for i in range(TestN):
        
            unsorted_list = get_unsorted_list(size) #Get a random list of numbers
            sorted_list_code = list(unsorted_list)  #Clone created list of numbers
            sorted_list_python = list(unsorted_list)
            
            
            #Sort Items code
            start = time.clock()
            arstar(sorted_list_code) #Sort Items
            elap = time.clock() - start
            temp1.append(elap)
            
            #Sort Items Python builtin
            start = time.clock()
            sorted_list_python.sort() #Sort Items
            elap = time.clock() - start
            temp2.append(elap)
         
        values1[size] = get_average(temp1)
        values2[size] = get_average(temp2)
        file.write(str(size)+","+str(values1[size])+","+str(values2[size])+"\n")
        print size, values1[size], values2[size]
        size *=2
    plot(values1, values2)
    file.close()

            
