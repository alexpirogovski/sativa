import itertools


class Disk(object):
    def __init__(self, name):
        self._disk_name = name
        self._data = {}

    def populate_data(self, headers, values):
        self._data = zip(headers, values)

    def get_data(self):
        print self._disk_name
        print self._data


class IOReportsList(object):
    def __init__(self):
        self._report_list = []

    def add_report(self, report):
        self._report_list.append(report)

    @property
    def report_list(self):
        return self._report_list


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
        del line[0]
        self._disks[-1].populate_data(self._headers, line)

    def set_headers(self, l):
        self._headers = dict.fromkeys(l, None)

    def get_disks(self):
        return self._disks
