# coding=gbk
# 等价于斐波那契数列
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

class Solution:
	
	# 递归：自顶向下
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2:
			return n
		else:
			# 二叉树
			return self.climbStairs(n-1) + self.climbStairs(n - 2)
	
	
	# 备忘录法
	def f(self, n):
		dic = dict()
		if n <= 2:
			return n
		else:
			if n in dic.keys():
				return dic[n]
			else:
				dic[n] = self.f(n-1) + self.f(n-2)
				return dic[n]
				

				
			
	
	
	
s = Solution()
print(s.climbStairs(30))
print(s.f(30))
