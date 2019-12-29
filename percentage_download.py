import pandas as pd
from preprocess import df2

categories = []
for category in df2['Category']:
    if category in categories:
        pass
    else:
        categories.append(category)
installes = []
for category in categories:
    total_install = df2[df2['Category'] == category]['Installs'].sum()
    installes.append(total_install)
cta_ins = pd.DataFrame(list(zip(categories, installes)),
                       columns=['Category', 'Installs'])
total_installs = cta_ins['Installs'].sum()
cta_ins['Installs'] = cta_ins['Installs'].apply(
    lambda x: (x*100)/total_installs)
cta_ins = cta_ins.sort_values(by=['Installs'], ascending=False)

cta_ins.to_excel("percentage_download.xlsx", index=False)
