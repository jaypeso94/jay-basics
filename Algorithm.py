list_1 = ['b', 'd', 'c', 'a']
#          0    1    2    3 

# d > c -> (c,d)

# d > a -> (a,d)

# c > a -> (a,c)

# b > a -> (a,b) 

InputVal = input('Pass 1, letter "b"')
for i in range(0,len(list_1)-1):
    if InputVal == list_1[i]:
        InputVal = i 
        
       
        if list_1[InputVal] > list_1[3]:
            temp = list_1[3]
            list_1[3] = list_1[InputVal]
            list_1[InputVal] = temp 
            print(temp)



