def binary_search (low , high , array , target) :
    mid =  low + ( high - low ) // 2
    if target == array[mid] :
        return mid
    if target > array[mid] :
        return binary_search (low + 1 , high , array , target)
    if target < array[mid] :
        return binary_search (low , high - 1 , array , target)


def binary(arr,low,high,target):
	mid=low+(high-low)//2
	if arr[mid]==target:
		print("ele found",mid)
		return target
	if arr[mid]<target:
		return binary(arr,low+1,high,target)
	if arr[mid]>target:
		return binary(arr,low,high-1,target)
	return False



if __name__ == '__main__' :
    array = [1,2,3,4,5,6,7,8,9]
    target = 8
    ans = binary(array , array[0],array[8],target)
    ans1 = binary_search(array[0] , array[8],array,target)
    print(ans)
    print(ans1)
