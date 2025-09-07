import pandas as pd
import numpy as np
import argparse

if __name__ == '__main__':
    # get command line arguments
    desc = "performs base correction for RTK-GNSS measurements with base placed over arbitrary point"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("--file", required=True, type=str)
    parser.add_argument("--ref", required=True, type=str)
    parser.add_argument("--meas", required=True, type=str)

    args = parser.parse_args()

    fn = args.file
    ref_str = args.ref
    meas_str = args.meas
    coords = ["Easting", "Northing", "Elevation"] #column names, should be mutable by commandline aswell ...

    # read data:
    table = pd.read_csv(fn)

    # reference and measured cartesian 3D point coordinates only
    ref_p = table.loc[table["Name"] == ref_str, coords]
    meas_p = table.loc[table["Name"] == meas_str, coords]     

    # desired result: array/tuple/whatever with delta x, delta y and delta z
    delta = meas_p.iloc[0] - ref_p.iloc[0] # = pd.Series

    # save corrected coordinates here:
    corr = table - delta # correct coordinats, but all other data lost ...

    #old = table.copy() # for checking purposes ..
    table.loc[table["Name"] != ref_str, coords] = corr.loc[corr["Name"] != ref_str, coords] # df w/ correct coordinates and all other data.

    #print((table[coords] + delta) == old[coords])
    #print(table[coords] == old[coords])
    #print(table.head(5))
    #coords.append("Name")
    #print(table[coords].head(5))

    # write to disc:
    base = fn.removesuffix('.csv')
    fn = base + '-corr.csv'
    
    table.to_csv(path_or_buf = fn)
