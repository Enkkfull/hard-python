from prettytable import PrettyTable

# First we think about the inputs

table = PrettyTable()
table.field_names = ["Qualcosaltro", "#"]

words_list = []
comma = ","
marks = ["!", ".", "?"]

# Ask words 
word = input("Insert first word: ")

while word != "stop": 
    words_list.append(word)
    word = input("Insert another word: ")

words_list = ["hello", ",", "I", "am", "G", "!", "and", "you", "amigo","?"]

#generating the sentences list
sentence = ""
sentence_joint = []

for element in words_list:
    if element in marks:
        sentence = sentence.strip()
        sentence = sentence.replace(sentence[0], sentence[0].upper(), 1)
        sentence_joint.append(sentence + element)
        
        sentence = ""
    elif element == comma:
        sentence += comma
    else:
        sentence += " " + element 

#add trailing sentence
if sentence != "":
    sentence = sentence.strip()
    sentence = sentence.replace(sentence[0], sentence[0].upper(), 1)
    sentence_joint.append(sentence)

full_sentences = "\n".join(sentence_joint)

# print sentence
print(full_sentences)

#statistics
#number of words
only_words = []

for word in words_list:
    if word not in marks and word != comma:
        only_words.append(word)

# this could also have been made with a list comprehension, that can be learnt in lesson 4
# as an example:
# only_words = [word for word in words_list if word not in marks and word != comma]

table.add_row(["Total number of words given: ", len(only_words)])
table.add_row(["Number of marks: ", len(words_list)-len(only_words)])
table.add_row(["Number of marks: ", len(sentence_joint)])


#finding most and least frequent character
letters_dict = {}
for char in full_sentences.lower():
    if char not in ["\n", " "]:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1

 #table.add_row(["Following the most and least frequent character: ", letters_dict])

max_char_count = max(letters_dict.values())
min_char_count = min(letters_dict.values())

max_chars = []
min_chars = []

for k, v in letters_dict.items():
    if v == max_char_count:
        max_chars.append(k)
    if v == min_char_count:
        min_chars.append(k)

table.add_row(["The most frequent ({}) character/s: ".format(max_char_count), ", ".join(max_chars)])
table.add_row(["The least frequent ({}) character/s: ".format(min_char_count), ", ".join(min_chars)])

print(table)
