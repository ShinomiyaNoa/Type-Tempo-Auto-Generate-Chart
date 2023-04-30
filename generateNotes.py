import json
import random


def generateNotes(number_of_bars, to_8_16_32, randomtype):
    notes = []
    pre_pos = [-1, -1, -1]  # initialize previous position
    pre_type = -1  # initialize previous type
    pre_key = ""
    pos_2 = int(to_8_16_32)  # randomly choose pos[1] in notes
    for i in range(number_of_bars):
        while True:
            pos_1 = i
            if pos_1 != pre_pos[0]:  # start at a bar
                pos_3 = 0
            else:
                # pos_3 = random.randint(0, pos_2-1)  # randomly choose pos[2]
                if randomtype == 1:
                    pos_3 = pre_pos[2] + random.randint(1, 2)
                else:
                    pos_3 = pre_pos[2] + 1
                if pos_3 >= pos_2:
                    break
            key = random.choice(["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "Z",
                                "X", "C", "V", "B", "N", "M", ",", ".", "/", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Space"])  # randomly choose key
            if pre_type == 1:
                note_type = 2
                key = pre_key
            else:
                # randomly choose note type
                if i != number_of_bars-1:
                    note_type = random.choices(
                        [0, 1], weights=[0.9, 0.1], k=1)[0]
                else:
                    note_type = 0
            pre_pos = [pos_1, pos_2, pos_3]  # update previous position
            pre_type = note_type  # update previous type
            pre_key = key
            notes.append({"pos": pre_pos, "key": key, "type": note_type})
    return notes


# with open(f'aa.json', 'w') as f:
#     json.dump(generateNotes(100), f)
