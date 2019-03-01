# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    for end_cursor in range(len(data) - 1, 0, -1):
        for idx in range(end_cursor):
            if descending and (data[idx][index] < data[idx + 1][index]):
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
            elif not descending and (data[idx][index] > data[idx + 1][index]):
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
    return data


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    for cursor in range(1, len(data)):
        current = data[cursor]
        position = cursor

        if descending:
            while position > 0 and data[position - 1][index] < current[index]:
                data[position] = data[position - 1]
                position -= 1
        else:
            while position > 0 and data[position - 1][index] > current[index]:
                data[position] = data[position - 1]
                position -= 1

        data[position] = current
    return data


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    for cursor in range(len(data) - 1, 0, -1):
        target_index = 0

        if descending:
            for position in range(1, cursor + 1):
                if data[position][index] < data[target_index][index]:
                    target_index = position

        else:
            for position in range(1, cursor + 1):
                if data[position][index] > data[target_index][index]:
                    target_index = position

        data[cursor], data[target_index] = data[target_index], data[cursor]
    return data


def quick_sort(data, index, descending=False):
    '''Sorts using the quick sort algorithm'''
    def recurse(lst, first, last):
        if first < last:
            split_index = split(lst, first, last)

            # sort each split section again
            recurse(lst, first, split_index - 1)
            recurse(lst, split_index + 1, last)

    def split(lst, first, last):
        # TODO update this pivot to the median of 3 strategy
        pivot = lst[first][index]

        left_cursor = first + 1
        right_cursor = last 

        srted = False
        while not srted:
            while left_cursor <= right_cursor and lst[left_cursor][index] <= pivot:
                left_cursor += 1

            while right_cursor >= left_cursor and lst[right_cursor][index] >= pivot:
                right_cursor -= 1

            if right_cursor < left_cursor:
                # finished sorting the current split list
                srted = True
            else:
                # swap the values in the list
                lst[left_cursor][index], lst[right_cursor][index] = lst[right_cursor][index], lst[left_cursor][index]
                
        lst[first][index], lst[right_cursor][index] = lst[right_cursor][index], lst[first][index] 
        # this could work with the left_cursor too
        return right_cursor

    recurse(data, 0, len(data) - 1)
    return data


def python_sort(data, index, descending=False):
    '''Sorts using the native Python sort algorithm (Timsort)'''
    # LEAVE this function as is - it will allow you to see your sorts against the python one
    data.sort(key=lambda t: t[index], reverse=descending)
