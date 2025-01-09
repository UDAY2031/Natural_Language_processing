import re
from nltk.tokenize import word_tokenize

text = "Splitting techniques: test, compare, and analyze results."
nltk_tokens = word_tokenize(text)
split_tokens = text.split()
regex_tokens = re.split(r'\W+', text)

print("NLTK:", nltk_tokens)
print("Split:", split_tokens)
print("Regex:", regex_tokens)
