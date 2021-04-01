import cv2
import numpy as np

capture = cv2.VideoCapture(2)
overlay = cv2.imread('eyeball.png', -1)

def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
	bg_img = background_img.copy()
	
	if overlay_size is not None:
		img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

	b,g,r,a = cv2.split(img_to_overlay_t)
	overlay_color = cv2.merge((b,g,r))
	
	mask = cv2.medianBlur(a,5)

	h, w, _ = overlay_color.shape
	roi = bg_img[y:y+h, x:x+w]

	img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))
	img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)
	bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)
	return bg_img

while True:
    ret, image = capture.read()
    over = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    gray = cv2.medianBlur(gray, 5)
    #gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #    cv2.THRESH_BINARY,11,3.5)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10)

    if circles is not None:
        for i in circles[0,:]:
            #center = (i[0], i[1])
            radius = int(i[2]) * 2
            over = overlay_transparent(image, overlay, int(i[0] - int(i[2])), int(i[1]) - int(i[2]), (radius, radius))
            #cv2.circle(image, center, 1, (255, 0, 0), 3)
            #cv2.circle(image, center, radius, (255, 0, 255), 3)

    cv2.imshow('video', over)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break