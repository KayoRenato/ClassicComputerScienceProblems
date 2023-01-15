from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTACGGTACGTA"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):  # limiting the end of the string
            return gene

        # Initialize codons from three nucleotides
        codon: Codon = (Nucleotide[s[i]],
                        Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


my_gene: Gene = string_to_gene(gene_str)

print(f'My Gene: {my_gene}')


# Linear search

print("\n-----  Linear search  -----")
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.T, Nucleotide.T)
gta: Codon = (Nucleotide.G, Nucleotide.T, Nucleotide.A)

print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))
print(linear_contains(my_gene, gta))

# Binary search
#? Require a sorted list  before the binary search
#? If you realize only one search, a linear search is more performative than a binary search.

print("\n-----  Binary search  -----")
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while low <= high: #when have search range
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)

print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
print(binary_contains(my_sorted_gene, gta))