import datetime
import os
import random

def modify():
    file = open('qwq.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('qwq.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()

def commit():
    message = random.randint(1, 3) * "q" + random.randint(1, 9) * "w" + random.randint(1, 3) * "q"
    os.system('git commit -a -m \"'+message+'\"')

def set_sys_time(year, month, day):
    os.system('sudo date -s %04d%02d%02d' % (year, month, day))

def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()

def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        for i in range(0, random.randint(1, 9)):
            trick_commit(cur_date.year, cur_date.month, cur_date.day)

if __name__ == '__main__':
    os.system('git config --global user.email "lemonhx@lemonhx.tech"')
    os.system('git config --global user.name "lemonhx"')
    daily_commit(datetime.date(2020, 1, 1), datetime.date(2020, 9, 15))
