import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com','JohnDoe@email.com']
}

df = pd.DataFrame(people)
print(df)
print()

# Filters basically create a True/False map of the dataframe. This map can then be applied to the same,
# Dataframe to filter out unwanted data in the dataset.
filt = (df['last'] == 'Doe') # create a filter

print(df[filt]) # filter using this syntax


# can also be done using .loc[]

print(df.loc[filt])
print(df.loc[filt, 'email']) # first val --> rows we want, second val --> columns we want.

filt2 = (df['last'] == 'Doe') & (df['first'] == 'John')
filt3 = (df['last'] == 'Schafer') | (df['first'] == 'John')
filt4 = ~filt3
print()
print(df.loc[filt2])
print()
print(df.loc[filt3])
print()
print(df.loc[filt4])


# from the same tutorial but a different dataset.
countries = ['United States', 'India', 'United Kingdom', 'Pakistan']
filt5 = df['Country'].isin(countries)
df.loc[filt5, 'Country'] # will filter results and return rows whose countries are in the list.

filt6 = df['LanguagesWorkedWith'].str.contains('Python', na=False)
#           Column                  string filtering        Handling NaN values.
df.loc[filt6, 'LanguagesWorkedWith']


