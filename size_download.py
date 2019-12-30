import pandas as pd
from preprocess import df2

range_download_size = {'10M to 20M': 0, '20M to 30M': 0, '30M+': 0}
for app in df2['Size']:
    if app > '10M' and app <= '20M':
        range_download_size['10M to 20M'] += 1
    elif app > '20M' and app <= '30M':
        range_download_size['20M to 30M'] += 1
    else:
        range_download_size['30M+'] += 1
ranges = []
values = []
for k, v in range_download_size.items():
    ranges.append(k)
    values.append(v)
ran_dow = pd.DataFrame(list(zip(ranges, values)), columns=[
                       'Ranges', 'Number of Downloads'])
ran_dow.to_excel("number_of_download_size.xlsx", index=False)
