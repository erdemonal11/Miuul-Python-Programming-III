# CASE STUDY III:

import pandas as pd

# Task I:

# question I:

df = pd.read_excel("dataset/miuul_gezinomi.xlsx")
print(df.head(), df.info())

# question II:

print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# question III:

df["ConceptName"].nunique()

# question IV:
df["ConceptName"].value_counts()

# question V:

df.groupby("SaleCityName").agg({"Price": "sum"})

# question VI:

df.groupby("ConceptName").agg({"Price": "sum"})

# question VII:

df.groupby(by=["SaleCityName"]).agg({"Price": "sum"})

# question VIII:

df.groupby(by=["ConceptName"]).agg({"Price": "sum"})

# question IX:

df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "sum"})

# Task II:

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["BookingType"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)

# Task III:


df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score" ]).agg({"Price": ["mean", "count"]})

df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# Task IV:

agg = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price",
                                                                                                ascending=False)
agg.head()

# Task V:

agg.reset_index(inplace=True)
agg.head()

# Task VI:

agg['sales_level_based'] = agg[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

# Task VII:

agg["SEGMENT"] = pd.qcut(agg["Price"], 4, labels=["D", "C", "B", "A"])
agg.head()
agg.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Task VIII:

agg.sort_values(by="Price")

new = "ANTALYA_HERŞEY DAHIL_HIGH"
agg[agg_df["sales_level_based"] == new]
