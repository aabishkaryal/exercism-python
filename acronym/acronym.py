# abbreviate generates acronym for the given words.
def abbreviate(words: str) -> str:
    acronym = ''
    words = words.replace('-', ' ').replace('_', ' ').split(' ')
    for word in words:
        acronym += word[0].upper() if len(word) > 0 else ""
    return acronym
