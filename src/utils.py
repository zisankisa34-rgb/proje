"""
Yardımcı fonksiyonlar: logging, seed, basit util'ler.
Geliştirip projeye özel hale getirebilirsiniz.
"""

import logging
import os
import random
import numpy as np


def setup_logging(level: str = "INFO"):
    """Basit logging ayarı."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=numeric_level
    )


def seed_everything(seed: int = 42):
    """Rastgeleliği kontrol altına almak için seed atar."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        # torch yoksa atla
        pass


def ensure_dir(path: str):
    """Verilen dizini oluşturur (varsa atlar)."""
    os.makedirs(path, exist_ok=True)
