str1 = "Hello!! how are you?"

punctuation = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"

result = ""

for char in str1:
    if char not in punctuation:
        result += char

print("Text without punctuation:", result)
