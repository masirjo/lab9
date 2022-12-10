# -*- coding: utf-8 -*-
"""lab9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZucqT22npSNNVLmazV6YsNOPZzoGWHf_
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import random
import matplotlib.pyplot as plt
import math as math
# %matplotlib inline

# 1
psg = pd.read_csv('/titanic.csv')
psg.info()

# 2.1
a_s = psg[(psg["Age"] >= 30) & (psg["Age"] < 40) & (psg["Sex"] == "male")]
a_s

# 2.2
a_s2 = psg[((psg["Age"] < 25) & (psg["Sex"] == "female")) | (psg["Pclass"] == 1) & (psg["Survived"] == 1)]
a_s2

# 3
s_s = psg.groupby(["Sex","Pclass"]).size()
s_s.plot.bar()

# 4
a_s3 = psg[(psg["Age"] < 25)]
a_s3

s_s = psg.groupby(["Sex","Pclass","Survived"]).size()
s_s.plot.bar()