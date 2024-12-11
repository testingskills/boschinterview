"""
Run EDA on Input JSON.
Usage - formats:
    $ python eda.py                 
"""


import json
from plotting import Plotting
import argparse

def main(opt):
    """
    Parse command-line arguments for EDA and plot graphs of various distributions after JSON processing.

    Args:
        known (bool, optional): If True, parses known arguments, ignoring the unknown. Defaults to False.

    Returns:
        None

    Example:
        ```python
        from ultralytics.yolo import parse_opt
        opt = parse_opt()
        print(opt)
        ```
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    parser.add_argument( '-f', '--file', help='JSON input file',type=argparse.FileType('r'),
)
    train = open(args.file.name)
    train_label_file = json.load(train)
    print(len(train_label_file))

    single_dict = {'weather': {}, 'scene': {}, 'timeofday': {}}
    truncated_dict = {'truncated': 0, 'not_truncated': 0}
    occlusion_dict = {'occluded': 0, 'not_occluded': 0}
    box_plot_dict = {}
    weather = set()
    scene = set()
    timeofday = set()
    labels = set()

    for file in train_label_file:
        attrb = file['attributes']
        weather.add(attrb['weather'])
        scene.add(attrb['scene'])
        timeofday.add(attrb['timeofday'])

        if attrb['weather'] not in single_dict['weather']:
            single_dict['weather'][attrb['weather']] = {}
            single_dict['weather'][attrb['weather']]['total'] = 1
        else:
            single_dict['weather'][attrb['weather']]['total'] += 1

        if attrb['timeofday'] not in single_dict['timeofday']:
            single_dict['timeofday'][attrb['timeofday']] = {}
            single_dict['timeofday'][attrb['timeofday']]['total'] = 1
        else:
            single_dict['timeofday'][attrb['timeofday']]['total'] += 1
        
        if attrb['scene'] not in single_dict['scene']:
            single_dict['scene'][attrb['scene']] = {}
            single_dict['scene'][attrb['scene']]['total'] = 1
        else:
            single_dict['scene'][attrb['scene']]['total'] += 1

        for label in file['labels']:
            if label['category'] == 'lane' or label['category'] == 'drivable area':
                continue        
            if label['attributes']['occluded']:
                occlusion_dict['occluded'] += 1
            else:
                occlusion_dict['not_occluded'] += 1
            
            if label['attributes']['truncated']:
                truncated_dict['truncated'] += 1
            else:
                truncated_dict['not_truncated'] += 1

            labels.add(label['category'])

            if label['category'] in box_plot_dict:
                box_plot_dict[label['category']].append(
                    abs(label['box2d']['x1']-label['box2d']['x2'])*
                    abs(label['box2d']['y1']-label['box2d']['y2'])
                    )
            else:
                box_plot_dict[label['category']] = [
                    abs(label['box2d']['x1']-label['box2d']['x2'])*
                    abs(label['box2d']['y1']-label['box2d']['y2'])
                ]

            if label['category'] in single_dict['weather'][attrb['weather']]:
                single_dict['weather'][attrb['weather']][label['category']] += 1
            else:
                single_dict['weather'][attrb['weather']][label['category']] = 1
            
            if label['category'] in single_dict['timeofday'][attrb['timeofday']]:
                single_dict['timeofday'][attrb['timeofday']][label['category']] += 1
            else:
                single_dict['timeofday'][attrb['timeofday']][label['category']] = 1
            
            if label['category'] in single_dict['scene'][attrb['scene']]:
                single_dict['scene'][attrb['scene']][label['category']] += 1
            else:
                single_dict['scene'][attrb['scene']][label['category']] = 1
            

    # Distribution of instances in whole dataset
    plot_dict = {}
    for cls in single_dict['timeofday']:
        for ins in labels:
            if ins not in plot_dict:
                plot_dict[ins] = 0
            if ins not in single_dict['timeofday'][cls]:
                continue
            plot_dict[ins] += single_dict['timeofday'][cls][ins]


    plot1 = Plotting()
    plot1.add_plot(plot_dict, 'Distribution of instances in whole dataset') 

    # Distribution of weather

    plot_dict = {}
    for cls in single_dict['weather']:
        if cls not in plot_dict:
            plot_dict[cls] = 0
        if cls not in single_dict['weather']:
            continue
        plot_dict[cls] += single_dict['weather'][cls]['total']


    plot2 = Plotting()
    plot2.add_plot(plot_dict, 'Distribution of weather') 

    # Distribution of scene

    plot_dict = {}
    for cls in single_dict['scene']:
        if cls not in plot_dict:
            plot_dict[cls] = 0
        if cls not in single_dict['scene']:
            continue
        plot_dict[cls] += single_dict['scene'][cls]['total']


    plot3 = Plotting()
    plot3.add_plot(plot_dict, 'Distribution of Scene') 


    # Distribution of time of day

    plot_dict = {}
    for cls in single_dict['timeofday']:
        if cls not in plot_dict:
            plot_dict[cls] = 0
        if cls not in single_dict['timeofday']:
            continue
        plot_dict[cls] += single_dict['timeofday'][cls]['total']


    plot4 = Plotting()
    plot4.add_plot(plot_dict, 'Distribution of time of day')


    plot5 = Plotting()
    plot5.add_plot(truncated_dict, 'Distribution of Truncated')


    plot6 = Plotting()
    plot6.add_plot(occlusion_dict, 'Distribution of Occlusion')

    plot7 = Plotting()
    plot7.add_box_plot(box_plot_dict, 'Distribution of Bbox area for each class')

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
    
