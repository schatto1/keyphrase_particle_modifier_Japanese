import json

file_address = "./test_SC/complete/Japanese_KP_1120_part1_SC.json"

data = []
document = []
with open(file_address) as current_file:
    for line in current_file:
        data.append(line)

    for i in range(len(data)):
        # print("Line String:\n" + data[i])
        document = json.loads(data[i])
        # Skip first JSON object that's not annotations
        if "maxRead" in document:
            continue

        # Iterate through each document in file
        for j in range(len(document["annotations"]["key_phrase"])):
            current_text = str(document["raw_text"])
            current_noun = str(document["annotations"]["key_phrase"][j]["extent"])
            if current_noun in current_text:
                print(current_noun + " is in the text")
                char_number = int(document["annotations"]["key_phrase"][j]["end"])
                following_three = current_text[char_number] + current_text[char_number+1] + current_text[char_number+2]
                print(following_three)
        #output = json.dumps(document, indent = 2)
        #print("JSON dump:\n" + output)

#for document in data:
#    output = json.dumps(document, indent = 2)
#    print(output)
