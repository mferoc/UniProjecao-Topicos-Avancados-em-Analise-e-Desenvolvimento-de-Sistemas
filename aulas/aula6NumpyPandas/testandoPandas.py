import numpy as np
import pandas as pd

games = pd.read_csv(
    "vgsales.csv",
    sep=',',
    header=0
)
print(games.shape)
games.head()
