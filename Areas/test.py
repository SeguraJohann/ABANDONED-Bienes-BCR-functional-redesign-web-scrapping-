import pandas as pd
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 28, 30, 35]}
df = pd.DataFrame(data)
print(df)

print(df.index.get_loc())