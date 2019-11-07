# UPPGIFT 1
# def sum2(c,s):
# return c + s

# UPPGIFT 2
#def create_greeting(name):
    #return 'Hejsan '+ name
#print(create_greeting('Linnea'))

# UPPGIFT 3
#def mean2(s,m):
   # return (s + m) / 2
# print(mean2(2,68))

# UPPGIFT 4
def sumlist(my_list):
    result = 0
    for my in my_list:
        result = result + my
    return result

tbbatb = [2,7,5,68] 
print(sumlist(tbbatb))

# UPPGIFT 5
def mean_list(my_list):
    sumlist(my_list)/len(tbbatb)
    