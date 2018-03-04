from disks import *
import re
from datetime import datetime


def is_empty(l):
    if len(l) == 0:
        return True
    else:
        return False


def split_line(l):
    return re.compile('\w+').findall(l)


def is_timestamp(l):
    try:
        datetime.strptime(l.strip(), '%m/%d/%Y %H:%M:%S %p')
    except ValueError:
        return False
    else:
        return True


def is_headers(l):
    if split_line(l)[0] == 'Device':
        return True
    else:
        return False


def is_garbage(l):
    if split_line(l)[0] == 'Linux' or len(l) == 0:
        return True
    else:
        return False


class LogReader(object):
    def __init__(self, log_file):
        self._log_file = log_file

    def read_report(self, l):
        pass

    def parse(self):
        report_list = IOReportsList()
        current_report = None

        with open(self._log_file) as f:
            for line in f:
                line = line.strip()
                if not is_empty(line):
                    if is_timestamp(line):
                        current_report = IOReport(line)
                        report_list.add_report(current_report)
                    elif is_garbage(line):
                        current_report = None
                    elif is_headers(line):
                        l = split_line(line)
                        del l[0]
                        current_report.set_headers(l)
                    else:
                        current_report.add_disk(split_line(line))
            return report_list


if __name__ == '__main__':
    log_file = 'small_iostat_sample.txt'
    my_report = IOReportsList(LogReader(log_file).parse())
    stam = my_report.report_list
    my_report.trrrrr()
    # for r in my_report.report_list:
    #     print r.timestamp


