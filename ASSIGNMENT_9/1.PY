my_list=[]
n=int(input('Enter the number of elements'))
for i in range(n):
    my_list.append(int(input(f'enter the elements {i}-:')))
print(my_list)  
key=int(input('Enter the key-:'))  
count=0
print('3 is found at indices-:',end='')
for i in range(n):
    if(my_list[i]==key):
        count=count+1
        print(f'{i},',end='')
print('\n')        
print(' The count for the key is',count)        #count the occurence