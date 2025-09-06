import pandas as pd
import numpy as np


if __name__ == '__main__':
    #TODO: make commandline arguments
    gon_02 = pd.read_csv("../data/GON_25_02_UTM.csv")

    ref_str = "OLE3"
    float_str = "OLE3-measured"
    coords = ["Easting", "Northing", "Elevation"] #column names

    #print(gon_02.head(5))
    #print(gon_02.dtypes)
    #print(gon_02.info())
    #print(gon_02["Name"].head())

    
    ref_p = gon_02.loc[gon_02["Name"] == ref_str, coords]
    float_p = gon_02.loc[gon_02["Name"] == float_str, coords] # maybe put both in one dataframe with .isin() ?

    #TODO: make np.array ??? -> no hassle with column names and so on ...
    # desired result: array/tuple/whatever with delta x, delta y and delta z
    # 

    print(type(float_p))
    print(type(float_p["Easting"]))

    print(float_p)
    print(ref_p)
    print(float_p.iloc[0, 0] - ref_p.iloc[0, 0]) # is the same as:
    print(float_p.iat[0, 0] - ref_p.iat[0, 0])

    #print(delta_x)
    # save corrected coordinates here:
    gon_02_corr = gon_02


    #things wich didn't work:
    #print(float_p[0, "Easting"])
    #print(float_p.loc[0, "Easting"] - ref_p.loc[0, "Easting"])

