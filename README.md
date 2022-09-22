# example-parquet

This project displays usage of the Parquet format for batch files stored to disk. Parquet allows predicate pushdown and better memory utilization for projects to implement (like Polars).

Pandas can store a DataFrame to a parquet file.

```
   a  b
0  1  1
1  2  2
2  3  3
```

```
❯ poetry run python store.py
```

Polars can read that with lazy execution, only bringing into memory what you want. Polars works well with the Parquet format. We can use Polars for a thin IO layer and convert back to Pandas.

```
❯ poetry run python load.py 
   a  b
0  2  2
1  3  3
```