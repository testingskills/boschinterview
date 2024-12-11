
## Bosch Interview Assignment
### Enviornment Setup:
```
git clone
bash setup.sh
source .venv/bin/activate
```
### EDA Assignment
```
cd EDA
python eda.py
```
### Yolov5 Model detection
```
cd yolov5
python detect.py --weights yolov5.pt --img 640 --conf 0.25 --source data/images
```
### Yolov5 Model Training
```
cd yolov5
python train.py --img 640 --batch 16 --epochs 1 --data data/bdd100k.yaml --weights yolov5.pt
