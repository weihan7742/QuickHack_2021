#%%
import os

class Test:
    def move_dir(self,pic_name):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        test_dir = os.path.join(BASE_DIR, r"images\test")

        og_pic_dir = os.path.join(BASE_DIR,pic_name)
        new_pic_dir = os.path.join(test_dir,pic_name)
        os.rename(og_pic_dir, new_pic_dir)

#%%
test = Test()
test.move_dir("./selfie.png")
# %%
