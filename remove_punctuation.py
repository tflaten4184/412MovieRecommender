# Author: Tyler
# Purpose: Contains a function that removes punctuation from a string

import csv
import re
import string

# Input: string
# Output: return string (without punctuation)
def remove_symbols(str) -> str:

    result = re.sub(r'[^A-Za-z0-9 ]+', '', str)

    return result


# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_string = "This, 'is' -a test string, containing punctuation."

    test_result = remove_symbols(test_string)

    print("Punctuation removed:", test_result)