"""
Veri ön işleme yardımcıları (örnek).
Bu dosyayı projenizin ihtiyaçlarına göre genişletebilirsiniz.

"""

from pathlib import Path
import pandas as pd
import numpy as np
from typing import Union


def load_csv(path: Union[str, Path]) -> pd.DataFrame:
    """CSV dosyasını yükler ve DataFrame döndürür."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} bulunamadı.")
    return pd.read_csv(path)


def basic_clean(df: pd.DataFrame, drop_na_threshold: float = 0.5) -> pd.DataFrame:
    """
    Temel temizleme:
    - Çoklu eksik değeri olan sütunları düşürür (eşik: drop_na_threshold).
    - Sayısal sütunlardaki inf değerleri NaN yapar.
    - Gerekirse diğer dönüşümler eklenebilir.
    """
    df = df.copy()
    # sütunlardaki boş oranı kontrolü
    na_ratio = df.isna().mean()
    drop_cols = na_ratio[na_ratio > drop_na_threshold].index.tolist()
    if drop_cols:
        df.drop(columns=drop_cols, inplace=True)
    # inf -> NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    # örnek: kategorik stringlerde trim
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()
    return df


def save_processed(df: pd.DataFrame, path: Union[str, Path], index: bool = False):
    """İşlenmiş veriyi CSV olarak kaydeder."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
