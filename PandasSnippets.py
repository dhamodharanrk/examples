import pandas as pd
df = pd.read_table("./DataSource/PandasSnippets_InputsApr2019.tsv")
# df = pd.read_csv("demo.csv")
print(df)
df.Pressure = df.Pressure * 10
df.to_csv("./outputs/PandasSnippets_InputsApr2019.csv",index=False)
print(df)

