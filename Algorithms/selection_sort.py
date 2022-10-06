def selection_sort (array , size) :
    for step in range (size) :
        min = step
        for i in range (step + 1 , size) :
            if array [i] < array [min] :
                array [i] , array [min] = array [min] , array [i]
    return array

if __name__ == '__main__' :
    array = [1,0,23,13,7,88,9,5]
    size = len(array)
    ans = selection_sort (array , size)
    print(ans)
