import pandas as pd
from preprocess import df2

range_download = {'10,000 and 50,000': 0, '50,000 and 150,000': 0,
                  '150,000 and 500,000': 0, '500,000 and 5,000,000': 0, '5,000,000+': 0}
for app in df2['Installs']:
    if app > 10000 and app <= 50000:
        range_download['10,000 and 50,000'] += 1
    elif app > 50000 and app <= 150000:
        range_download['50,000 and 150,000'] += 1
    elif app > 150000 and app <= 500000:
        range_download['150,000 and 500,000'] += 1
    elif app > 500000 and app <= 5000000:
        range_download['500,000 and 5,000,000'] += 1
    else:
        range_download['5,000,000+'] += 1
ranges = []
values = []
for k, v in range_download.items():
    ranges.append(k)
    values.append(v)
ran_dow = pd.DataFrame(list(zip(ranges, values)), columns=[
                       'Ranges', 'Number of Downloads'])
ran_dow.to_excel("number_of_download.xlsx", index=False)
