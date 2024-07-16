import sys

counter = 0
arg_list=[]
for i in sys.argv:
    counter+=1
    arg_list.append(sys.argv)

print(f"number of arguments is {counter}\narguments list : {arg_list[0]}")
