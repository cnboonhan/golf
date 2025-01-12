# golf

## Install dependencies
```
sudo apt install libgl1 -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Image Capture
```
```

## Image Segmentation
```
cd image_segmentation

# Prepare dataset
cd data
gdown 1_freQwcmT6FZqqWjasofRsZlECySeM0p
unzip "Golf Club Detection.zip" -d coco
python3 general_json2yolo.py 
cd ..

# Train model
python3 main.py
```
