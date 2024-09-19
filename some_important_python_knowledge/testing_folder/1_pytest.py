# Here is how to write test with pytest
# when you want to run the file using "pytest {file_path}"

import pandas as pd
import pytest


def normal_test() :
    x = 1
    y = 1
    assert x==y

def test_dataframe() :
    df1 = pd.DataFrame({
        "col1": [1,2],
        "col2": [2,3]
    })
    df2 = pd.DataFrame({
        "col1": [1,2],
        "col2": [2,3]
    })
    
    pd.testing.assert_frame_equal(df1, df2)
    