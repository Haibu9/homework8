
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(12, 1.3)

values_list = ['hi', 5.6, False]
print_params(*values_list)

values_dict = {'a': 99, 'b': [11, 22, 33], 'c': 'exp'}
print_params(**values_dict)

values_list_2 = [(55, 'www'), 100]
print_params(*values_list_2, 42)