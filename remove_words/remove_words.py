import pysrt as ps
import re

subs = ps.open("./remove_words/test.srt", encoding='utf-8')
print("subtitle length: ", len(subs))
print("first_sub: ", subs[0])

for sub in subs:
    text_tmp = sub.text
    text_tmp = re.sub('(那个|啊|呃|也是|这个|就是|的话|哈)', '', text_tmp)
    sub.text = text_tmp

subs.save('./remove_words/test_output.srt', encoding='utf-8')
