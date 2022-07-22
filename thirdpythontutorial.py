import camelot as cm
#!ls
input_pdf = cm.read_pdf("India factsheet_economic_n_hdi.pdf", flavours = 'lattice', pages='1,2')
print(input_pdf)
for n in input_pdf:
 print(n)
print(input_pdf[2].df)
df = input_pdf[2].df.loc[11:14, 1:3]
print(df)
df.columns = ["KPI", "2001", "2011"]
df = df.reset_index(drop = True)
df.loc[:, ["2001", "2011"]] = df.loc[:,[ "2001", "2011"]].astype(float)
print(df)
df.to_csv("table_from_pdf.csv")
df.to_excel("table_from_pdf.xlsx")
import padnas as pd
df2 = pd.read_csv("packt_output.csv")
print(df2)
import seaborn as sns
df_melted = df.melt('KPI', var_names = 'year', value_name = 'percentage')
sns.barplot(x = 'KPI', y = 'percentage', hue = 'year', data= df_melted)
print(df_melted)
sns.barplot(x="KPI", y='percentage', hue="year", data = df_melted)

