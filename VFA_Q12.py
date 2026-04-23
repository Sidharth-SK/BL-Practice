#Count total vowels in a given sentence (case-insensitive)
sentence: str = "I Love Python"
def vowel_count(input_str: str) -> int:
    vowels: str = "aeiou"
    return sum(1 for char in input_str.lower() if char in vowels)
