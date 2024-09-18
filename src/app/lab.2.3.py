a1 = {'simple_key': 'hello'}
a2 = {'k1': {'k2': 'hello'}}
a3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(a1['simple_key'])  
print(a2['k1']['k2'])  
print(a3['k1'][0]['nest_key'][1][0])  