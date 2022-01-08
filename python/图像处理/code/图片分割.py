import cv2
import os


class CutImage:
	def __init__(self, input_dir, out_dir, dst_w, dst_h):
		self.input_dir = input_dir
		self.out_dir =  out_dir
		self.dst_w = dst_w
		self.dst_h = dst_h
	
	
	def cut(self):
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		
		img = cv2.imread(input_dir)
		imginfo = img.shape
		h = imginfo[0]
		w = imginfo[1]


		h_num = h // self.dst_h 	
		w_num = w // self.dst_w	


		for h in range(h_num):
			for w in range(w_num):
				# (left, upper, right, lower)
				img_part = (w*self.dst_w, h*self.dst_h, (w+1)*self.dst_w, (h+1)*self.dst_h)
				x, y, x_w, y_h = img_part
				dst = img[y:y_h, x:x_w]
				filename = out_dir + '/' + str(h+1) + '_' + str(w+1) + '.jpg'
				print(filename)
				cv2.imwrite(filename, dst)


if __name__ == '__main__':

	size_list = [60, 80, 100, 120, 140, 160]
	
	input_dir = 'XIUSHI058.jpg'
	base_dir = 'xs058'

	for size in size_list:
		out_dir = base_dir + '/' + str(size)
		cut_img = CutImage(input_dir, out_dir, size, size)
		cut_img.cut()
		







 		






