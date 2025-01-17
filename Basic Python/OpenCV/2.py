import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from PIL import Image

data_path = 'faces/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

training_data, Labels = [], []

for i,files in enumerate(onlyfiles):
    print(i,files)
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    training_data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()



model.train(np.asarray(training_data),np.asarray(Labels))

print(model)

print("Model Training Complete !!!")
