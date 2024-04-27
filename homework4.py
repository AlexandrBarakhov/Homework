immutable_var = (1, 2.5, "apple", True)
print(immutable_var)
immutable_var[0] = 5
immutable_var.append("???")
immutable_var.remove("apple")
# Кортеж является неизменяемой упорядоченной коллекцией.
# В кортеже нельзя заменить значение элемента, добавить или удалить элемент.

mutable_list = [2, 3.5, "orange", False]
mutable_list[0] = 'Yes'
mutable_list.append("!!!")
mutable_list.remove(False)
print(mutable_list)
