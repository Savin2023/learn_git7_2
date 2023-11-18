import numpy as np
import pandas as pd

def sko1(a):
    return(np.std(a))

def sko2(a):
    df=pd.DataFrame(data=a)
    return(pd.DataFrame.std(df))