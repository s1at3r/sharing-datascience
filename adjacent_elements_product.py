""" Create a function that will return the largest product of a pair of adjacent elements within a given Array."""

input_array = [3, 6, -2, -5, 7, 3]


def adjacent_element_product(input_array):
    final_array = []
    for i in range(len(input_array) - 1):
        final_array.append(input_array[i] * input_array[i + 1])
    result = max(final_array)

    print(result)


adjacent_element_product(input_array)
