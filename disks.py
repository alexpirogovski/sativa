from data_holder import *

class Disk(object):
    def __init__(self, name):
        self._disk_name = name
        self._data = {}

    def populate_data(self, headers, values):
        self._data = zip(headers, values)

    def get_data(self):
        print self._disk_name
        print self._data

    def get_data_by_name(self, header):
        if header in self._data.keys():
            return self._data[header]
        else:
            return None


class IOReportsList(object):
    def __init__(self):
        self._report_list = []

    def add_report(self, report):
        self._report_list.append(report)

    @property
    def report_list(self):
        return self._report_list

    def get_disk_report_by_name(self, disk_name, name):
        pass
        # g = MyGraph(disk_name)
        # for report in self._report_list:
        #     for disk in report.get_disks:
        #         p = Point(report.timestamp, disk.get_data_by_name(name))
        # return g


class IOReport(object):
    def __init__(self, timestamp):
        self._disks = []
        self._timestamp = timestamp
        self._headers = {}

    @property
    def timestamp(self):
        return self._timestamp

    def add_disk(self, line):
        self._disks.append(Disk(line[0]))
        self._disks[-1].populate_data(self._headers, line[1:])

    def set_headers(self, l):
        self._headers = dict.fromkeys(l, None)

    def get_disks(self):
        return self._disks
