import json

three_char_particles = ["くらい", "ばかり"]
two_char_particles = ["から", "より", "まで", "だけ", "ほど", "など", "なり", "やら", "こそ", "でも", "しか", "さえ", "だに"]
one_char_particles = ["が", "の", "を", "に", "へ", "と", "で", "は", "も"]

def load_documents(file_address):
    data = []
    with open(file_address) as current_file:
        for line in current_file:
            data.append(line)
    return data

def check_particles(document, j):
    current_text = str(document["raw_text"])
    text_length = len(current_text)
    current_noun = str(document["annotations"]["key_phrase"][j]["extent"])
    if current_noun in current_text:
        print(current_noun + " is in the text") #REMOVE LATER
        char_number = int(document["annotations"]["key_phrase"][j]["end"])
        if char_number+2 < text_length:
            following_three = current_text[char_number] + current_text[char_number+1] + current_text[char_number+2]
            if following_three in three_char_particles:
                print(following_three)
                return
        if char_number+1 < text_length:
            following_two = current_text[char_number] + current_text[char_number+1]
            if following_two in two_char_particles:
                print(following_two)
                return
        if char_number < text_length:
            following_one = current_text[char_number]
            if following_one in one_char_particles:
                print(following_one)
                return

# MAIN SCRIPT STARTS HERE
file_address = "./test_SC/complete/Japanese_KP_1120_part1_SC.json"
data = load_documents(file_address)

# Iterate through each document in file
for i in range(len(data)):
    document = json.loads(data[i])

    # Skip first JSON object that's not annotations
    if "maxRead" in document:
        continue


    # Iterate through each annotation in document
    key_phrase_length = len(document["annotations"]["key_phrase"])
    for j in range(key_phrase_length):
        check_particles(document, j)
