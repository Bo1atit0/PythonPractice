def best_score(a_dictionary):

    max_keys = max(a_dictionary, key= lambda key:a_dictionary[key])
    print(max_keys)


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)



