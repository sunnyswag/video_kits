import re

def word_to_wordx(input_src: str) -> None:
    """用来提取txt文本中有效信息的脚本
    
    Attributes:
        input_src: 输入路径
    """
    book = []
    book_output = []
    output_src = re.findall(r"(.+?)book.txt", input_src)[0] + 'edited_book.txt'

    with open(input_src, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip("\n") # 去除换行符
            if line != "" and line[0] != "无" and line[: 5] != '2021-'\
                and line[: 4] != "笔记来自": # 去除无效的行
                if line[0] == '【': # 将以'【'开头的行取消换行
                    book[-1] += line
                else: # 去除每行开头和结尾的标点符号
                    if line[0] in ['，', '。', ',', '.', '：']:
                        line = line[1:]
                    if line[-1] in ['，', '。', ',', '.', '：']:
                        line = line[:-1]
                    book.append(line)

    for line in book:
        book_output.append(re.sub(r"【.*】", "", line))
            
    with open(output_src, "w", encoding='utf-8') as f:
        for i in range(len(book_output)):
            f.write("{}. ".format(i + 1) + book_output[i])
            f.write('\n')
    
    print("转换完成!")
    print("输出路径为: {}".format(output_src))

if __name__ == "__main__":
    word_to_wordx("./word_to_wordx/book.txt")