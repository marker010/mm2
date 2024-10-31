import pickle

lines_content = [] 

with open(r"C:\Users\13708\OneDrive\桌面\python实验三数据\红楼梦.txt", "r", encoding='gb18030') as f:
    for i in range(5):
        line = f.readline()  # 每次读取一行
        lines_content.append(line.strip())  # 去除换行符并加入列表

print(lines_content)

with open(r"C:\Users\13708\OneDrive\桌面\python 作业\实验三\红楼梦.dat", "wb") as output_file:
    for d in lines_content:
        pickle.dump(d, output_file)  # 使用正确的文件对象
    print("dat写入成功")

with open(r"C:\Users\13708\OneDrive\桌面\python 作业\实验三\红楼梦.dat", "rb") as input_file:
    end = False
    while not end:
        try:
            x = pickle.load(input_file)
            print(x)
        except:
            end = True
    print("dat已经全部解码")