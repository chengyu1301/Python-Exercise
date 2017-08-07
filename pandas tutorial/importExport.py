# read: csv, excel, sql, json, html, clipboard, ......

import pandas as pd

data = pd.read_csv('students.csv')
print(data)

data.to_pickle('students.pickle')