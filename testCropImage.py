# import cv2
# import numpy
#
# from PIL import Image
# from PIL import ImageCms
#
# # force opening truncated/corrupt image files
# from PIL import ImageFile
# import PySimpleGUI as sg
#
# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# img = Image.open(fullPath)
#                         if img.mode == "CMYK":
#                             img = ImageCms.profileToProfile(img, "USWebCoatedSWOP.icc", "sRGB_Color_Space_Profile.icm",
#                                                             outputMode="RGB")
#                         img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
#
#                         # (1) Convert to gray, and threshold
#                         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                         th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
#
#                         # (2) Morph-op to remove noise
#                         kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
#                         morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)
#
#                         # (3) Find the max-area contour
#                         cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
#                         cnt = sorted(cnts, key=cv2.contourArea)[-1]
#
#                         # (4) Crop and save it
#                         x, y, w, h = cv2.boundingRect(cnt)
#                         dst = img[y:y + h, x:x + w]
#
#                         # create/write to file
#                         cv2.imwrite(path+nameWithoutExtension+'_edited.'+extensionOfFile, dst)