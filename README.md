# example-parquet

This project demonstrates usage of the Parquet format for batch files stored to disk. Parquet allows predicate pushdown providing, in theory, better memory utilization for projects to implement (like Polars).

Pandas can store a DataFrame to a parquet file.

```
❯ ./df.parquet
   a  b
0  1  1
1  2  2
2  3  3
```

```
❯ poetry run python store.py
```

Polars can read the parquet file with lazy execution.

```py
lazy = (
    pl.scan_parquet("df.parquet")
        .filter(pl.col("a") > 1)
)
```

This example uses Polars as a thin IO layer to convert to Pandas DataFrames.

```
❯ poetry run python load.py 
   a  b
0  2  2
1  3  3
```

See [#1](https://github.com/twin-labs/example-parquet/issues/2) for zero-copy plans.
