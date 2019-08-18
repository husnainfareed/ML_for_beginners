

import pandas as pd 

Men = ['Smart', 'Handsome', 'Charming', 'Brilliant', 'Humble']

s = pd.Series(Men)
print('Seires:')
print(s)

print('\nvalues:')
print(s.values)

print('\nindex:')
print(s.index)

print('\ntype:')
print(s.dtype)
