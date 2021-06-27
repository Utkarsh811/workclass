list=[]
n=int(input('Enter the no of elements-:'))
for i in range(n):
    list.append(int(input(f'Enter the element {i}-:')))
print(list)
even_list=[]
odd_list=[]
for i in range(n):
    if(list[i]%2==0):
        even_list.append(list[i])
    else:
         odd_list.append(list[i])
print(even_list)
print(odd_list)         

