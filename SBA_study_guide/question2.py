# Create two functions one to filter the word ‘perscholas’ from
# vowels letters and the second function to filter the word ‘perscholas’ from consonants
# 	Examples:
# 	vowelfilter(“perscholas”)
# 	output:
# 	prschls
# 	consonantsfilter(“perscholas”)
# 	output:
# 	eoa

def vowel_filter(string_to_be_filtered):
    for i in string_to_be_filtered:
        if i in "aeiou":
            string_to_be_filtered = string_to_be_filtered.replace(i, '')
    return string_to_be_filtered

def consonant_filter(string_to_be_filtered):
    for i in string_to_be_filtered:
        if i not in "aeiou":
            string_to_be_filtered = string_to_be_filtered.replace(i, '')
    return string_to_be_filtered

print(vowel_filter("perscholas"))
print(consonant_filter("perscholas"))
