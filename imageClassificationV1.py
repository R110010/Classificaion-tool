'''
This script is a simple interactive image classification tool
where you can view and classify images interactively based on key presses.
Created By: Raj Deep Bania
'''

import os
import shutil
import cv2

source_folder = "D://Python//idClassification//Source//"
# destionation folfers 
# exampleFolder = "D://Python//idClassification//front" # front
A = "D://Python//idClassification//front" # front
B = "D://Python//idClassification//back" # Back
C = "D://Python//idClassification//other" # other
wrongKey = "D://Python//idClassification//wrongKey" # wrong key typed


files = os.listdir(source_folder)
for file in files:
    source_path = os.path.join(source_folder, file)
    img = cv2.imread(source_path)
    # Resize the image to a specific width and height
    desired_width = 1000
    desired_height = 700
    img_resized = cv2.resize(img, (desired_width, desired_height))

    # Add fixed text to the image
    text = "Press 1 for front, 2 for back, 3 for other, 4 for wrong file"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_resized, text, (10, 30), font, 1, (0, 165, 255), 2, cv2.LINE_AA)

    cv2.imshow('Resized Image', img_resized)
    inp = cv2.waitKey(0)  # Wait until a key is pressed
    print(inp)
    #(Ascii values are used)
    if inp == 49 : # for 1
        shutil.move(source_path, A)
    elif inp == 50 : # for 2
        shutil.move(source_path, B)
    elif inp == 51 : # for 3
        shutil.move(source_path, C)
    elif inp == 52 : # for 4
        shutil.move(source_path, wrongKey)        
    else : # for other file press any key
        break

cv2.destroyAllWindows()
        