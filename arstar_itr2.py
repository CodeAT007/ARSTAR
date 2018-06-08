import random

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
    
    if len(RL) > 1:
        ## go through the list to break it into sorted slices
        prev = RL[0]
        DL = []
        i = 0
        for indx, item in enumerate(RL):
            print prev, i, indx, DL
            if item < prev:
                DL += [RL[i:indx]]
                i = indx
                
            prev = item
        print prev, i, indx, DL
        DL += [RL[i:]]

        ## merge the list into single sorted list

        while len(DL) > 1:
            
            print DL
            DL.insert(0,merge(DL.pop(),DL.pop()))  ## inefficient and need more work
            
        print DL[0]
        return DL[0]

    else:
        print RL
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
       



f = get_unsorted_list(10)
print f
f_s = arstar(f)
print f_s
print is_sorted_list(f_s)



            
