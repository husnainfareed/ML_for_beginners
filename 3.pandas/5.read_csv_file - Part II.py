

import pandas as pd 

google = pd.read_csv('csv/google_stock_price.csv', squeeze=True)
# print(google)

print('\nWill print number of rows')
google.count()

print('\nWill print number of rows')
print(len(google))

print(f'Sum: {google.sum()}')
print(f'Mean: {google.mean()}')
print(f'Standard Deviation: {google.std()}')
print(f'Min Value: {google.min()}')
print(f'Max Value: {google.max()}')
print(f'Min Value ID: {google.idxmin()}')
print(f'Max Value ID: {google.idxmax()}')


