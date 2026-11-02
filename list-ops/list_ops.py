def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat_list = []
    for lst in lists:
        flat_list += lst
    return flat_list
    
def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]