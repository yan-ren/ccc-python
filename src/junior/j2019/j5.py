rules = []

for i in range(3):
    text = input().split()
    rules.append((text[0], text[1]))

text = input().split()
steps, src_str, dst_str = int(text[0]), text[1], text[2]

visited = [set() for _ in range(steps+1)]
result = None

def replace(word, rule_number):
    replacements = []
    rule = rules[rule_number]
    index = 0

    while index < len(word):
        index = word.find(rule[0], index, len(word))
        if index == -1:
            break
        new_word = word[0:index] + rule[1] + word[index+len(rule[0]):]
        replacements.append([rule_number + 1, index + 1, new_word])
        index += 1

    return replacements


def traverse(cur_str, cur_step, records):
    global result

    if result is not None:
        return
    
    if cur_step > steps:
        return
    
    if cur_step == steps:
        if cur_str == dst_str:
            result = records
        return
    
    if cur_str in visited[cur_step]:
        return
    
    for rule_number, _ in enumerate(rules):
        replacements = replace(cur_str, rule_number)
        for replacement in replacements:
            new_records = records.copy()
            new_records.append(replacement)
            traverse(replacement[2], cur_step+1, new_records)
            visited[cur_step+1].add(replacement[2])


traverse(src_str, 0, [])

for r in result:
    print(r[0], r[1], r[2])
