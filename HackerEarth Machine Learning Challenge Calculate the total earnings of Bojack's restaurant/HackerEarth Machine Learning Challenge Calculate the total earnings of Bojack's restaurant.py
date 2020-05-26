import cv2
from matplotlib import pyplot as plt
from keras.preprocessing.image import img_to_array,load_img
import re
import pdf2image
from pytesseract import image_to_string,image_to_data
import pandas as pd
from pdf2image import convert_from_path
from PIL import Image
from pytesseract import Output
from matplotlib.patches import Rectangle


test=pd.read_csv('/content/Test.csv')
for i in range(131,201):
  pages = convert_from_path('/content/TE_'+str(i)+'.pdf')
  for page in pages:
    page.save('/content/TE_'+str(i)+'jpg', 'JPEG')
def image_preprocessing(path):
  img = cv2.imread(path,0)
  img = cv2.medianBlur(img,5)

  ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
  th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

  titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
  images = [img, th1, th2, th3]

  for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
  new_image=images[3]
  return new_image
new_image=image_preprocessing('/content/TE_132jpg')   #Example for showing how the image is being transfrormed for better results
image_to_string(new_image)

"""Setting 400 dpi"""

for i in range(131,201):
  im = Image.open('/content/TE_'+str(i)+'jpg')
  im.save('/content/TE_'+str(i)+'jpg.jpeg',dpi=(400,400))

"""Extracting text from data"""

from PIL import Image
from matplotlib import pyplot
from pytesseract import image_to_string
from keras.preprocessing.image import load_img
l_test=[]
for i in range(131,201):
  custom_config = r'-c tessedit_char_whitelist=subtotalSUBTOTAL$0123456789.: --psm 6'
  image=load_img('/content/TE_'+str(i)+'jpg.jpeg')
  text=image_to_string(image,config=custom_config)
  l_test.append(text)
l_test

"""Filling the empty sequences"""

k=[]
for i in range(len(l_test)):
  if l_test[i]=='':
    filename='/content/TE_'+str(131+i)+'jpg.jpeg'
    image=image_preprocessing(filename)           #Using image_preprocessing function to remove background noise resulting in better pytesseract accuracy
    l_test[i]=image_to_string(image)
    k.append(l_test[i])
l_test

"""Searching terms like total,subtotal and amount that may contain the total amount"""

k=[]
for i in l_test:
  k.append(i.split('\n'))
k
for i in k:
  j=0
  while j<len(i):
      result1=re.search(r"subtotal", i[j].lower())
      result2=re.search(r"total", i[j].lower())
      result3=re.search(r"amount", i[j].lower())
      result4=re.search(r"cash", i[j].lower())
      if result1==None and result2==None and result3==None:
        i.pop(j)
      else:
        j=j+1
k
final=[]
for i in range(len(k)):
  for_this=[]
  for j in range(len(k[i])):
    result=re.findall("\d+\.\d+",k[i][j])     
    if len(result)>0:
      for_this.append(float(result[0]))
  if len(for_this)==0:
    final.append(0)
  else:
    final.append(max(for_this))               
final
for i in range(len(final)):
  if final[i]==0:
    final[i]=sum(final)/len(final)
final


import csv
with open('predictions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FileName','Total Amount'])
    for i in range(len(list(final))):
        writer.writerow([test["FileName"][i],final[i]])