# Author: Jacob
# Purpose: Removes stopwords from a string

import csv
import string
from nltk.corpus import stopwords

# Input: string
# Output: return string (without punctuation)
def remove_stopwords(str) -> str:

    stop = stopwords.words('english')

    new_desc = [word for word in str.split() if word not in stop]

    result = (" ").join(new_desc)

    return result


# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_string = "This is a string that contains some stop words."

    test_result = remove_stopwords(test_string)

    print("Stopwords removed:", test_result)