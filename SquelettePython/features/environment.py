import pandas as pd

def before_feature(context, feature):

    if 'excel' in feature.tags:   # >>> you can have this check on feature.name instead of tag
        path_to_file = 'src/files/excel.xlsx'
        df=pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if 'excel' in sc.name) # >>> find the first examples object for scenario with given name
        test_table = example.table
        print(df)
        new_df = df.fillna("")
        print('no empty cell version')
        print(new_df)
        for row in new_df.itertuples(index=False):
            test_table.add_row(row)
    else:
        print("nothing to do")
        