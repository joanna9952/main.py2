# exercise 1
def count_integer(numbers, integer):
    count = 0
    for num in numbers:
        if num == integer:
            count += 1
    if count > 0:
        return print(count)
    else:
        return print(42)


numbers = list(map(int, input('Enter the numbers separated by space ').strip().split()))
integer = int(input('integer = '))
print('numbers = ', numbers)
print('integer = ', integer)

count_integer(numbers, integer)


# exercise 2

def list_func(numbers, integer):
    if integer not in numbers:
        return print([])
    else:
        index_of_integer = numbers.index(integer)
        numbers[index_of_integer] = 6
        numbers.reverse()
        print(numbers)
        numbers.reverse()
        return print(numbers)

numbers = list(map(int, input('Enter the numbers separated by space ').strip().split()))
integer = int(input('integer = '))
print('numbers = ', numbers)
print('integer = ', integer)

list_func(numbers, integer)


# exercise 3
def compare_lists(list1, list2):
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    if len(common) == 0:
        return print([])
    else:
        return print(common)


list1 = list(map(int, input('Enter the numbers separated by space ').strip().split()))
list2 = list(map(int, input('Enter the numbers separated by space ').strip().split()))
print('list1 = ', list1)
print('list2 = ', list2)

compare_lists(list1, list2)

#exercise 4
def remove_duplicates(lst):
    if len(lst) == 0:
        return print(lst)

    no_duplicates = list(set(lst))

    if len(no_duplicates) == len(lst):
        return print(lst)
    else:
        return print(no_duplicates)

lst = list(map(int, input('Enter the numbers separated by space ').strip().split()))
print('list = ', lst)

remove_duplicates(lst)

#exercise 5
def dict_func(dictionary):

    default_values = {"Type": "unknown type", "Brand": "unknown brand", "Price": "unknown price"}

    if not dictionary["Type"]:
        dictionary["Type"] = default_values["Type"]
    if not dictionary["Brand"]:
        dictionary["Brand"] = default_values["Brand"]
    if not dictionary["Price"]:
        dictionary["Price"] = default_values["Price"]

    my_type = dictionary.get("Type", default_values["Type"])
    my_brand = dictionary.get("Brand", default_values["Brand"])
    my_price = dictionary.get("Price", default_values["Price"])

    print(f'You have a {my_type} from {my_brand} that costs {my_price}.')
    dictionary['OS'] = 'Linux'
    return print(dictionary)

dictionary = {}
dictionary ['Type'] = input('Type:')
dictionary ['Brand'] = input('Brand:')
dictionary ['Price'] = input('Price:')

dict_func(dictionary)

