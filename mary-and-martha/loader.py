"""
Insight Engine - Experimental Test Data, Parsed with Purpose.
"""

import pandas as pd

def load_csv(path: str) -> pd.DataFrame:

    """
    Load a CSV file and return a DataFrame.

    Args: path (str): Path on local disk to the CSV file.

    Returns:

      pd.DataFrame: Parsed data.
    """

  return pd.read_csv(path)
