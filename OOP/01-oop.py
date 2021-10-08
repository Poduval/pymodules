# initialize ----
import os
os.getcwd()
import pandas as pd
from OOP.recruitment import Recruitment

# import data ----

df = pd.read_csv("OOP/data.txt", sep=";")
df.head()

# Analysis ----
rc = Recruitment(df)
rc.Attributes()
rc.df
rc.n_candidates
rc.Overview()
rc.Results()
rc.Results(top = False)
