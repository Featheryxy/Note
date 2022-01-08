import os 


input_dir = ''
input_list = []
find_list = []

name_list = list(os.walk(input_dir))[0][2]
print(list(os.walk(input_dir)))
print("图片名称: ", name_list, "图片数量: ", len(name_list))

	
n = len(input_list)
for i in range(0, n-1, 2):
	img_name = str(input_list[i]) + "_" + str(input_list[i+1]) + ".jpg"
	find_list.append(img_name)
print("要修改的图片名称： ", find_list, "要修改的图片数量: ", len(find_list))



os.chdir(input_dir)
for raw_name in find_list:
	if raw_name in name_list:
		newname = raw_name[:-4] + '_3.jpg'
		print("rename...", newname)
		os.rename(raw_name, newname)



