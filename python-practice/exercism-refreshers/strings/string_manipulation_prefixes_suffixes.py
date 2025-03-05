"""
String Manipulation: Prefixes and Suffixes

This module contains functions for manipulating strings through prefix and suffix operations
for an English vocabulary assignment.

Context:
These functions were created to help with an English vocabulary homework exercise
focused on creating new words by adding prefixes and suffixes.

This exercise demonstrates:
1. Adding prefixes to words
2. Creating word groups with consistent prefixes
3. Removing suffixes while handling spelling changes
4. Converting adjectives to verbs by adding suffixes

My Learning Process:
- I initially struggled with initializing variables outside loops and concatenating in the loop
- I had to look up string slicing syntax for removing characters
- I learned about the importance of handling punctuation when working with real text
- I discovered the usefulness of the isalnum() method for detecting non-alphanumeric characters
"""


def add_prefix_un(word):
    """
    Add the prefix 'un' to a given word.
    
    Args:
        word: str - the root word to be prefixed
        
    Returns:
        str - the word with 'un' added at the beginning
        
    Purpose:
        Creates a negative or opposite form of the original word by adding 'un'.
        
    Examples:
        >>> add_prefix_un("happy")
        'unhappy'
        >>> add_prefix_un("manageable")
        'unmanageable'
    """
    un_word = f'un{word}'
    return un_word


def make_word_groups(vocab_words):
    """
    Create a string with a prefix applied to each word in a list.
    
    Args:
        vocab_words: list - list of words, with prefix as the first element
        
    Returns:
        str - a string with the prefix and prefixed words separated by " :: "
        
    Purpose:
        Formats a group of related words that all use the same prefix,
        showing both the prefix alone and then each word with the prefix applied.
        
    Notes:
        Initially tried to build this entirely within the loop, but learned
        it's better to initialize the result variable first and build on it.
        
    Examples:
        >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
        'en :: enclose :: enjoy :: enlighten'
        >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
        'pre :: preserve :: predispose :: preposition'
    """
    prefix = vocab_words[0]
    result = prefix 
    
    for word in range(1, len(vocab_words)):  # Had to look up this syntax for range-based loops
        result += f' :: {prefix}{vocab_words[word]}'
    
    return result


def remove_suffix_ness(word):
    """
    Remove the suffix 'ness' from a word and fix any spelling changes.
    
    Args:
        word: str - word ending with 'ness' suffix
        
    Returns:
        str - root word with 'ness' removed and spelling adjusted if needed
        
    Purpose:
        Extracts the original root word by removing the 'ness' suffix,
        handling the special case where 'i' needs to be changed back to 'y'.
        
    Notes:
        Had to be careful with string immutability - created new strings
        rather than trying to modify in place.
        
    Examples:
        >>> remove_suffix_ness("heaviness")
        'heavy'
        >>> remove_suffix_ness("sadness")
        'sad'
    """
    no_ness = word[:-4]
    
    if no_ness[-1] == 'i':
        return no_ness[:-1] + 'y'  # Had to learn about how to deal with string immutability here
    
    return no_ness


def adjective_to_verb(sentence, index):
    """
    Extract an adjective from a sentence and convert it to a verb.
    
    Args:
        sentence: str - a sentence containing an adjective to extract
        index: int - the index of the word to extract after splitting
        
    Returns:
        str - the extracted adjective converted to a verb by adding 'en'
        
    Purpose:
        Demonstrates the process of "verbing" or "verbifying" in English,
        where adjectives can be turned into verbs by adding an 'en' suffix.
        
    Notes:
        Had to handle punctuation carefully - words at the end of a sentence
        have punctuation that needs to be removed before adding the suffix.
        Learned to use isalnum() to check for non-alphanumeric characters.
        
    Examples:
        >>> adjective_to_verb('I need to make that bright.', -1)
        'brighten'
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'
    """
    listed_sentence = sentence.split()
    
    word = listed_sentence[index]
    
    if word and not word[-1].isalnum():  # Had to look up isalnum() to identify punctuation
        return word[:-1] + 'en'
    
    return word + 'en'