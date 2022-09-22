"""Read a filtered slice of a parquet file into a DataFrame object using Polars. Convert to Pandas."""
import polars as pl

lazy = (
    pl.scan_parquet("df.parquet")
        .filter(pl.col("a") > 1)
)

df = lazy.collect().to_pandas()

print(df)