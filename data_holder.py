class Point(object):
    def __init__(self, t, y):
        self._y = y
        self._t = t

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value


class MyGraph(object):
    def __init__(self, name=''):
        self._list = []
        self._name = name

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        self._list = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_point(self, point):
        self._list.append(point)

    def return_data_time_series(self):
        g = {'title': self._name, 'data': []}
        g['title'] = self._name
        for p in self._list:
            g['data'].append(p.t)
            g['data'].append(p.y)
        return g

    def return_data_line(self):
        g = {'title': self._name, 'data': []}
        g['title'] = self._name
        for p in self._list:
            g['data'].append(p.y)
        return g

    def return_t(self):
        return [str(p.t) for p in self._list]

    def return_y(self):
        return [p.y for p in self._list]







