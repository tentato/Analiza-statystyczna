import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import stats

print(" ")

###### heart_1 ######
# filename = 'heart/heart_1.csv'
# dataset = pd.read_csv(filename, delimiter=";")
# men_df = dataset[dataset['Sex'] == 0] 
# women_df = dataset[dataset['Sex'] == 1]

# max_heart_rate_men_array = men_df.loc[:,"MaxHeartRate"].to_numpy()
# max_heart_rate_women_array = women_df.loc[:,"MaxHeartRate"].to_numpy()

# men_shapiro_wilk_test = stats.shapiro(max_heart_rate_men_array)
# women_shapiro_wilk_test = stats.shapiro(max_heart_rate_women_array)
# mannwhitneyu_test = stats.mannwhitneyu(men_shapiro_wilk_test, women_shapiro_wilk_test)
# print(men_shapiro_wilk_test)
# print(women_shapiro_wilk_test)
# print(mannwhitneyu_test)
###### heart_1 ######


###### heart_2 ######
# filename = 'heart/heart_2.csv'
# dataset = pd.read_csv(filename, delimiter=";")
# Po59_df = dataset[dataset['Group'] == "Po59"] 
# Przed51_df = dataset[dataset['Group'] == "Przed51"] 
# Miedzy51i59_df = dataset[dataset['Group'] == "Miedzy51i59"] 

# max_heart_rate_Po59_array = Po59_df.loc[:,"MaxHeartRate"].to_numpy()
# max_heart_rate_Przed51_array = Przed51_df.loc[:,"MaxHeartRate"].to_numpy()
# max_heart_rate_Miedzy51i59_array = Miedzy51i59_df.loc[:,"MaxHeartRate"].to_numpy()

# Po59_shapiro_wilk_test = stats.shapiro(max_heart_rate_Po59_array)
# Przed51_shapiro_wilk_test = stats.shapiro(max_heart_rate_Przed51_array)
# Miedzy51i59_shapiro_wilk_test = stats.shapiro(max_heart_rate_Miedzy51i59_array)
# kruskal_test = stats.kruskal(max_heart_rate_Po59_array, max_heart_rate_Miedzy51i59_array, max_heart_rate_Przed51_array)

# wilcoxon_Po59_Przed51_test = stats.wilcoxon(max_heart_rate_Po59_array, max_heart_rate_Przed51_array)
# wilcoxon_Po59_Miedzy51i59_test = stats.wilcoxon(max_heart_rate_Po59_array, max_heart_rate_Miedzy51i59_array)
# wilcoxon_Przed51_Miedzy51i59_test = stats.wilcoxon(max_heart_rate_Przed51_array, max_heart_rate_Miedzy51i59_array)

# print("Po59: ",Po59_shapiro_wilk_test)
# print("Przed51: ",Przed51_shapiro_wilk_test)
# print("Miedzy51i59: ",Miedzy51i59_shapiro_wilk_test)
# print(kruskal_test)
# print("Para Po59 i Przed51: ",wilcoxon_Po59_Przed51_test)
# print("Para Po59 i Miedzy51i59: ",wilcoxon_Po59_Miedzy51i59_test)
# print("Para Przed51 i Miedzy51i59: ",wilcoxon_Przed51_Miedzy51i59_test)

# Wynik:
# Po59:  ShapiroResult(statistic=0.9658281207084656, pvalue=0.01811080612242222)
# Przed51:  ShapiroResult(statistic=0.9683021306991577, pvalue=0.026885511353611946)
# Miedzy51i59:  ShapiroResult(statistic=0.9587957859039307, pvalue=0.006085100583732128)
# Wniosek: Rozkład różny od normalnego dla Miedzy51i59 - wykonać test nieparametryczny.
# KruskalResult(statistic=33.8303687772499, pvalue=4.506389845871221e-08)
# Wniosek: Istotna różnica dla co najmniej jednej pary, dla której? - wykonać test Wilcoxona.
# Para Po59 i Przed51:  WilcoxonResult(statistic=726.0, pvalue=1.7589680484140034e-07)
# Para Po59 i Miedzy51i59:  WilcoxonResult(statistic=1439.0, pvalue=0.03079307540084529)
# Para Przed51 i Miedzy51i59:  WilcoxonResult(statistic=1070.0, pvalue=0.00035343717027207683)
# Wniosek: Istotna różnica dla pary Po59 i Miedzy51i59
###### heart_2 ######

###### survey ######
# filename = 'gym/survey.csv'
# dataset = pd.read_csv(filename, delimiter=";")

# KgBefore_array = dataset.loc[:,"KgBefore"].to_numpy()
# KgAfter_array = dataset.loc[:,"KgAfter"].to_numpy()

# KgBefore_shapiro_wilk_test = stats.shapiro(KgBefore_array)
# KgAfter_shapiro_wilk_test = stats.shapiro(KgAfter_array)
# paired_t_test = stats.ttest_rel(KgAfter_array, KgBefore_array)

# print("KgBefore: ",KgBefore_shapiro_wilk_test)
# print("KgAfter: ",KgAfter_shapiro_wilk_test)
# print("Paired t-test: ",paired_t_test)

# Wynik:
# KgBefore:  ShapiroResult(statistic=0.9979059100151062, pvalue=0.37734147906303406)
# KgAfter:  ShapiroResult(statistic=0.9978006482124329, pvalue=0.3324885964393616)
# Wniosek: Rozkład normalny dla obu grup.
# Paired t-test:  Ttest_relResult(statistic=28.43292751032821, pvalue=2.411765476943316e-125)
# Wniosek: Hipoteza zerowa odrzucona - sterydy mają wpływ na wzros masy.
###### survey ######

print("")