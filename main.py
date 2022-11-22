import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import stats

print(" ")

# filename = 'pima/pima.csv'
# filename = 'heart/heart.csv'
filename = 'wdbc/wdbc.csv'

dataset = pd.read_csv(filename)
# positive_df = dataset[dataset['Class'] == 1] 
# negative_df = dataset[dataset['Class'] == 2]
# positive_df = dataset[dataset['Class'] == "B"] 
# negative_df = dataset[dataset['Class'] == "M"] 
# positive_df = dataset[dataset['Class'] == "tested_positive"] 
# negative_df = dataset[dataset['Class'] == "tested_negative"]

# Shapiro Wilk test
for idx, col in enumerate(dataset.columns):
    if not col == "Class":
        # positive_attribute_array = positive_df.loc[:, col].to_numpy()
        # negative_attribute_array = negative_df.loc[:, col].to_numpy()
        g1 = dataset.loc[:,"Radius1"].to_numpy()
        g2 = dataset.loc[:,"Radius2"].to_numpy()
        g3 = dataset.loc[:,"Radius3"].to_numpy()
        # positive_shapiro_wilk_test = stats.shapiro(positive_attribute_array)
        # negative_shapiro_wilk_test = stats.shapiro(negative_attribute_array)
        # mannwhitneyu_test = stats.mannwhitneyu(positive_attribute_array, negative_attribute_array)
        kruskal_test = stats.kruskal(g1, g2, g3)
        # print("Col: ", col, "Positive test: %.5f" % positive_shapiro_wilk_test.pvalue, "Negative test: %.5f" % negative_shapiro_wilk_test.pvalue, "Mannwhitneyu test: %.5f" % mannwhitneyu_test.pvalue)
        print(kruskal_test)

print("")



# print(dataset)
# print(positive_df)
# print(negative_df)

# print("{}{}_{}_results.png saved...".format(results_folder, class_number, filename.split('.')[0]))


# result_df = pd.DataFrame(data=[WL_arr, ZC_arr, VAR_arr, MAV_arr, SSC_arr],
#                         index=["WL_arr", "ZC_arr", "VAR_arr", "MAV_arr", "SSC_arr"],
#                         columns=dataset.columns)
