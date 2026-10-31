import pandas as pd 
from pathlib import Path 
import os 

def save_as_Parquet(df, outputpath):
    #creating output Directory 
    outputpath = Path(outputpath)
    outputpath.parent.mkdir(parents = True, exist_ok = True)

    #Saveing data as Parquet 
    df.to_parquet(
        outputpath,
        engine = 'pyarrow',
        index = False,
        compression = 'snappy'
    )    

    print('Parquet saved secsessfuly')

    #Getting file size 
    file_size = os.path.getsize(outputpath)
    print("Parquet file size:", file_size, "bytes")

    return file_size