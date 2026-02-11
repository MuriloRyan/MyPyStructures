mask_64 = 0xFFFFFFFFFFFFFFFF

class SplitMix64:
    def __init__(self, seed: int) -> None:
        self.state: int = seed & mask_64
        self.i = 0
        self.temp_i = 0

    def generate(self):
        # 1. Increment state
        self.state = (self.state + 0x9E3779B97F4A7C15) & mask_64
        
        # 2. Mixing
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & mask_64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & mask_64
        z = (z ^ (z >> 31)) & mask_64
        return z
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.temp_i > 0:
            if self.i < self.temp_i:
                self.i += 1
                return self.generate()
            
            self.temp_i = 0 
            raise StopIteration
        
        # Default behavior: Infinite generation
        self.i += 1
        return self.generate()

    def __call__(self, steps: int):
        """
        Used in loops where you want n returns

        for i in SplitMix64(n):
            return i

        """
        self.temp_i = self.i + steps
        return self
