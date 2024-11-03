import pandas as pd

data = pd.read_csv('data.csv', header=None)

rows = []

for index, row in data.iterrows():
    word, variations = row[0].split(": ")
    variations_list = variations.split()
    for variation in variations_list:
        rows.append({'Misspelling': variation, 'RealWord': word })

df = pd.DataFrame(rows)

csv_file = 'words.csv'

df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'CSV file "{csv_file}" has been created successfully.')
