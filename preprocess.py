import pandas as pd
df2 = pd.read_excel('./data2.csv').dropna()


def number_of_installs(installs: str):
    temp = installs.split(',')
    head = temp[:-1]
    tail = temp[-1]
    tail = tail.split('+')[0]
    return int(''.join([*head, tail]))


df2["Installs"] = df2["Installs"].apply(number_of_installs)
