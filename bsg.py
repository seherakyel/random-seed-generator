import time

class XorshiftRNG:
    def __init__(self, seed=None):
        if seed is None:
            self.state = time.time_ns() & 0xFFFFFFFF
        else:
            self.state = seed & 0xFFFFFFFF
        
        if self.state == 0:
            self.state = 0x92D68CA2  

    def next(self):
        x = self.state
        
        x ^= (x << 13) & 0xFFFFFFFF
        
        x ^= (x >> 17)
        
        x ^= (x << 5) & 0xFFFFFFFF
        
        self.state = x
        return x


rng = XorshiftRNG(seed=time.time_ns())

print("Üretilen ilk 5 sayı:")
for i in range(5):
    print(f"{i+1}. Sayı: {rng.next()}")