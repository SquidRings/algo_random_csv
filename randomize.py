import pandas as pd
import random

dtypes = {f'groupe{i}': str for i in range(1, 28)}
df = pd.read_csv('data.csv', dtype=dtypes)

with open('logins2.txt', 'r') as f:
    logins = [line.strip() for line in f]
random.shuffle(logins)
print(logins)
for column in df:
    members = df[column].dropna()
    while len(members) < 3 and logins:
        login = logins.pop(0)
        if (df == login).any().any():
            continue
        df.loc[len(members), column] = login
        members = df[column].dropna()

df.to_csv('data_final.csv', index=False)