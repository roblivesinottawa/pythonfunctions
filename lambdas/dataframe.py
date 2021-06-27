import pandas as pd

df = pd.DataFrame({
    'Name': ['Luke', 'Gina', 'Sam', 'Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})

print(df)

df['age'] = df['Birthyear'].apply(lambda x: 2021 - x)

print(df) # adds the age column