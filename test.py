import pandas as pd

data = pd.read_csv('users.csv', header=0)
print(data)
data_dict = data.set_index('users')['passwords'].to_dict()
print(data_dict)
