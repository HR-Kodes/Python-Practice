def inertion_sort (array) :
    for step in range (1 , len(array)) :
        key = array [step]
        j = step - 1

        while j >= 0 and key < array [j] :
            array [j + 1] = array [j]
            j = j - 1

        array [j + 1] = key
    return array


if __name__ == '__main__' :
    array = [12 , 34 , 3, 12 , 1 , 0 , 5 , 45 , 38, 21 , 44, 9 , 4]
    ans = inertion_sort (array)
    print(ans)
