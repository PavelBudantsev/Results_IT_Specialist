test_data_array = ["11", "Hello", "2", "World", ":-)"]
result_array = []
length = len(test_data_array)
n = 0
m = 0
while length > 0:
    if len(test_data_array[n]) <= 3:
        result_array.insert(m, test_data_array[n])
        m = m + 1
    n = n + 1
    length = length - 1
print(result_array)