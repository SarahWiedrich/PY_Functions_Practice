#return max number
def max_num(*num):
    x = max(*num)
    print(x)

max_num(3, 6, 7, 12, 22)

#multiply all the numbers in a list
def mult_list(my_list):
    result = 1
    for num in my_list:
        result = result * num
    return result

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]

print(mult_list(list1))
print(mult_list(list2))
    

#reverse a string
def rev_string(text):
    reverse = text [::-1]
    print(reverse)

rev_string("Hello")

#check if a number falls in a given range
def num_within(num):
    if num in my_range :
        print("in range")
    else:
        print("not in range")

my_range = range(2, 3, 4)
num_within(2)

#pascals triangle 
def pascal(n):
    row = [1]
    start = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [l + r for l, r in zip(row + start, start + row)]
    return n>=1

pascal(1)
pascal(5)