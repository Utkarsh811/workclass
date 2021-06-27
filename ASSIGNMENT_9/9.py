#for matrix addition matrix should have equal dimensions , means equal number of rows and columns
row=int(input('Enter the number of rows of matrix-1'))
cols=int(input('Enter the number of cols of matrix-1'))
row1=int(input('Enter the number of rows of matrix-2'))
cols1=int(input('Enter the number of columns of matrix-2'))
if(row==row1 and cols==cols1):
    matrix_1=[]
    matrix_2=[]
    matrix_3=[]
    
    for i in range(row):
        a=[]

        for j in range(cols):
            a.append(int(input(f'Enter the element [{i},{j}]-')))
        matrix_1.append(a)
    print(matrix_1)        
        


    for i in range(row):
        for j in range(cols):
            print(matrix_1[i][j],end=' ')
        print('\n')  


        #creating matrix -2

    for i in range(row1):
        a=[]

        for j in range(cols1):
            a.append(int(input(f'Enter the element [{i},{j}]-')))
        matrix_2.append(a)
    print(matrix_2)        
        


    for i in range(row1):
        for j in range(cols1):
            print(matrix_2[i][j],end=' ')
        print('\n')  


        #adding

    for i in range(row1):
        a=[]
        for j in range(cols1):
            a.append(matrix_1[i][j]+matrix_2[i][j])
        matrix_3.append(a)
    print(matrix_3)    

    for i in range(row1):
        for j in range(cols1):
            print(matrix_3[i][j],end=' ')
        print('\n')  
    




      



   
