"""
Script for capturing images with a Basler camera. Images are
saved and new folders are created with simple keyboard commands.
"""

from os import makedirs
import cv2
from pypylon import pylon
from os.path import join, exists

# Creating the camera instance and opening it
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

# Setting the exposute time
exp_time = 100
camera.ExposureTimeAbs.SetValue(exp_time)

# Checking the image width
new_width = camera.Width.GetValue() - camera.Width.GetInc()
if new_width >= camera.Width.GetMin():
    camera.Width.SetValue(new_width)

# Initializing the variables
crosshair = False # if the crosshair is on
saving = False # if the image was just saved
img_idx = 0 # the index of the saved image
obj_idx = 1 # the index of the folder the images are saved to
subf_stem = "osa" # the stem of the folder name
len_img_num_str = 4 # the number of decimals in the image name 
len_obj_num_str = 2 # the number of decimals in the subfolder name
savepath = r"C:\Users\k5000582\OneDrive - Epedu O365\LAAKI\mittaus\osat"
img_ext = ".jpg" # the format of saved images
wait_time = 100 # the waiting time between the images in milliseconds

# Staring grabbing images
camera.StartGrabbing()

# As long as the camera is grabbing, reading images one by one from it
while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Reading the image data, scaling it down to fit the screen and showing
        # the preview image
        img = grabResult.Array
        height, width = img.shape
        scale = 600/height
        preview_img = cv2.resize(img, None, fx=scale, fy=scale)

        # If the crosshair is on, drawing a green crosshair
        if crosshair:
            preview_img = cv2.cvtColor(preview_img, cv2.COLOR_GRAY2BGR)
            H, W, _ = preview_img.shape
            preview_img[round(H/2)-1:round(H/2)+1, :] = (0, 255, 0)
            preview_img[:, round(W/2)-1:round(W/2)+1] = (0, 255, 0)

        # Flashing the image borders after the image has been saved
        if saving:
            preview_img[:10, :] = 255
            preview_img[-10:, :] = 255
            preview_img[:, :10] = 255
            preview_img[:, -10:] = 255
            saving = False
        cv2.imshow("kuva", preview_img)

        # q = quit
        k = cv2.waitKey(1)
        if k == ord("q"):
            print("User quitted. Bye!")
            break
        
        # c = crosshair on/off
        elif k == ord("c"):
            crosshair = not crosshair
        
        # +/- = increase/decrease exposure time by 100 us
        elif k == ord("+") or k == ord("-"):
            if k == ord("+"):
                exp_time += 100
            else:
                if exp_time > 100:
                    exp_time -= 100
            camera.ExposureTimeAbs.SetValue(exp_time)
            print(f"Exposure time set to {exp_time}.")
        
        # n = initialize new folder (increase folder index)
        elif k == ord("n"):
            obj_idx += 1
            img_idx = 0
            print(f"New folder initialized with index {obj_idx}.")
        
        # s = save image (and increase image index)
        elif k == ord("s"):
            # Creating the image name, e.g. 0012.jpg
            img_idx_str = str(img_idx)
            num_str = (len_img_num_str - len(img_idx_str)) \
                * "0" + img_idx_str 
            img_name = num_str + img_ext
            
            # Creating the subfolder name, e.g. holkki03
            obj_idx_str = str(obj_idx)
            num_str = (len_obj_num_str - len(obj_idx_str)) \
                * "0" + obj_idx_str
            subf_name = subf_stem + num_str
            
            fullf_name = join(savepath, subf_name)
            img_path = join(fullf_name, img_name)

            if not exists(fullf_name):
                makedirs(fullf_name)
            
            cv2.imwrite(img_path, img)
            print(f"image {img_path} saved!")
            img_idx += 1
            saving = True

    grabResult.Release()
camera.Close()
