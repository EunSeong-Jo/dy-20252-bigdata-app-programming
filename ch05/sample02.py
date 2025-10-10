import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

jumsu = [3.5, 4.0, 4.5, 3.8]
year = [2024, 2025, 2026, 2027]

jumsu_df = pd.DataFrame(
    {
        'jumsu': jumsu,
    }, index = year)
jumsu_df.plot.line()
plt.show()

