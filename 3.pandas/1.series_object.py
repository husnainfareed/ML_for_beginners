

import pandas as pd 

print('\nExample 1')
flavor = ['Chocolate', 'Mango', 'Vanilla', 'Strawberry', 'Banana']
print(pd.Series(flavor))

print('\nExample 2')
lottery = [34,66,89,22,90,12,5]
print(pd.Series(lottery))

print('\nExample 3')
reg = [True, False, True, True, True]
print(pd.Series(reg))
