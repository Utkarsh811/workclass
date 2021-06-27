list=[]
n=int(input('Enter the elements-:'))
for i in range(n):
    list.append(int(input(f'Enter the elements {i}-:')))
max=list[0]
max2=list[0]
for i in range(n):
    if(list[i]>max):
        max=list[i]
#print(max)
for i in range(n):
    if(list[i]>max2 and list[i]<max):
        max2=list[i]
print('The 2nd largest number is -:',max2)        