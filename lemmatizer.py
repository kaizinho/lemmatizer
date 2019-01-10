# coding: utf-8
import re


def lemmatize(sentence, word_list):
    lemm_sentence = ""

    for word in sentence.split():
        lemm_sentence += word_list.get(word, word) + " "

    return lemm_sentence.strip()

def extract_words(raw_data_file, filename="data/swedish_words.json"):
    pattern1 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|Räkneord|Interjektion|Konjugation)===)$"
    pattern2 = r"^'''([a-zA-ZåäöÅÄÖ]+)'''$"
    pattern3 = r"^#{{böjning\|sv\|[a-zA-ZåäöÅÄÖ]+\|([a-zA-ZåäöÅÄÖ]+)}}"

    data = ""
    matching_strings = []
    counts = {
        "one": 0,
        "two": 0,
        "three": 0
    }

    with open(raw_data_file, "r") as input:
        with open(filename, "w") as output:
            output.write("{\r\n")
            for line in input:
                match1 = re.search(pattern1, line)
                match2 = re.search(pattern2, line)
                match3 = re.search(pattern3, line)

                if len(matching_strings) == 0:
                    if match1:
                        matching_strings.append(match1.group())
                        counts["one"] += 1
                elif len(matching_strings) == 1:
                    if match2:
                        matching_strings.append(match2.group(1))
                        counts["two"] += 1
                    else:
                        matching_strings = []
                elif len(matching_strings) == 2:
                    if match3:
                        data += '\t"' + matching_strings[1] + '": "' + match3.group(1) + '",\r\n'
                        counts["three"] += 1
                    matching_strings = []

            output.write(data.rstrip(',\r\n'))
            output.write("\r\n}\r\n")
