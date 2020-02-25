import pandas as pd # to import excel files
import numpy as np

# A simple form of merging two DataFrames column-wise
comp_list = pd.DataFrame(index=range(len(80)), columns=['col1']) # 80 is the number of elements/rows in each column
df_ = pd.DataFrame(index=range(len(comp_list)), columns=['col2','col3'])
df_.shape
merged = pd.concat([comp_list, df_], axis=1, sort=False) # Merge on columns
print(merged)
