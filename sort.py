from collections import defaultdict

#default dict of coach names and strings to catch them
from names_lists import names_dict

names_rev = {}
for name, nickname in names_dict.items():
    for nickname in nickname:
        names_rev[nickname] = name

with open('output_files/output_comments.txt', 'r', encoding='utf-8') as in_file, \
     open('output_files/found_names.txt', 'w', encoding='utf-8') as out_file:
    #TODO this is an issue cause its treating each line as a new comment
    for line in in_file:
        for name, nicknames in names_dict.items():
            for nickname in nicknames:
                if nickname in line:
                    out_file.write(f"{name}: {line}")
                    break
