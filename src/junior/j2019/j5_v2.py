NUM_RULES = 3

def input_words():
    words = []
    for _ in range(NUM_RULES):
        rss = input().split()
        words.append((rss[0], rss[1]))
    return words

def input_steps():
    ss = input().split()
    return int(ss[0]), ss[1], ss[2]

def replace(word, x, rn):
    replacements = []
    for i in range(len(word)):
        cpos, j = i, 0
        while j < len(x) and cpos < len(word) and word[cpos] == x[j]:
            cpos, j = cpos + 1, j + 1
        if j == len(x):
            new_word = word[0:i] + worddst[rn] + word[cpos:]
            replacements.append([rn + 1, i + 1, new_word])
    return replacements

def get_dst_string(cur, cur_step, records):
    if cur_step > steps:
        return None
    
    if cur_step == steps:
        if cur == dst:
            return records
        return None
    
    if cur in visited[cur_step]:
        return None
    
    for i in range(NUM_RULES):
        replacements = replace(cur, wordsrc[i], i)
        for r in replacements:
            new_records = records.copy()
            new_records.append(r)
            visited[cur_step + 1].add(r[2])
            result = get_dst_string(r[2], cur_step + 1, new_records)
            if result is not None:
                return result
    
    return None

if __name__ == "__main__":
    wordsrc = []
    worddst = []
    visited = [set() for _ in range(steps + 1)]

    wordsrc = input_words()
    steps, src, dst = input_steps()

    result = get_dst_string(src, 0, [])

    if result is not None:
        for x in result:
            print(x[0], x[1], x[2])
