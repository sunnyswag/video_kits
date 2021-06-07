book = []
with open("./word_to_wordx/book.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip("\n")
        if line != "" and line[0] != "无" and line[: 5] != '2021-'\
            and line[: 4] != "笔记来自":
            book.append(line)

with open("./word_to_wordx/book_edited.txt", "w", encoding='utf-8') as f:
    for i in range(len(book)):
        f.write("{}.".format(i + 1) + book[i])
        f.write('\n')
            