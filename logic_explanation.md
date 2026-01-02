# Algoritma Çalışma Mantığı (bsg.py)

Kullanılan algoritma **Xorshift32** türevidir. Bu yöntem, bilgisayarın bit seviyesindeki işlemlerini (XOR ve Kaydırma) kullanarak çok hızlı bir şekilde "sözde rastgele" (pseudo-random) sayılar üretir.

## Temel Bileşenler

1.  **Bitwise XOR (^)**: İki bit aynıysa 0, farklıysa 1 sonucunu verir. Bu işlem veriyi "karıştırmak" için mükemmeldir.
2.  **Bitwise Shoft (<< ve >>)**: Sayının bitlerini sağa veya sola kaydırır. Bu işlem, bitlerin konumunu değiştirerek sayının yapısını bozar.

## Adım Adım İşleyiş

1.  **Başlangıç (Seed)**:
    *   `__init__` fonksiyonunda, algoritmanın başlangıç değeri (`state`) belirlenir.
    *   Rastgelelik için `time.time_ns()` (nanosaniye hassasiyetli zaman) kullanılır.
    *   Sonuç `0xFFFFFFFF` ile maskelenerek 32-bit sınırında tutulur.

2.  **Sayı Üretimi (`next` fonksiyonu)**:
    *   Algoritma mevcut `state` değerini alır: `x = self.state`
    *   **Adım 1**: `x ^= (x << 13)` -> Sayı sola 13 bit kaydırılır ve kendisiyle XORlanır.
    *   **Adım 2**: `x ^= (x >> 17)` -> Sayı sağa 17 bit kaydırılır ve kendisiyle XORlanır.
    *   **Adım 3**: `x ^= (x << 5)` -> Sayı sola 5 bit kaydırılır ve kendisiyle XORlanır.
    *   *Not: Sola kaydırma işlemlerinden sonra `& 0xFFFFFFFF` işlemi yapılarak sayının 32 bitten taşması engellenir.*

3.  **Sonuç**:
    *   Ortaya çıkan yeni `x` değeri, bir sonraki adım için yeni `state` olarak kaydedilir.
    *   Hesaplanan `x` değeri (tam sayı olarak) kullanıcıya döndürülür.

Bu üç adımdaki (13, 17, 5) kaydırma miktarları, Xorshift algoritmasının mucidi George Marsaglia tarafından, 32-bit sayılar için maksimum periyodu (tekrar etmeden en uzun diziyi) verecek şekilde matematiksel olarak seçilmiştir.
