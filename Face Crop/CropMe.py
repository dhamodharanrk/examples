__author__ = 'dhamodharan.k'
import cv2
import glob
import os
from PIL import Image,ImageEnhance,ImageFilter


def imgCrop(image, cropBox, boxScale=1.0):
    xDelta=max(cropBox[2]*(boxScale-1),0)
    yDelta=max(cropBox[3]*(boxScale-1),0)
    PIL_box=[cropBox[0]-xDelta, cropBox[1]-yDelta, cropBox[0]+cropBox[2]+xDelta, cropBox[1]+cropBox[3]+yDelta]
    return image.crop(PIL_box)

current_path =  os.getcwd()
face_cascade = cv2.CascadeClassifier(current_path + '\\\haarcascades\\haarcascade_frontalface_alt.xml')
all_files = glob.glob(current_path + "\\ImageToDetect" + "\\*.jpg")
for names in all_files:
    name_chunk = str(names).split("\\")[-1].split('.')
    file_name,ext = name_chunk[0],".{}".format(name_chunk[1])
    pil_im = Image.open(names)
    img = cv2.imread(names)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cropped = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    croppedImage = imgCrop(pil_im, faces[0], boxScale=1.2)
    wpercent = (300 / float(croppedImage.size[0]))
    hsize = int((float(croppedImage.size[1]) * float(wpercent)))
    resized = croppedImage.resize((300, hsize), Image.ANTIALIAS)
    enhancer = ImageEnhance.Sharpness(resized)
    enhanced = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Color(enhanced)
    enhanced = enhancer.enhance(1.3)
    enhanced.filter(ImageFilter.UnsharpMask())
    enhanced.save(current_path + "\\Detected Images\\"+ file_name + "_croped" + ext)

    height, width, depth = img.shape
    imgScale = 1000 / width
    newX, newY = img.shape[1] * imgScale, img.shape[0] * imgScale
    newimg = cv2.resize(img, (int(newX), int(newY)))
    cv2.imwrite(current_path + "\\Detected Images\\" + file_name + ext ,img)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()