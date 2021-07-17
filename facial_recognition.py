#%% Import Libraries
import numpy as np
import cv2

#%%
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5) # Adjust factor

    for x,y,w,h in faces:
        print(x,y,w,h)
        end_cord_x = x+w
        end_cord_y = y+h
        roi_gray = gray[y:end_cord_y, x:end_cord_x]  # Region of interest for gray (y_start-y_end)
        roi_color = frame[y:end_cord_y, x:end_cord_x] # Region of interest for color
        img_item = "my-image.png"
        cv2.imwrite(img_item,roi_gray) # Write to image

        color = (255,0,0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y), color, stroke)

    # Display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()# %%

# %%
