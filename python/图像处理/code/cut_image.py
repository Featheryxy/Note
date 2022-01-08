import cv2
import os


class CutImage:
	def __init__(self, input_dir, out_dir, dst_w, dst_h, front_size=1):
		self.input_dir = input_dir
		self.out_dir =  out_dir
		self.dst_w = dst_w
		self.dst_h = dst_w
		self.front_size = front_size
		if not os.path.exists(self.out_dir):	
			os.makedirs(self.out_dir)
	
	
	def get_nums(self):
		img = cv2.imread(self.input_dir)
		imginfo = img.shape
		height = imginfo[0]
		width = imginfo[1]
		h_nums = height // self.dst_h 	
		w_nums = width // self.dst_w	
		return h_nums, w_nums
	
	
	def get_img_box(self):
		img_box = []
		h_nums, w_nums = self.get_nums()
		
		for h_num in range(h_nums):
			for w_num in range(w_nums):
				# (left, upper, right, lower)
				img_part = (w_num*self.dst_w, h_num*self.dst_h, \
							(w_num+1)*self.dst_w, (h_num+1)*self.dst_h)
				img_box.append(img_part)
		
		return img_box
	
	
	def cut(self):		
		i = 0
		img_box = self.get_img_box()
		h_nums, w_nums = self.get_nums()
		img = cv2.imread(self.input_dir)
		
		
		for h_num in range(h_nums):
			for w_num in range(w_nums):				
				x, y, x_w, y_h = img_box[i]
				dst = img[y:y_h, x:x_w]
				i += 1
				path = self.out_dir + '/' + str(h_num+1) + '_' + str(w_num+1) + '.jpg'
				print(path)
				cv2.imwrite(path, dst)
				
				
	def bulit_net(self):
		print(self.front_size)
		line_color = (105, 105, 105)
		front_color = (255, 255, 0)
		
		i = 0
		img = cv2.imread(self.input_dir)
		img_box = self.get_img_box()
		h_nums, w_nums = self.get_nums()
		front_type = cv2.FONT_HERSHEY_SIMPLEX
	
		for h in range(h_nums):
			for w in range(w_nums):
				# (left, upper, right, lower)

				x, y, x_w, y_h = img_box[i]
				i += 1			
				cv2.rectangle(img, (x, y), (x_w, y_h), line_color, 1)
				index = str(h+1) + ':' + str(w+1)			
				cv2.putText(img, index, (x, y_h-5), front_type, \
										self.front_size, front_color, 1)
		
		
		filename = str(self.dst_h) + '.jpg'
		print(filename)
		cv2.imwrite(filename, img)
		'''
		win_name = 'img'
		cv2.imshow(win_name, img)
		if cv2.waitKey() == ord('q'):
			cv2.destroyAllWindows()
		'''


if __name__ == '__main__':
	input_dir = ['123.jpg'] * 6 
	base_dir = '123'

	size_list = [60, 80, 100, 120, 140, 160]
	front_size_list = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
	out_dir_list = []
	
	for item in size_list:
		path = base_dir + '/' + str(item)
		out_dir_list.append(path)

	
	for m in map(CutImage, input_dir, out_dir_list, size_list,\
										size_list, front_size_list):
		m.cut()
		m.bulit_net()
		
			








