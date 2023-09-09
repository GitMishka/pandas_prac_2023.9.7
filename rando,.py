import pandas as pd
data = pd.read_csv('file.csv')
data.to_csv('output.csv', index=False)
