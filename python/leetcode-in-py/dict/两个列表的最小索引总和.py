# coding=gbk

# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。

def findRestaurant(list1, list2):
		"""
		:type list1: List[str]
		:type list2: List[str]
		:rtype: List[str]
		"""
		ret = []
		dict1 = {}
		
		for i in range(len(list1)):
			if list1[i] in list2:
				dict1[list1[i]] = i + list2.index(list1[i])
		min_value = min(list(dict1.values()))
		for key, value in dict1.items():
			if value == min_value:
				ret.append(key)
				return ret
				
if __name__ == "__main__":
	list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
	list2 = ["KFC", "Shogun", "Burger King"]
	print(findRestaurant(list1, list2))
	
