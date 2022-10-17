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

# df = pd.read_csv("Salaries.csv")
# #print(df.head(5))
#
# print(df.columns.tolist())
#
# # avarage pay from the data, base salary
# avarage_base_pay = df["BasePay"].mean()
#
# # employee with the highest overtime
# highest_overtime = df['OvertimePay'].max()
#
# # accessing to single person salary
# joseph_salary = df[df['EmployeeName'] == 'JOSEPH DRISCOLL' ]['TotalPayBenefits']
#
# # highest salary and persons name
# highest_salary_total = df["TotalPay"].max()
# person = df[df['TotalPayBenefits'] == highest_salary_total ]['EmployeeName']
#
# # highest salary and persons name / faster way
# person_2 = df.loc[df['TotalPayBenefits'].idxmax()]
#
# # lovest paid person
# lowest_person = df.loc[df['TotalPayBenefits'].idxmin()]
#
# # avarage base pay of all employees per year (2011-2014)
# avarage_base_year = df.groupby('Year').mean()['BasePay']
#
# # unique joy titles
# unique_job_titles = df['JobTitle'].nunique()
#
# # Top 10 most common job titles
# most_common_jobs = df['JobTitle'].value_counts().head(10)
#
# # number of people with 'Chief' in job title
# def if_chief(title):
#     if "chief" in title.lower().split():
#         return True
#     else:
#         return False
#
# job_title_chief = sum(df["JobTitle"].apply(lambda x: if_chief(x)))






