import json
from PIL import Image

train_image_load = 'dataset/bdd100k/images/100k/train/'
val_image_load = 'dataset/bdd100k/images/100k/val/'

train_labels_load = 'dataset/bdd100k/labels/100k/train/'
val_labels_load = 'dataset/bdd100k/labels/100k/val/'


train_json_load = 'dataset/bdd100k/bdd100k_labels_images_train.json'
val_json_load = 'dataset/bdd100k/bdd100k_labels_images_val.json'

main_file = open("dataset/bdd100k/trainbdd100k.txt", "w")

category = {'traffic light': 0, 'traffic sign': 1, 'car': 2, 'person': 3, 'bus': 4, 'truck': 5, 'rider': 6, 'bike': 7, 'motor': 8, 'train': 9}
cat_no = -1
json_label_file = json.load(open(train_json_load))

for file in json_label_file:
    main_file.write(train_image_load + file['name'] + '\n')

    img = Image.open(train_image_load + file['name'])
    w,h = img.size

    label_file = open(train_labels_load + file['name'].split('.')[0] + '.txt', 'w')

    for label in file['labels']:
        if label['category'] == 'lane' or label['category'] == 'drivable area':
            continue
        
        if label['category'] not in category:
            cat_no += 1
            category[label['category']] = cat_no
        
        x1 = float(label['box2d']['x1'])
        x2 = float(label['box2d']['x2'])
        y1 = float(label['box2d']['y1'])
        y2 = float(label['box2d']['y2'])

        label_file.write(str(category[label['category']]) 
                        + ' ' 
                        + str((x1+x2)/(2*w))
                        + ' '
                        + str((y1+y2)/(2*h))
                        + ' '
                        + str(abs(x2-x1)/w)
                        + ' '
                        + str(abs(y2-y1)/h)
                        + '\n'
                        )
    label_file.close()
main_file.close()

main_file = open("dataset/bdd100k/valbdd100k.txt", "w")

json_label_file = json.load(open(val_json_load))

for file in json_label_file:
    main_file.write(val_image_load + file['name'] + '\n')

    img = Image.open(val_image_load + file['name'])
    w,h = img.size

    label_file = open(val_labels_load + file['name'].split('.')[0] + '.txt', 'w')

    for label in file['labels']:
        if label['category'] == 'lane' or label['category'] == 'drivable area':
            continue
        
        if label['category'] not in category:
            cat_no += 1
            category[label['category']] = cat_no
        
        x1 = float(label['box2d']['x1'])
        x2 = float(label['box2d']['x2'])
        y1 = float(label['box2d']['y1'])
        y2 = float(label['box2d']['y2'])

        label_file.write(str(category[label['category']]) 
                        + ' ' 
                        + str((x1+x2)/(2*w))
                        + ' '
                        + str((y1+y2)/(2*h))
                        + ' '
                        + str(abs(x2-x1)/w)
                        + ' '
                        + str(abs(y2-y1)/h)
                        + '\n'
                        )
    label_file.close()
main_file.close()

print(category)



