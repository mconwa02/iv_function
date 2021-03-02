import pandas as pd
import numpy as np
import pytest

# pytest.fixtue
test_df = pd.DataFrame({"A": [123, 23, 100], "B": [24, 12, 12], "C": [23, 1, 22]})

print(test_df)

df = pd.read_csv("iv_data.csv")

print(df)

@pytest.mark.parametrize
def test_calculate_woe(woe):

    assert woe

if __name__ == '__main__':
    @pytest
