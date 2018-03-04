from svg.charts import line
from svg.charts.plot import Plot
from data_holder import *
import os, json

platform_log_dir = '/home/iguazio/igz/platform/manof/volumes/logs/platform/'
log_file = platform_log_dir + 'igz0.performance_indicators.0_info.log'
grep_line = 'Finished loop iteration'


# def my_line():
#     g = line.Line()
#     opt = dict(
#         height=100,
#         width=100,
#     )
#     g.__dict__.update(opt)
#     return g

def line_builder():
    ln = line.Line()
    options = dict(
        scale_integers=True,
        area_fill=True,
        width=1280,
        height=480,
        fields=[graph_collection['_docker_ps'].return_t()],
        graph_title='Docker Line',
        show_graph_title=True,
        no_css=False,
        right_align=False,
        show_x_labels=False,
    )
    ln.__dict__.update(options)
    ln.add_data(graph_collection['_docker_ps'].return_data_line())
    return ln


def performance_plot():
    g = Plot({
        'min_x_value': 0,
        'min_y_value': 0,
        'area_fill': True,
        'stagger_x_labels': True,
        'stagger_y_labels': True,
        'show_x_guidelines': True
    })



graph_collection = {}


def get_jsons_from_log_lines():
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


def generate_graphs():
    yield 'G', line_builder()


def save_samples():
    root = os.path.dirname(__file__)
    for sample_name, sample in generate_graphs():
        res = sample.burn()
        with open(os.path.join(root, sample_name + '.py.svg'), 'wb') as f:
            f.write(res)


if __name__ == '__main__':
    get_jsons_from_log_lines()
    for key, value in graph_collection.iteritems():
        print key
    generate_graphs()
    save_samples()
