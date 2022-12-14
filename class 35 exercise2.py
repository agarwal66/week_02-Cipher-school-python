def reverse_list(l):
    r_list = []
    for i in range(1, len(l)+1):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list    
    #return l[::-1]
    #return l
#numbers = [1,3,5,6,7,]
#popped_item = numbers.pop()

#print(reverse_list(numbers))    