# Author: Tyler
# Purpose: Contains a function that removes punctuation from a string

import csv
import string

# Input: string
# Output: return string (without punctuation)
def remove_punctuation(str) -> str:

    charsToRemove = ".'?\":;-,–()"

    result = str
    for char in charsToRemove:
        result = result.lower().replace(char, "")

    return result


# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_string = "This, 'is'-a test string, containing punctuation."

    test_result = remove_punctuation(test_string)

    print("Puncuation removed:", test_result)