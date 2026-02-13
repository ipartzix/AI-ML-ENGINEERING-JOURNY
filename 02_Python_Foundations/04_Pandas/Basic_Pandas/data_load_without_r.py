import numpy as np

from pathlib import Path
import pandas as pd 


data = Path("D:/AI ML ENGINEERING JOURNY/02_Python_Foundations/04_Pandas/dataset/products.csv")
demo = pd.read_csv(data)
print(demo)
