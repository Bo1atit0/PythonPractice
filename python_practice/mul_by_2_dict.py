def multiply_by_2(a_dictionary):
    result = {}
    for key, value in a_dictionary.items():
        result[key] = value * 2
    return result
  




a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(a_dictionary)
print(new_dict)