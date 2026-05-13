'''
List deduplicator:
Write a function that takes a list which may have duplicates and returns a new list with duplicates removed, but in the same original order. (Don't just convert to a set — that loses order.)
'''

def duplicateRemover(lst):
    new_lst = []

    for item in lst:
        if item not in new_lst:
            new_lst.append(item)

    return new_lst

n = int(input("Enter the number of elements in the list: "))

if n == 1:
    print("This is for checking duplicates in a list, it requires you to have more than 1 element")
elif n == 0:
    print("This is for checking duplicates in a list, it requires you to have more than 0 elements")
elif n < 0:
    print(f"You use your big brain and tell me how a list can have {n} elements! (╯°□°)╯︵ ┻━┻")
else:
    lst = []   
    for i in range(n):
        item = input(f"Enter element{i+1}: ")    
        lst.append(item)

    print("Original List:", lst)
    print("List after removing duplicates:", duplicateRemover(lst))