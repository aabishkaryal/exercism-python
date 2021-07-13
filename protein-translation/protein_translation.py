translation_dict = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUG": "Leucine",
    "UUA": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = translation_dict.get(codon, 0)
        if protein == 0:
            raise Exception("unknown codon")
        elif protein == "STOP":
            return result
        else:
            result.append(protein)
    return result
