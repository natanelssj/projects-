# ********** Q1 **********
def q1():
    # your code
    def koltz(parameter):
        parameter=int(parameter)
        counter=1
        print(parameter,end="->")
# Perform the Collatz sequence until parameter becomes 1
        while (parameter > 1):
            if (parameter %2==0):
                parameter = parameter//2
                print(parameter,end="->")
                if(parameter==1):print('done')
                counter+=1
            else:
# If the parameter is odd, multiply it by 3 and add 1
                parameter=(parameter*3)+1
                print(parameter,end="->")
                counter+=1

    result =int (input ('enter a  number: ')) 
    koltz(result)
    
    pass
     


"""
Helper functions for question 1 will be written here.
"""


# ********** Q2 **********
def q2():
    # your code
    mat = matrix()
# Counter to keep track of the rotation step
    counter = 0
# Perform rotation and swapping operations on the matrix
    for i in range(0, 12, 2):
     for j in range(0, 12, 2):
        if (counter) % 2 == 0:
            rotate_clockwise(mat, i, j)
            counter+=1
        else:
            rotate_counter_clock(mat, i, j)
            counter+=1
        # Swap elements in the submatrices

    for index_i in range(2,12,4):
        for index_j in range(2,12,4):
            swap(mat,index_i-2,index_j-2,index_i,index_j)
            swap(mat,index_i-2,index_j,index_i,index_j-2)
    print_matrix (mat)
    sum_of_cols(mat,8)
    search_num(mat,89)
    big_divider(mat,7,7)
    pass

    


"""
Helper functions for question 2 will be written here.
"""
def matrix():
           mat = []
           rows = 12
           cols = 12
           val = 1

           for i in range(rows):
               row = []
               for j in range(cols):
                   row.append(val)
                   val += 1
               mat.append(row)
           return mat


def swap(mat, row_1, col_1, row_2, col_2):
    for i in range(2):
        for j in range(2):
            temp = mat[row_1 + i][col_1 + j]
            mat[row_1 + i][col_1 + j] = mat[row_2 + i][col_2 + j]
            mat[row_2 + i][col_2 + j] = temp


def rotate_clockwise(matrix,start_row,start_col):
    temp = matrix[start_row][start_col]
    matrix[start_row][start_col]=matrix[start_row+1][start_col]    
    matrix[start_row+1][start_col]=matrix[start_row+1][start_col+1]    
    matrix[start_row+1][start_col+1]=matrix[start_row][start_col+1]
    matrix[start_row][start_col+1]=temp


def rotate_counter_clock(matrix, start_row, start_col):
    temp = matrix[start_row][start_col]
    matrix[start_row][start_col] = matrix[start_row][start_col+1]
    matrix[start_row][start_col+1] = matrix[start_row+1][start_col+1]
    matrix[start_row+1][start_col+1] = matrix[start_row+1][start_col]
    matrix[start_row+1][start_col] = temp


def print_matrix(mat):
    for index in mat:
        print(index)


def search_num(searching,number):
    counter=0
    for i in range (len(searching)): 
        for j in range(len(searching[i])):
            if searching[i][j]==number :
                print('Q2B=', i)
                counter += 1

    if counter==0:
        print('the number',number ,'not found')


def sum_of_cols(mat,col):
    sum=0

    for i in range(len(mat)):
        sum+=mat[i][col]
    
        
    print ('Q2A=',sum )
                
def big_divider(mat,row, div):
    number=0
    max=0
    for i in range (len(mat[div])):
        if mat[div][i]%7==0 and mat[div][i]>max:
            max=mat[div][i]
    print('Q2C= ',max)

# ********** Q3 **********
"""
The class for question 3 will be written here.
"""
class product:
    def __init__(self, name , price ,discount):
        self._name=name 
        self._price=price
        self._discount=discount
        

    def get_name(self):
         return self._name

    def set_name(self,name):
        self._name=name

    def get_price(self):
        return self._price
    def set_price(self,price):
        self._price=price 
    def has_discount(self,discount):
        return self._discount
    def set_discount(self,discount):
        self._discount=discount



# ********** Q4 **********
def q4():
    # your code
    tomer_picture_list = [
        ['Mona Lisa', 5341, 67],
        ['Starry night', 8908, 27],
        ['A girl with a pearl earring', 5914, 13],
        ['This Kiss', 3922, 20],
        ['Las Meninas', 5046, 61],
        ['birth of venus', 5576, 44],
        ['Guernica', 5627, 43],
        ['Arrangement in gray and black', 6680, 46],
        ['the night watch', 4361, 75],
        ['The Last Supper', 4907, 13],
        ['Sunrise impression', 3580, 68],
        ['Freedom leads the people', 5657, 20],
        ['The gypsy woman', 3862, 60],
        ['The sailors\' feast', 5332, 27],
        ['Night hawks', 4420, 44],
        ['The jellyfish raft', 7026, 71],
        ['the swing', 9594, 73],
        ['June flames', 9340, 69],
        ['son of man', 9847, 38],
        ['A storm in the Sea of Galilee', 7555, 56]
    ]
    count=0
    num_of_people=0
    rec(tomer_picture_list, 80000,count,num_of_people)

def rec(lst, price,counter,num_people ):
    index = 0
    name = lst[0][0]
    min_price = lst[0][1]
    max_people = lst[0][2]
    # Iterate through the list to find the painting with the maximum number of people
    for i, item in enumerate(lst[1:]):
        if  item[2] > max_people  :
            index = i + 1
            min_price = item[1]
            max_people = item[2]
            name = item[0]
    # Check if the price is greater than or equal to the minimum price of the painting
    if price >= min_price:
        del lst[index]
        counter+=1
        num_people+=max_people
        rec(lst, price - min_price,counter,num_people)

    else: 
        print('Q4A:',counter)
        print('Q4B:',num_people)
        print('Q4C:',price)

q1()
q2()
q4()

