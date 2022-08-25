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