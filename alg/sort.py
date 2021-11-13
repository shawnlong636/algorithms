def test():
    print("test")

def mergesort(array: [int]) -> [int]:
    if len(array) == 1:
        return array
    i = int(len(array) / 2)
    left_array = mergesort(array[0:i])
    right_array = mergesort(array[i:])
    return merge(left_array, right_array)

def merge(left_array: [int], right_array: [int]) -> [int]:
    left_index = 0
    right_index = 0
    new_array = []
    
    # iterate through both arrays
    while (left_index < len(left_array) and right_index < len(right_array)):
        if (left_array[left_index] < right_array[right_index]):
            new_array.append(left_array[left_index])
            left_index += 1
        else:
            new_array.append(right_array[right_index])
            right_index += 1

    while (left_index < len(left_array)):
        new_array.append(left_array[left_index])
        left_index += 1
        
    while (right_index < len(right_array)):
        new_array.append(right_array[right_index])
        right_index += 1
        
    return new_array
    