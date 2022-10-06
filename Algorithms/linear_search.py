def linear_search (array,target) :
    for i in range(len(array)) :
        if array[i] ==  target :
            return i

if __name__ == '__main__' :
    array = [1, 231, 413452,5213,5,23,341,4,31]
    target = 413452
    print(linear_search(array,target))
