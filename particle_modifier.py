import json

file_address = "./test_SC/complete/Japanese_KP_1120_part1_SC.json"

data = []
document = []
with open(file_address) as current_file:
    for line in current_file:
        data.append(line)

    for i in range(len(data)):
        print("Line String:\n" + data[i])
        document = json.loads(data[i])
        if "maxRead" in document:
            continue
        print("Raw Text:\n" + document["raw_text"])
        #output = json.dumps(document, indent = 2)
        #print("JSON dump:\n" + output)

#for document in data:
#    output = json.dumps(document, indent = 2)
#    print(output)
