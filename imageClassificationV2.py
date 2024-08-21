'''
This script is a simple interactive image classification tool
where you can view and classify images interactively based on key presses.
Created By: Raj Deep Bania
modified : 25/04\2024 (undo function added)
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
D = "D://Python//idClassification//wrongKey" # EXTRA
length = len(os.listdir(source_folder))
while length > 0 :   
        files = os.listdir(source_folder)
        for file in files:
            source_path = os.path.join(source_folder, file)
            img = cv2.imread(source_path)
            # Resize the image to a specific width and height
            desired_width = 1200
            desired_height = 700
            img_resized = cv2.resize(img, (desired_width, desired_height))

            # Add fixed text to the image
            text = "Press 1 for front, 2 for back, 3 for other, 4 for wrong file"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_resized, text, (10, 30), font, 1, (0, 165, 255), 2, cv2.LINE_AA)

            cv2.imshow('Resized Image', img_resized)
            length = len(os.listdir(source_folder))
            print("final length = " ,length)
            inp = cv2.waitKey(0)  # Wait until a key is pressed
            print(inp)
            #(Ascii values are used)
            if inp == 122 or inp == 90: # (to undo press lowercase z)
                shutil.move(moved_path,source_folder)
                continue
            elif inp == 49 : # for 1
                shutil.move(source_path, A)
                moved_path = os.path.join(A,file)
            elif inp == 50 : # for 2
                shutil.move(source_path, B)
                moved_path = os.path.join(B,file)
            elif inp == 51 : # for 3
                shutil.move(source_path, C)
                moved_path = os.path.join(C,file)
            elif inp == 52 : # for 4
                shutil.move(source_path, D) 
                moved_path = os.path.join(D,file)       
            else : # PRESS ANY OTHER KEY TO BREAK THE LOOP
                break
            
else :
    cv2.destroyAllWindows()
        