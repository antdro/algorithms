# Algorithm's complexity is O(k)

def count(_list, _max):
    '''
    Count frequency of elements in array

    params:
        _list: array to sort
        _max: the largest value in array

    return:
        _dict: dictionary with frequency
    '''
    
    _dict = {key: 0 for key in range(_max + 1)}
    for item in _list:
        _dict[item] += 1

    return _dict
    

def search(_dict, index):
    '''
    Find ith item in sorted array
    
    params:
    _dict: dictionary where to search for item
    index: position in array
    
    return:
    item: item in index'th position
    '''    
    _sum = 0
    for item in _dict:
        _sum += _dict[item]
        if _sum >= index:
            return item
