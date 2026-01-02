# RSÜ - Rastgele Sayı Üreteci Projesi

Bu proje, Beyzanur Hoca'nın verdiği RSÜ ödevi kapsamında **Xorshift** algoritması kullanılarak geliştirilmiştir. 

Proje, mevcut `bsg.py` dosyası üzerine kurulmuştur.

## Proje İçeriği ve Dosyalar

1.  **Kod**: [`bsg.py`](bsg.py)
    *   Algoritmanın Python implementasyonu.
    *   Xorshift algoritmasını barındırır.
    *   Yorum satırı içermez.

2.  **Sözde Kod (Pseudocode)**: [`pseudocode.md`](pseudocode.md)
    *   `bsg.py` içindeki algoritmanın adım adım mantıksal anlatımı.

3.  **Akış Şeması**: [`flowchart.mermaid`](flowchart.mermaid)
    *   Algoritmanın görsel akış diyagramı.

4.  **Algoritma Mantığı**: [`logic_explanation.md`](logic_explanation.md)
    *   Algoritmanın nasıl çalıştığının detaylı açıklaması.

5.  **Algoritma Çıktıları**: [`outputs.txt`](outputs.txt)
    *   Kodun ürettiği örnek çıktılar.

6.  **İstatistiksel Test Sonuçları**: [`test_results.txt`](test_results.txt)
    *   **Ki-Kare (Chi-Square) Testi**: Dağılımın homojenliğini doğrular.
    *   **Koşu (Runs) Testi**: 0 ve 1'lerin eşitliğini ve bağımsızlığını doğrular.
    *   Test kodlarına [`statistical_tests.py`](statistical_tests.py) dosyasından ulaşılabilir.

## Nasıl Çalıştırılır?

Ana algoritmayı çalıştırmak için:

```bash
python3 bsg.py
```

Testleri çalıştırmak için:

```bash
python3 statistical_tests.py
```
