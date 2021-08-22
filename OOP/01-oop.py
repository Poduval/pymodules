
import pandas as pd
from OOP.Py.recruitment import Recruitment

# import data
df = pd.read_csv("OOP/data/recruitment.txt", sep=";")
df.head()

# Analysis
rc = Recruitment(df)
rc.Attributes()
rc.df
rc.n_candidates
rc.Overview()
rc.Results()
rc.Results(top = False)



