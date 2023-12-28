a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
a = sorted(a_dictionary.keys())
for key in a:
    value = a_dictionary[key]
    print("{}: {}".format(key, value))
   
