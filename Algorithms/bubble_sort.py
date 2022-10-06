def bubble_sort (array) :
    for i in range(len(array)) :
        for j in range(i + 1 , len(array)) :
            if array [j] < array [i] :
                array [i] ,array [j] =array [j] ,array [i]
    return array







if __name__ == '__main__' :
    array = [1 , 5, 0 ,113 ,141,3425246, 326  ,1341 ,352]
    print(bubble_sort (array))
