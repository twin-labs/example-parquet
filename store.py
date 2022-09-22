"""Using pandas to save a DataFrame object as a parquet file."""
import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": [1, 2, 3]})

df.to_parquet("df.parquet", index=False)
