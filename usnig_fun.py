def contain_even(l):
    for ele in l:
        if ele %2==0:
            print("Even number found")
            break
    else:
            print("No even number found") 
print("For list1:  ")
contain_even([1,6,5,7,9]) 
print("For list2:") 
contain_even([1,3,5,7,9])             