"""
String Methods: Essay Editor

This module contains functions for helping edit and improve an essay using string methods
for proofreading and text enhancement.

Context:
These functions were created to assist a younger sister with editing her paper
for school, focusing on proper punctuation, grammar, and word choice.

This exercise demonstrates:
1. Capitalizing words in titles
2. Checking for proper sentence endings
3. Cleaning up unnecessary whitespace
4. Replacing words with better alternatives

My Learning Process:
- I initially struggled with for loop syntax and had to look up how to use enumerate()
- I received a pylint warning about using range(len()) and learned about enumerate()
- I had to refresh my understanding of the strip() method for whitespace removal
- I needed to learn how to properly handle punctuation when replacing words in a sentence
"""


def capitalize_title(title):
    """
    Convert the first letter of each word in a title to uppercase.
    
    Args:
        title: str - title string that needs title casing
        
    Returns:
        str - title string with the first letter of each word capitalized
        
    Purpose:
        Ensures proper formatting for paper titles by capitalizing
        the first letter of each word.
        
    Notes:
        First iteration used range(len(title_list)) but I learned that
        enumerate() provides a more Pythonic approach.
        
    Examples:
        >>> capitalize_title("my hobbies")
        'My Hobbies'
        >>> capitalize_title("fish are cold blooded")
        'Fish Are Cold Blooded'
    """
    title_list = title.split()
    
    for word_index, word_value in enumerate(title_list):  # Learned to use enumerate() after a pylint warning
        title_list[word_index] = word_value[0].upper() + word_value[1:]
    
    return ' '.join(title_list)


def check_sentence_ending(sentence):
    """
    Check if a sentence ends with a period.
    
    Args:
        sentence: str - a sentence to check
        
    Returns:
        bool - True if the sentence ends with a period, False otherwise
        
    Purpose:
        Verifies proper punctuation by checking if sentences
        end with a period as required.
        
    Examples:
        >>> check_sentence_ending("Fittonia are nice")
        False
        >>> check_sentence_ending("Snails can sleep for 3 years.")
        True
    """
    return sentence[-1] == '.'


def clean_up_spacing(sentence):
    """
    Remove extra whitespace from the beginning and end of a sentence.
    
    Args:
        sentence: str - a sentence that may have extra spaces
        
    Returns:
        str - the sentence with leading and trailing whitespace removed
        
    Purpose:
        Makes the paper look professional by removing
        unnecessary spacing at the start and end of sentences.
        
    Notes:
        Had to verify that strip() removes whitespace from both ends,
        not all whitespace in the string.
        
    Examples:
        >>> clean_up_spacing("  A rolling stone gathers no moss")
        'A rolling stone gathers no moss'
        >>> clean_up_spacing("  Elephants can't jump.  ")
        "Elephants can't jump."
    """
    if sentence[0] == ' ' or sentence[-1] == ' ':  # Had to refresh on how the or operator works
        return sentence.strip()  # Had to verify strip() removes whitespace from both ends
    
    return sentence


def replace_word_choice(sentence, old_word, new_word):
    """
    Replace all instances of a word in a sentence with a new word.
    
    Args:
        sentence: str - a sentence to modify
        old_word: str - word to be replaced
        new_word: str - replacement word
        
    Returns:
        str - the sentence with all instances of old_word replaced with new_word
        
    Purpose:
        Improves the quality of writing by replacing basic words
        with more sophisticated alternatives.
        
    Notes:
        Initial approach didn't account for punctuation attached to words.
        The final solution preserves punctuation when replacing words.
        
    Examples:
        >>> replace_word_choice("Animals are cool.", "cool", "awesome")
        'Animals are awesome.'
        >>> replace_word_choice("Animals are cool.", "small", "tiny")
        'Animals are cool.'
    """
    sentence_list = sentence.split()
    
    for word_index, word_value in enumerate(sentence_list):  # Needed to learn to iterate by index and value together
        if word_value and not word_value[-1].isalnum():  # Learned how to properly boolean logic isalnum method
            punctuation = word_value[-1]
            word_without_punctuation = word_value[:-1]
            
            if word_without_punctuation == old_word:
                sentence_list[word_index] = new_word + punctuation  # Had to learn how to preserve punctuation
        else:
            if word_value == old_word:
                sentence_list[word_index] = new_word
    
    return ' '.join(sentence_list)