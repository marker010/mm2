import jieba

# 读取文件
with open(r"C:\Users\13708\OneDrive\桌面\python实验三数据\红楼梦.txt", encoding='gb18030', errors='ignore') as f:
    data = f.read()

# 人物列表
characters = [
    "贾演", "贾源", "贾代化", "贾代善", "贾代儒", "贾代修", "贾敷", "贾敬", 
    "贾赦", "贾政", "贾敏", "贾敕", "贾效", "贾敦", "贾珍", "贾琏", "贾琮", 
    "贾珠", "贾宝玉",'宝玉','宝二爷', "贾环", "贾瑞", "贾璜", "贾珩", "贾㻞", "贾珖", 
    "贾琛", "贾琼", "贾璘", "贾元春", "贾迎春", "贾探春", "贾惜春", 
    "喜鸾", "四姐", "贾蓉", "贾兰", "贾蔷", "贾菌", "贾芸", "贾芹", 
    "贾萍", "贾菖", "贾菱", "贾蓁", "贾藻", "贾蘅", "贾芬", "贾芳", 
    "贾芝", "贾荇", "贾芷", "贾葛", "贾巧姐","史太君", "史鼐", "史鼎", "史湘云",
    "王子腾", "王子胜", "王夫人", "薛姨妈", "王仁", "王熙凤", "薛蟠", "薛蝌", "薛宝钗", "薛宝琴",
     "林黛玉","黛玉","妙玉", "邢夫人", "尤氏", "李纨", "秦可卿", "胡氏", "许氏", 
    "香菱", "赵姨娘", "刘姥姥", "甄宝玉","袭人", "媚人", "晴雯", "绮霰", "麝月", "檀云", "秋纹", "碧浪", 
    "茜雪", "春燕", "坠儿", "四儿", "佳蕙", "抱琴", "司棋", "莲花儿", 
    "绣橘", "待书", "翠墨", "蝉姐", "入画", "彩屏", "紫鹃", "雪雁", 
    "春纤", "鸳鸯", "琥珀", "珍珠", "玻璃", "翡翠", "鹦鹉", "靛儿", 
    "傻大姐", "银蝶", "炒豆儿", "卐儿", "莺儿", "文杏", "平儿", "小红", 
    "丰儿", "金钏", "玉钏", "绣鸾", "绣凤", "彩云", "彩霞", "素云", 
    "同喜", "同贵", "缕儿", "翠缕", "宝珠", "瑞珠", "姣杏", "小螺", 
    "善姐", "臻儿", "篆儿", "小吉祥儿", "小鹊", "小舍儿", "宝蟾","茗烟", "焦大", "李贵", "锄药", "墨雨", "伴鹤", "扫花", "引泉"
]

# 分词
words = jieba.lcut(data)
print("词汇拆解完成")

# 统计人物出现次数
counts = {}
for word in words:
    if len(word) == 1:  # 忽略单字词
        continue
    if word in characters:  # 只统计人物名字
        if word == "贾宝玉" or word == "宝玉" or word == "宝二爷":
            word = '贾宝玉'
        elif word == "林黛玉" or word == "黛玉":
            word = "林黛玉"
        counts[word] = counts.get(word, 0) + 1

# 排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

with open(r"C:\Users\13708\OneDrive\桌面\python 作业\实验三\红楼梦结果.txt", "w", encoding='utf-8') as output_file:
    for i in range(20):
        word, count = items[i]
        output_file.write(f"{i + 1} {word} {count}\n")

print("结果已输出到红楼梦结果.txt")