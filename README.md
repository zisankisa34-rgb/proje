# proje

Proje: Arıza Öngörü (proje)

Dizin yapısı
project/
 ├─ data/
 │   └─ raw/        (ham veri)
 │   └─ processed/  (temizlenmiş veri)
 ├─ notebooks/
 │   └─ 01_veri_test.ipynb
 ├─ models/          (eğitilmiş modeller)
 ├─ src/
 │   └─ preprocessing.py
 │   └─ utils.py
 ├─ docs/            (dokümantasyon)
 ├─ outputs/         (grafikler, raporlar, çıktı dosyaları)
 └─ README.md

Başlamak için
1. Sanal ortam oluşturun: python -m venv .venv
2. Aktif edin: source .venv/bin/activate (Linux/macOS) veya .venv\Scripts\activate (Windows)
3. Bağımlılıkları yükleyin: pip install -r requirements.txt
4. Ham veriyi `data/raw/` içine koyun.
5. `src/preprocessing.py` içindeki fonksiyonlarla veriyi işleyip `data/processed/` içine kaydedin.

Notlar
- Boş dizinlerin git tarafından izlenmesi için `.gitkeep` dosyaları eklendi.
- `data/raw` ve `models` gibi büyük dosya içerebilecek klasörler `.gitignore` içine alınmıştır; isterseniz bu davranışı değiştirebiliriz.
