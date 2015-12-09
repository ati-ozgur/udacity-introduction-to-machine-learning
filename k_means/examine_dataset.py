import pandas as pd
df = pd.DataFrame.from_dict(data_dict,orient='index')

feature_list = ['bonus', 'salary','exercised_stock_options','total_payments']

df[feature_list] = df[feature_list].astype(float)

df["exercised_stock_options"].max()
df["exercised_stock_options"].min()

df["salary"].max()
df["salary"].min()

