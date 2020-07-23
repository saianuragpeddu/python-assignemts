import pandas as pd

csvPath = "dimensions.csv"
parquetFilename = "load_dimensions"

df = pd.read_csv(csvPath)
df.loc[df['name'] == 'material', 'name'] = 'product'

new_row = {'id':'11', 'dimension_id':3, 'name':'week, 'description':'Week', 'valid_from':'', 'valid_to':'', 'created_at':''}

df_marks = df_marks.append(new_row, ignore_index=True)
df.loc[df['id'] != None, ['valid_from','created_at']] = datetimevalue 

now = pd.to_datetime("now")

df["valid_from"] = df["valid_from"].map(lambda ts: now.strftime("%d-%m-%Y &H.%M.%S"))
df["created_at"] = df["created_at"].map(lambda ts: now.strftime("%d-%m-%Y &H.%M.%S"))

print('\n\nNew row added to DataFrame\n--------------------------')
print(df_marks)

df.to_parquet(parquetFilename)
