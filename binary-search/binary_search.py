def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (high + low) // 2
        if value == search_list[mid]:
            return mid
        if value < search_list[mid]:
            high = mid -1
        if value > search_list[mid]:
            low = mid +1
        
    raise ValueError("value not in array")