import pandas as pd

df = pd.DataFrame({
    'Name': ['Luke', 'Gina', 'Sam', 'Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})

print(df)

df['age'] = df['Birthyear'].apply(lambda x: 2021 - x)

print(df) # adds the age column

print(list(filter(lambda x: x > 18, df['age']))) # [45, 37]

df['double_age'] = df['age'].map(lambda x : x * 2) 
print(df)


df['Gender'] = df['Status'].map(lambda x: 'Male' if x == 'Father' or x == 'Son' else 'Female')
print(df)

df[['Name', 'Status']] = df.apply(lambda x: x[['Name', 'Status']].str.upper(), axis=1)
print(df)