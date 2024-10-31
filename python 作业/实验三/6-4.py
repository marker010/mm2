import time

def get_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    week_day_map = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    week_day = week_day_map[current_time.tm_wday]
    print(f"当前系统时间: {formatted_time} {week_day}")

for i in range(5):
    get_time()
    time.sleep(1)