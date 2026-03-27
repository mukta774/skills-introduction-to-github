"""Data loading and caching utilities."""

import pandas as pd
from typing import Optional

class DataLoader:
    """Handles dataset loading with caching."""
    
    DATASET_URL = "https://github.com/mukta774/skin_care/blob/2c6f1651027a2a53cbfb494afb2a1335f281e744/Skin_Type_OG.csv"
    
    _cache = {}
    
    @classmethod
    def load_dataset(cls, url: Optional[str] = None, cache: bool = True) -> pd.DataFrame:
        """Load dataset from URL with optional caching."""
        url = url or cls.DATASET_URL
        
        if cache and url in cls._cache:
            return cls._cache[url].copy()
        
        df = pd.read_csv(url)
        
        if cache:
            cls._cache[url] = df.copy()
        
        return df
    
    @staticmethod
    def check_missing_values(df: pd.DataFrame) -> dict:
        """Check and report missing values."""
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        
        return {
            'counts': missing[missing > 0],
            'percentages': missing_pct[missing_pct > 0]
        }
    
    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicate rows."""
        initial_rows = len(df)
        df_clean = df.drop_duplicates()
        removed = initial_rows - len(df_clean)
        
        if removed > 0:
            print(f"Removed {removed} duplicate rows")
        
        return df_clean