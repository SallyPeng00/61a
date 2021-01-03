def mutate_lst(lst, origin, dest):
     # First let's set the original location to 0
    counter = 0
    for i in lst:
        if counter == origin:
        	lst.pop(counter)
        	lst.insert(counter, 0)
        counter += 1
     # Now let's set the element at dest to 1
    counter = 0
    for i in lst:
        if counter == dest:
        	lst.pop(counter)
        	lst.insert(counter, 1)
        counter += 1
    
    return lst