
import pandas as pd 

# print(' squeeze used to convert into series') 
# print(' usecol used to get specific col')
# pokemon = pd.read_csv('csv/pokemon.csv', squeeze=True, usecols=['Pokemon'])

# print(' by default, shows first five value ')
# print(pokemon.head())

# print('\nTo print first seven')
# print(pokemon.head(7))

# print('\nTo print last 5 values')
# print(pokemon.tail())

# print('\nTo print values')
# print(pokemon.values)

# print('\nTo print index')
# print(pokemon.index)

# print('\nTo print object type')
# print(pokemon.dtype)

# print('\nTo print True if no repeition, else false')
# print(pokemon.is_unique)

# print('\nTo print dimension 1, since series is 1 here')
# print(pokemon.ndim)

# print('\nTo print (721,0) i.e. 721 rows, 0 cols')
# print(pokemon.shape)

# print(pokemon.name)
# print('\nwill print col name')

# print('\nwill print first 7 values in sorted form')
# print(pokemon.sort_values().head(7))

# print('\nwill print first 7 values in sorted form in descending order')
# print(pokemon.sort_values(ascending=False).tail(7))

# print('\nwill print data at position 10')
# print(pokemon[10])

# print('\nwill print data at position 100, 510, 600')
# print(pokemon[[100,510,600]])

# print('\nwill print data from 50 to 500')
# print(pokemon[50:511])

# print('\nwill print data from 0 to 50')
# print(pokemon[:51])

# print('\nwill print data of last 20')
# print(pokemon[-30:-10])


# pokemon = pd.read_csv('csv/pokemon.csv', index_col='Pokemon', squeeze=True)
# print(pokemon.head())

# print('\n Will print Electric for Pikachu type and Nan for Digimon, since we have no any Digimon. Nan mean not a number')
# print(pokemon[['Pikachu', 'Digimon']])

# print(pokemon.sort_index().head(7))

# print(pokemon.get('Moltres'))
# print(pokemon.get(['Moltres', 'Meowth']))

# print(pokemon.get(key = 'Digimon', default='This is not a pokemon'))

# will print quantity of each value
# print(pokemon.value_counts())




