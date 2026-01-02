import math
from bsg import XorshiftRNG
import time

# Helper function to normalize 32-bit int to 0-1 float
def normalize(n):
    return n / 0xFFFFFFFF

def chi_square_test(numbers, num_bins=10):
    n = len(numbers)
    expected = n / num_bins
    counts = [0] * num_bins
    
    for num in numbers:
        # Normalize strictly to [0,1) for binning
        val = normalize(num)
        bin_idx = int(val * num_bins)
        if bin_idx == num_bins: 
            bin_idx -= 1
        counts[bin_idx] += 1
    
    chi_sq = sum(((c - expected) ** 2) / expected for c in counts)
    return chi_sq, counts

def runs_test(numbers):
    # Convert to bits based on median/0.5 threshold after normalization
    bits = ""
    for num in numbers:
        val = normalize(num)
        bits += '1' if val >= 0.5 else '0'
        
    n = len(bits)
    ones = bits.count('1')
    zeros = bits.count('0')
    
    prop = ones / n
    if abs(prop - 0.5) > (2 / math.sqrt(n)):
        return False, 0.0, "Frequency test failed"
    
    runs = 1
    for i in range(n - 1):
        if bits[i] != bits[i+1]:
            runs += 1
            
    expected_runs = 2 * n * prop * (1 - prop)
    std_dev = math.sqrt(2 * n * prop * (1 - prop) * (2 * prop * (1 - prop) - 1 / n))
    
    if std_dev == 0:
        return False, 0.0, 0
        
    z_score = (runs - expected_runs) / std_dev
    return True, z_score, runs

def main():
    # Use bsg.py's class
    rng = XorshiftRNG(seed=time.time_ns())
    
    # Generate 1000 numbers for robust statistics
    numbers = []
    for _ in range(1000):
        numbers.append(rng.next())
    
    print("--- Istatistiksel Test Sonuclari (bsg.py) ---")
    
    # 1. Chi-Square Test
    chi_sq, counts = chi_square_test(numbers)
    print(f"\n1. Ki-Kare (Chi-Square) Testi:")
    print(f"   H0: Sayilar 0-1 arasinda esit dagilmistir. (Normalizasyon sonrasi)")
    print(f"   Ki-Kare Degeri: {chi_sq:.4f}")
    # Critical value (df=9 p=0.05) = 16.92
    if chi_sq < 16.92:
        print("   SONUC: BASARILI (H0 reddedilemez, dagilim uniform)")
    else:
        print("   SONUC: BASARISIZ (H0 reddedildi)")

    # 2. Runs Test
    passed, z, num_runs = runs_test(numbers)
    
    print(f"\n2. Kosu (Runs) Testi (0-1 Esitligi ve Bagimsizlik):")
    print(f"   Kosularin Sayisi: {num_runs}")
    print(f"   Z-Skoru: {z:.4f}")
    
    if abs(z) < 1.96:
         print("   SONUC: BASARILI (Rastgelelik dogrulandi)")
    else:
         print("   SONUC: BASARISIZ (Rastgelelik supheli)")

if __name__ == "__main__":
    main()
