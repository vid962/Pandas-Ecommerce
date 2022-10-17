import pandas as pd

df = pd.read_csv("Ecommerce Purchases")

print(df.info())

# ----------------------> average, minimum and maximum  purchase price
average_purchase = df['Purchase Price'].mean()
min_purchase = df['Purchase Price'].min()
max_purchase = df['Purchase Price'].max()

# ----------------------> people which have language settings in 'en'
english_on_web = df[df["Language"] == "en"]["Language"].count()

# ----------------------> lawyer positions
lawyers = df[df['Job'] == 'Lawyer']['Job'].count()

# ----------------------> time of purchase (pm or am)
am_pm_buyers = df['AM or PM'].value_counts()

# -----------------------> most common job titles
common_job = df['Job'].value_counts().head()

# -----------------------> checking single lot
lot = df.loc[df['Lot'] == '90 WT']['Purchase Price']

# -----------------------> American Express clients, purchasing for more than $95
AMEXclient_purchase = df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)]['Purchase Price'].count()

# -----------------------> Credit Cards with expiration date > 2025
CC_expire_in2022 = df[df['CC Exp Date'].apply(lambda exp: exp[3:] == "25")]['CC Exp Date'].count()





