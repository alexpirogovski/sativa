import os
import re
from dateutil.parser import parse
from datetime import datetime


# class IOReport(object):
#     def __init__(self):
#         self._data = {}




if __name__ == '__main__':
    log = 'small_iostat_sample.txt'
    # timestr = '02/27/2018 12:41:39 PM'
    headers = ''

    with open(log) as f:
        # Start creating an object

        for line in f:
            try:
                datetime.strptime(line.strip(), '%m/%d/%Y %H:%M:%S %p')
            except ValueError:
                s = re.compile('\w+').findall(line)
                print s
                if not s or s[0] == 'Linux':
                    pass
            else:
                # print('Found a timestamp')
                print line.strip()
