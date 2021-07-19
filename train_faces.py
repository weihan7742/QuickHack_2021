#%% Import libraries
import os
from PIL import Image # pip install pillow --upgrade 
import numpy as np
import cv2 # pip install opencv-contrib-python --upgrade
import pickle 

class Train: 
    def training(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []
        #%% Crawl through each image in the photo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        for root, dirs, files in os.walk(image_dir): # Directory
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root,file)
                    label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower() # Label each as directory

                    # Create a unique label
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1

                    id = label_ids[label]

                    pil_image = Image.open(path).convert("L") # Turns into grayscale
                    size = (550,550) 
                    final_image = pil_image.resize(size,Image.ANTIALIAS) # Resize to be more accurate
                    image_array = np.array(pil_image,"uint8") # Turn image into numpy array
                    faces = face_cascade.detectMultiScale(image_array) # Adjust factor

                    for x,y,w,h in faces:
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(id)
        # %%
        with open("labels.pkl", 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train,np.array(y_labels))
        recognizer.save("trainer.yml")
# %%
Train().training()