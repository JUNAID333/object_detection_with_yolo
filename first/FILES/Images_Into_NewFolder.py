import cv2

#----------------Change FolderName, min_num of the image and max_num of the image -----------------
folderName="Ai"
min_num=1061
max_num=1200


for i in range(min_num,max_num+1):
    path="E://Telugu Character Recogniton//Vowel_Dataset//"+folderName+"//"+str(i)+".jpg"
    img=cv2.imread(path,cv2.IMREAD_COLOR)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("B"+str(i),img)         # Before Resize
    #cv2.waitKey(0)
    x=28
    newimg = cv2.resize(img,(x,x))
    cv2.imshow("A"+str(i),newimg)         # After Resize
    #cv2.waitKey(0)
    cv2.imwrite("E://Telugu Character Recogniton/Resized_Vowel_Dataset//"+str(i)+".jpg",newimg)

    cv2.destroyAllWindows()
