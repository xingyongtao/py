from extract import *
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help='input excel file path')
parser.add_argument("output", help='output excel file path')
args = parser.parse_args()

raw = pd.read_excel(args.input, sheet_name="Sheet1", index_col=0)

data = []
for drug, col in raw.iteritems():
    # print(drug)
    for day, content in col.iteritems():
        if pd.isnull(content):
            continue
        tuples = split_cell(content)
        for (person, count) in tuples:
            # print('{},{},{},{}'.format(day, drug, person, count))
            data.append([day, drug, person, count])

dest = pd.DataFrame(data, columns=['日期', '药品', '销售', '数量'])
dest.to_excel(args.output, index=False)
