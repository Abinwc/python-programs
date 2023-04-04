"""Build-in datatypes
1. integers
2. floating
3. boolean
4. string
5. None

Data-structures:
1. List
2. Tuples
3. Sets
4. Arrays
5. Dictionaries
6. Que
7. Stack
"""
import array

x = 3
y = -3
z = 3.34
bool = True
boolNegative = False
str = 'Abi'
str2 = "Harish"


print(x)
print(bool)

list = [1, 3, 'Waseem']
list.append('Abin')
print(list)


tuples = (1, 2, 3)
print(tuples[0])


sets = {1, 2, 3}

dic = {
    1: 'Abin',
    2: 'Harish',
    3: 'Waseem'
}

dic2 = {
    'name': 'Waseem',
    'age': 21,
    'occupation': 'Developer'
}


list = [1, 2, 3, 4, 5]
arr = array.array('i', [1, 2, 4, 5, 5])


print("My array", arr)
