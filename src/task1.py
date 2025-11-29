import pandas as pd
import glob

files = glob.glob("D:/Dash/quantium-starter-repo/data/*.csv")
print("Files found:", files)   # DEBUG

df_list = [pd.read_csv(file) for file in files]

df = pd.concat(df_list, ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["Sales"] = df["quantity"] * df["price"]

final_df = df[["Sales", "date", "region"]]

final_df.to_csv("D:/Dash/quantium-starter-repo/output.csv", index=False)

print("✔️ Done! Output saved")
