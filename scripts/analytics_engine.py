import pandas as pd

# ----------------------------
# LOAD AUTOMATED PARSED CSVs
# ----------------------------

df19 = pd.read_csv("extracted_data/vnrplacements2023.csv")
df20 = pd.read_csv("extracted_data/Placement-Statistics-for-Batch-(2020-24).csv")
df21 = pd.read_csv("extracted_data/Placement-Statistics-for-Batch-2025.csv")

# actual total institutional offers from brochures
actual_totals = {
    "2019-23": 1713,
    "2020-24": 1417,
    "2021-25": 2058
}

# ----------------------------
# ANALYTICS FUNCTION
# ----------------------------

def summarize(df, year, actual_total):

    highest_package = df["CTC_LPA"].max()
    average_ctc = round(df["CTC_LPA"].mean(), 2)

    premium_offers = df[df["CTC_LPA"] >= 10]["Offers"].sum()
    mass_offers = df[df["CTC_LPA"] < 5]["Offers"].sum()

    premium_ratio = round((premium_offers / actual_total) * 100, 2)
    mass_ratio = round((mass_offers / actual_total) * 100, 2)

    return {
        "Year": year,
        "Highest_Package": highest_package,
        "Average_CTC": average_ctc,
        "Premium_Offers_10L+": premium_offers,
        "Mass_Offers_Below5L": mass_offers,
        "Premium_Ratio_%": premium_ratio,
        "Mass_Ratio_%": mass_ratio,
        "Total_Offers": actual_total
    }

summary = [
    summarize(df19, "2019-23", actual_totals["2019-23"]),
    summarize(df20, "2020-24", actual_totals["2020-24"]),
    summarize(df21, "2021-25", actual_totals["2021-25"])
]

summary_df = pd.DataFrame(summary)

summary_df.to_csv("extracted_data/yearly_summary.csv", index=False)

print(summary_df)
print("Automated yearly analytics generated successfully.")