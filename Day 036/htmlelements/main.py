import pandas

data = pandas.read_csv("Project-Estimation.csv")
df = pandas.DataFrame(data)
df['Description'] = df['Description'].str.replace(r'<[^<>]*>', '', regex=True)
df.to_csv("Updated.csv")

