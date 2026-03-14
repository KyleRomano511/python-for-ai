import pandas as pd
from helpers import calculate_total, format_currency

# read data
df = pd.read_csv("data/sales.csv")


# calculate all row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row["quantity"], row["price"])
    totals.append(total)

# add total to df
df["total"] = totals

#########

print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row["total"])
    print(f"{row['product']}: {formatted_total}")

# Total sales
grand_total = sum(totals)
formatted_grand_total = format_currency(grand_total)
print(f"\nTotal Sales: {formatted_grand_total}")
