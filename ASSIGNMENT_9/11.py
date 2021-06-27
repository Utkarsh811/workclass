
import time
start = time.time()
l1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print(f"Original list : \n{l1}")
for i in l1:
    if i == 0:
     l1.remove(i) #o(n)
     l1.append(i)#o(1)

end=time.time()

print(l1)
print(end-start)


'''
import time
my_list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
start=time.time()
count=0
for i in range(27):
    if(my_list[i]!=0):
        my_list[count]=my_list[i]
        count=count+1
        time.sleep(1)

while(count<27):
    my_list[count]=0
    count=count+1
print(my_list)    
end=time.time()  

print(end-start)     

'''
