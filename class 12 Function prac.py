# functions practice
def song():
    return "happy birthday song"
print(song)    


def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(9))            





def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_even(10))            


def last_char(name):
    return name[-1]
print(last_char("Prateek agarwal"))
