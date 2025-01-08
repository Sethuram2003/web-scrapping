import pandas as pd
import numpy as np

df_= pd.read_csv("cypherhunter_products.csv")
df_price = pd.read_csv("output.csv")

df_price = df_price.dropna()

print(df_price.info())

columns_to_convert = ['Market Cap', 'Fully Diluted Valuation', '24 Hour Trading Vol', 
                      'Circulating Supply', 'Total Supply', 'Max Supply']

# Remove non-numeric characters and convert to integer
for col in columns_to_convert:
    df_price[col] = pd.to_numeric(df_price[col].replace({'\$': '', ',': '', '∞': np.nan}, regex=True), errors='coerce').fillna(0).astype(int)
# Check the result
print(df_price.dtypes)  # should show 'int64' for converted columns
print(df_price)





