import cv2
import os


def net(img_name, w_h, front_size):
	line_color = (105, 105, 105)
	front_color = (255, 255, 0)

	img = cv2.imread(img_name)

	imginfo = img.shape
	h = imginfo[0]
	w = imginfo[1]

	dst_h = w_h
	dst_w = w_h

	h_num = h // dst_h 	
	w_num = w // dst_w	
	
	front_type = cv2.FONT_HERSHEY_SIMPLEX
	
	for h in range(h_num):
		for w in range(w_num):
			# (left, upper, right, lower)
			img_part = (w*dst_w, h*dst_h, (w+1)*dst_w, (h+1)*dst_h)
			x, y, x_w, y_h = img_part			
			cv2.rectangle(img, (x, y), (x_w, y_h), line_color, 1)
			index = str(h+1) + ':' + str(w+1)			
			cv2.putText(img, index, (x, y_h-5), front_type, front_size, front_color, 1)
	
	filename = str(dst_h)+'.jpg'
	print(filename)
	cv2.imwrite(filename, img)
	win_name = 'img'
	# cv2.imshow(win_name, img)
	if cv2.waitKey() == ord('q'):
		cv2.destroyAllWindows()


if __name__ == '__main__':
	img_name = ['LENW045.JPG'] * 6
	w_h_list = [i for i in range(60, 170, 20)]
	front_size_list = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
	list(map(net, img_name, w_h_list, front_size_list))
	
