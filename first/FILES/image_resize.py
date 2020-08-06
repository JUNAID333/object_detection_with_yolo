import cv2

img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow("before Resize",img)
cv2.waitKey(0)

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
cv2.imshow("In GrayScale",img)
cv2.waitKey(0)

x=28
newimg = cv2.resize(img,(x,x))
cv2.imshow("28X28",newimg)
print(newimg.shape)
cv2.waitKey(0)
cv2.imwrite("rimg1.jpg",newimg)
cv2.destroyAllWindows()
