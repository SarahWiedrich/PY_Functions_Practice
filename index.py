def hello():
    print("Good day chap")

hello()

def pack(a, b, c):
    my_list=[a, b, c]
    print(my_list)

pack("Mon", "Tues", "Wed")

def eat_lunch(lunch):
    if lunch:
        for item in lunch:
            if item == lunch[0]:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")
    else:
        print("My lunchbox is empty")

my_lunch = ["PB&J", "baby carrots", "juice box"]
no_Lunch = []

eat_lunch(my_lunch)


# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for a in args:
        print(a)

arb_args("apple", 12, "Yum", 13)

#inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(int1, int2):
    def one():
        return int1+int2
    def two():
        return int1-int2
    print(one() + one())

inner_func(12, 24)

#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead. (if nothing is given as a lunch variable then the default as an argument to mystery meat)

def lunch_lady(name, lunch="Mystery Meat"):
    print(name + " " + lunch)

lunch_lady('Sarah')

#sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(int1, int2):
    print((int1 + int2), (int1 * int2))

sum_n_product(2, 4)


#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args

#arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*ints):
    total = 0
    for a in ints:
        total += a #(total = total + a)
    print(total/len(ints)) 

arb_mean(2,4,6)

#arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    longestString = ""
    maxlength = 0
    for arg in args:
        if len(arg) > maxlength:
            longestString = arg
            maxlength = len(arg)
    return longestString
