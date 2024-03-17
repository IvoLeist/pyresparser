# %%
import pandas as pd
import json

# %%
json_file_path = '../resumes/frontend/summary/frontend_resumes_extracted.json'
csv_file_path = '../resumes/frontend/summary/frontend_resumes_extracted.csv'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


# %%
df = pd.DataFrame(data)
# %%
# remove lists and convert to strings separated by semicolons
for col in df.columns:
    df[col] = df[col].apply(lambda x: '; '.join(x) if isinstance(x, list) else x)
# %%
df.to_csv(csv_file_path, index=False, sep=",", escapechar="\\")
# %%
print(f"Data has been written to {csv_file_path}")