import pandas as pd


with open('mena-countries.txt', 'r') as f:
    country_names = [line.strip() for line in f.readline().split(',')]

country_names.append('Türkiye')
country_names.append('Pakistan')
country_names.append('Iraq')

hdi_data = pd.read_csv('HDI.csv')

gnipc_columns = hdi_data.columns[hdi_data.columns.str.startswith('gnipc') | (hdi_data.columns == 'Country')]
print(gnipc_columns.to_list())
# gnipc_columns.append('Country')

gnipc_data = hdi_data[gnipc_columns]
menna = gnipc_data.loc[gnipc_data['Country'].str.contains('|'.join(country_names))]
# print(test.values.tolist())
menna.to_csv('GNIPC.csv')