def quicksort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        piv = a_list[0]
        less = [i for i in a_list[1:] if i <= piv]
        greater = [i for i in a_list[1:] if i > piv]
        return quicksort(less) + [piv] + quicksort(greater)

print(quicksort([7, 9, 5, 4, 3, 2, 1]))