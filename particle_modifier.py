import json

three_char_particles = ["くらい", "ばかり"]
two_char_particles = ["から", "より", "まで", "だけ", "ほど", "など", "なり", "やら", "こそ", "でも", "しか", "さえ", "だに"]
one_char_particles = ["が", "の", "を", "に", "へ", "と", "で", "は", "も"]
common_mistakes = ["ですが", "もしく", "です", "とって", "にて", "でした", "では"]

start_file = 1
end_file = 40

def load_documents(file_address):
    data = []
    with open(file_address) as current_file:
        for line in current_file:
            data.append(line)
    return data #string

def append_to_file(file_address, document):
    with open(file_address, "a", encoding="utf8") as outfile:
        json.dump(document, outfile, ensure_ascii=False)
        outfile.write("\n")

def check_particles(document, j):
    #Returns a dictionary
    current_text = str(document["raw_text"])
    text_length = len(current_text)
    current_noun = str(document["annotations"]["key_phrase"][j]["extent"])
    if current_noun in current_text:
        char_number = int(document["annotations"]["key_phrase"][j]["end"])
        if char_number+2 < text_length:
            following_three = current_text[char_number] + current_text[char_number+1] + current_text[char_number+2]
            if following_three in common_mistakes:
                return document
            elif following_three in three_char_particles:
                return modify_keyphrase(document, j, current_noun, char_number, following_three, 3)
        if char_number+1 < text_length:
            following_two = current_text[char_number] + current_text[char_number+1]
            if following_two in common_mistakes:
                return document
            elif following_two in two_char_particles:
                return modify_keyphrase(document, j, current_noun, char_number, following_two, 2)
        if char_number < text_length:
            following_one = current_text[char_number]
            if following_one in one_char_particles:
                return modify_keyphrase(document, j, current_noun, char_number, following_one, 1)
    return document #Noun not in text or no particle found; return original dict

def modify_keyphrase(document, j, current_noun, char_number, following_text, number):
    document["annotations"]["key_phrase"][j]["extent"] = current_noun + following_text
    document["annotations"]["key_phrase"][j]["end"] = char_number + number
    return document #dict

def main(file_address, output_address):
    # MAIN SCRIPT STARTS HERE
    data = load_documents(file_address)
    open(output_address, "w").close()

    # Iterate through each document in file
    for i in range(len(data)):
        document = json.loads(data[i])

        # Skip first JSON object that's not annotations
        if "maxRead" in document:
            append_to_file(output_address, document)
            continue

        # Iterate through each annotation in document
        key_phrase_length = len(document["annotations"]["key_phrase"])
        for j in range(key_phrase_length):
            document = check_particles(document, j)
        append_to_file(output_address, document)

for count in range(start_file, end_file):
    file_address = "./test_SC/complete/Japanese_KP_1120_part" + str(count) + "_SC.json"
    output_address = "./test_SC/fixed/Japanese_KP_1120_part" + str(count) + "_SC.json"
    main(file_address, output_address)
