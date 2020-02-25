
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    x = array
 #  if x ==[]:
 #       answer = 0
    answer = 0
    if x == []:
        answer = 0
    else:  
        for i in range(len(x)): 
        #  print(i)
        #  answer = sum(x[2*i])*x[-1]
            if i %2 == 0:
                answer = answer + x[i] 
            else :
                answer = answer
    # if x == []:
    #     x.append(0)
        answer = answer * x[-1]
    return answer
print(checkio([]))