Trädportalen Export
===================

Extracts tree observations from [Trädportalen](https://www.tradportalen.se/), converts them to
GeoJSON and finally zips the converted data.

The reason for this is that Trädportalen currently does not have a machine friendly export for all its
data.

## The data

If you are just looking for the actual exported data, it can be downloaded here: https://tradportalen.s3.eu-north-1.amazonaws.com/tradportalen.zip

## Running

Run the `export.sh` script:

```shell
./export.sh
```

All downloaded data will be stored in the `data/` directory, finally storing a `tradportalen.zip` with all the combined obsvervations in one file.
