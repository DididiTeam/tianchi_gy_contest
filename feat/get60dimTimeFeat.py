import datetime
"""
etl data to (link,startTime,endTime,time)
"""
def parse_line(s = '3377906284395510514;2016-05-21;[2016-05-21 07:06:00,2016-05-21 07:08:00);10.0'):
    arr = s.split(';')
    time_interval = arr[2].split(',')
    start_time = datetime.datetime.strptime(time_interval[0], '[%Y-%m-%d %H:%M:%S')
    end_time  = datetime.datetime.strptime(time_interval[1], '%Y-%m-%d %H:%M:%S)')
    return (arr[0] ,start_time ,end_time , float(arr[3]))






def loadData(filePath):
    with open(filePath) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    content.pop(0)
    t = list(map(parse_line,content))









if __name__ == '__main__':
    #loadData("/Users/wangxinyuan/Desktop/tianchi/gy_contest_link_traveltime_training_data.txt")


