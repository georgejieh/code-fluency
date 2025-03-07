"""
Pig Latin Translator - String Transformation Based on Conditionals

Context:
This program translates English text to Pig Latin, a made-up language where
words are altered according to specific rules about vowels and consonants.
The program handles multiple complex rules to determine how to transform
each word.

This exercise demonstrates:
1. String indexing, slicing, and manipulation
2. Complex conditional logic with multiple rules
3. Processing text word by word
4. Character-by-character analysis with positional tracking
5. Handling special cases within general patterns

Learning process:
- Needed a reminder on how to use enumerate() in for loops
- Had to look up the startswith() method (knew about endswith() already)
- Needed to refresh on how to use break to exit a loop when a condition is met
- Had to refactor my initial solution to handle multiple words in the input
"""

def translate(text: str) -> str:
    """
    Translate English text to Pig Latin.
    
    Args:
        text: str - The English text to translate
        
    Returns:
        str - The Pig Latin translation
        
    Purpose:
        Apply Pig Latin translation rules:
        1. If a word begins with a vowel or "xr"/"yt", add "ay" to the end
        2. If a word begins with consonants, move them to the end and add "ay"
        3. If a word begins with consonants followed by "qu", move all to the end and add "ay"
        4. If a word begins with consonants followed by "y", move consonants to the end and add "ay"
        
    Evolution:
        Initially implemented for single words, then enhanced to handle multiple words.
        Refined to better handle edge cases and improve structural clarity.
    """
    words = text.strip().split()
    result = []
    
    for word in words:
        # Rule 1: Word begins with vowel or special case "xr"/"yt"
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):  # Had to look up startswith() method
            translated_word = word + 'ay'
        else:
            vowels = 'aeiou'
            consonant_count = 0
            
            # Determine where the consonant cluster ends
            for char_position, char in enumerate(word):  # Had to refresh on enumerate usage
                # Rule 3: Handle "qu" after consonants
                if char == 'q' and char_position + 1 < len(word) and word[char_position + 1] == 'u':
                    consonant_count = char_position + 2
                    break  # Needed to look up break statement syntax
                # Rules 2 & 4: Regular vowel or "y" after consonants
                elif char in vowels or (char == 'y' and char_position > 0):
                    consonant_count = char_position
                    break
                # Edge case: all consonants
                if char_position == len(word) - 1:
                    consonant_count = len(word)
                    
            # Apply the transformation by rearranging and adding "ay"
            translated_word = word[consonant_count:] + word[:consonant_count] + 'ay'
            
        result.append(translated_word)
        
    return ' '.join(result)
