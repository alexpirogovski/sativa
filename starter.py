#!/usr/bin/python

from data_holder import *
import json
import os
from svg.charts import time_series


platform_log_dir = '/home/iguazio/igz/platform/manof/volumes/logs/platform/'
log_file = platform_log_dir + 'igz0.performance_indicators.0_info.log'
grep_line = 'Finished loop iteration'

graph_collection = {}

with open(log_file) as f:
    for line in f:
        json_from_line = json.loads(line)
        if json_from_line['what'] == grep_line:
            timestamp = json_from_line['when']
            for key, value in json_from_line['more']['time_table'].iteritems():
                graph_name = value['indicator']
                elapsed = value['elapsed']
                if graph_name not in graph_collection.keys():
                    graph_collection[graph_name] = MyGraph(graph_name)
                new_point = Point(timestamp, elapsed)
                graph_collection[graph_name].add_point(new_point)


def graph_builder(graph):
    g = time_series.Plot({})

    g.timescale_divisions = '10 minutes'
    g.stagger_x_labels = True
    g.x_label_format = '%H:%M:%S.%f'
    g.width = 1920
    g.height = 640
    g.show_data_labels = False
    g.show_data_values = False
    g.area_fill = True
    g.add_data(graph_collection[graph].return_data_time_series())
    return g


def combined_graph_builder():
    g = time_series.Plot({})

    g.timescale_divisions = '10 minutes'
    g.stagger_x_labels = True
    g.x_label_format = '%H:%M:%S.%f'
    g.width = 1920
    g.height = 640
    g.show_data_labels = False
    g.show_data_values = False
    g.area_fill = True
    for k, v in graph_collection.iteritems():
        g.add_data(graph_collection[k].return_data_time_series())
    return g


def generate_graphs():
    for key, value in graph_collection.iteritems():
        print key
        yield key, graph_builder(key)
    yield 'Combined_graph', combined_graph_builder()


def save_samples():
    root = os.path.dirname(__file__)
    for sample_name, sample in generate_graphs():
        res = sample.burn()
        with open(os.path.join(root, sample_name + '.py.svg'), 'wb') as f:
            f.write(res)


if __name__ == '__main__':
    save_samples()
