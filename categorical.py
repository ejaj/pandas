import pandas as pd
import numpy as np

# lmh_values = ["low", "high", "medium", "medium", "high"]
# lmh_cat = pd.Categorical(lmh_values)
# print(lmh_cat)
# print(lmh_cat.categories)
# print(lmh_cat.codes)
# print(lmh_cat.sort_values())
# cat_series = pd.Series(lmh_values, dtype="category")
# print(cat_series)
# np.random.seed(123456)
# values = np.random.randint(0, 100, 5)
# bins = pd.DataFrame({"Values": values})
# print(bins)
# bins['Group'] = pd.cut(values, range(0, 101, 10))
# print(bins)
# print(bins.Group)


np.random.seed(123456)
names = ['Ryani', 'Ivana', 'Sami', 'Samir', 'Rose']
grades = np.random.randint(50, 101, len(names))
scores = pd.DataFrame({"Name": names, 'Grade': grades})
score_bins = [0, 59, 62, 66, 69, 72, 76, 79, 82, 86, 89, 92, 99, 100]
letter_grades = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
letter_cats = pd.cut(scores.Grade, score_bins, labels=letter_grades)
scores['Letter'] = letter_cats
print(scores)
