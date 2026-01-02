# RSÜ Algoritması Sözde Kodu (bsg.py Analizi)

BAŞLA

    SINIF XorshiftRNG:
        
        FONKSİYON KURUCU(seed DEĞERİ):
            EĞER seed BOŞ İSE:
                state = ŞİMDİKİ_ZAMAN_NANOSANİYE() VE 0xFFFFFFFF
            DEĞİLSE:
                state = seed VE 0xFFFFFFFF
            
            EĞER state 0'A EŞİT İSE:
                state = 0x92D68CA2 (Yedek Sabit Değer)

        FONKSİYON next():
            x = state
            
            // 1. Adım: Sola Kaydır 13 ve XOR
            x = x XOR ((x Sola Kaydır 13) VE 0xFFFFFFFF)
            
            // 2. Adım: Sağa Kaydır 17 ve XOR
            x = x XOR (x Sağa Kaydır 17)
            
            // 3. Adım: Sola Kaydır 5 ve XOR
            x = x XOR ((x Sola Kaydır 5) VE 0xFFFFFFFF)
            
            state = x
            DÖNDÜR x (32-bit Tam Sayı)

    ANA PROGRAM:
        rng = YENİ XorshiftRNG(seed=ŞİMDİKİ_ZAMAN_NANOSANİYE())
        
        DÖNGÜ i -> 0'dan 5'e:
            YAZDIR (i+1). Sayı: rng.next()

BİTİR
