from typing import Dict, List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    original_candidates = candidates
    word, candidates = word.upper(), [x.upper() for x in candidates]
    anagrams = []
    for i, x in enumerate(candidates):
        if (isAnagram(word, x)):
            anagrams.append(original_candidates[i])
    return anagrams


def isAnagram(word1: str, word2: str) -> bool:
    if (len(word1) != len(word2) or word1 == word2):
        return False
    for i, _ in enumerate(word1):
        letter: str = word1[i]
        if (word1.count(letter) != word2.count(letter)):
            return False
    return True
