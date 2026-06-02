import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

print(df.describe())