my_list=['ego','hulk','kulh','garbage','feather']
my_list1=['fgo','job','bug','braise','list','hamper','green']
my_list2=[]
for i in range(len(my_list)):
    my_list2.append(my_list[i])
for j in range(len(my_list1)):
    my_list2.insert(len(my_list)+j,my_list1[j])
print(my_list2)    
#output
'''
['ego', 'hulk', 'kulh', 'garbage', 'feather', 'fgo', 'job', 'bug', 'braise', 'list', 'hamper', 'green']
'''
#another way
print(my_list+my_list1)