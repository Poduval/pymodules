# initialize ----
# %%
# import os
# os.getcwd()
import pandas as pd
from Py.recruitment import Recruitment
# %%

# import data ----
# %%
df = pd.read_csv("data/recruitment.txt", sep=";")
df.head()
# %%

# Analysis ----

## Initiating class, print available attributes ----
# %%
rc = Recruitment(df)
rc.Attributes()
# %%

## Attribute 1: print number of candidates ----
# %%
# rc.df
rc.n_candidates
# %%

## Attribute 2: overview of candidates ----
# %%
rc.Overview()
# %%

## Attribute 3: Results of interview ----
# %%
rc.Results()
rc.Results(top = False)
# %%