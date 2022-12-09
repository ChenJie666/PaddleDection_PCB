import matplotlib.pyplot as plt
import cv2

infer_img = cv2.imread("D:/ML/Project/PaddleDetection-release-2.3/output/04_missing_hole_10.jpg")
plt.figure(figsize=(15, 10))
plt.imshow(cv2.cvtColor(infer_img, cv2.COLOR_BGR2RGB))
plt.show()
