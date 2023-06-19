def largetsAltitude(gain):
    """
     0 + -5 = -5
    -5 + 1 = -4
    -4 + 5 =  1
     1 + 0 =  1
     1 + - 7 = 6
    """
    ans = [0]
    for i in range(0,len(gain)):
        temp = ans[i] + gain[i]
        ans.append(temp)
    return max(ans) 
print(largetsAltitude([-5,1,5,0,-7]))
print(largetsAltitude([-4,-3,-2,-1,4,3,2]))