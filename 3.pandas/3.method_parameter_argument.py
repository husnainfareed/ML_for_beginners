

import pandas as pd

print('Example 1')
Rate = [4.87, 87.5, 23.8, 98.0, 87.6, 9.0]
r = pd.Series(Rate)

print(f'sum: {r.sum()}')
print(f'product: {r.product()}')
print(f'mean: {r.mean()}')
print('\n')

print('Example 2')
fruits = ['Apple', 'Mango', 'Banana', 'Chickoo', 'Guava', 'Watermelon', 'Orange']
days = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

print(pd.Series(index=days, data=fruits))
