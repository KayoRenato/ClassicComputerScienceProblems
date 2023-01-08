class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.__compresss(gene)

    def __compresss(self, gene: str) -> None:
        self.bit_string: int = 1 #sentinel

        # bitwise operators
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid nucleotide: {nucleotide}")


    def decompress(self) -> str:
        gene: str = ""

        for i in range(0, self.bit_string.bit_length()-1, 2): # -1 to exclude the sentinel
            bits: int = self.bit_string  >> i & 0b11 # get only two relevant bits

            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid nucleotide: {bits}")
        
        return gene[::-1] # reverse complement string using slice with reverse
    
    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof

    original: str = "ACTGAGTGAGGTA"*1000
    print(f"Original is {getsizeof(original)} bits")

    compressed: CompressedGene = CompressedGene(original)
    print(f"Compressed is {getsizeof(compressed.bit_string)} bits")

    print(compressed)

    print(f"Original and decompressed are the same: {original == compressed.decompress()}")