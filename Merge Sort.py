def MergeSort(listToSort):
    if len(listToSort) > 1:
        mid = len(listToSort) // 2
        left = listToSort[:mid]
        right = listToSort[mid:]

        MergeSort(left)
        MergeSort(right) 
        
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                listToSort[k] = left[i]
                i += 1
            else:
                listToSort[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            listToSort[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            listToSort[k] = right[j]
            j += 1
            k += 1
    return listToSort  

Data = [2, 4, 67, 34, 1, 78, 98, 3, 5, 6, 67777, 564, 234, 54]   
print(MergeSort(Data))   
    
    