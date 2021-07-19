#%%
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images","iu")
root, dirs, files = next(os.walk(image_dir))
print(len(files))
# %%
