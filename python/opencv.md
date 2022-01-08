# openCV

## 1 基础知识

```python
# 获取所有事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

h, w, d = img.shape
img[height, width]
AXIS:  y, x
img[行信息，列信息]
```

**对比度**：使直方图的分布更加分散

**一维直方图**： 灰度值    灰度空间下

**二维直方图**：每个颜色(Hue), 饱和度(Saturation)  HSV空间下

**灰度值**： 灰度是表明图像明暗的数值，即黑白图像中点的颜色深度，范围一般从0到255，白色为255 ，黑色为0，故黑白图片也称灰度图像。灰度值指的是单个像素点的亮度。灰度值越大表示越亮

**mask** : 只有黑白两种颜色

**二值化**：让图像的像素点矩阵中的每个像素点的灰度值为0（黑色）或者255（白色），也就是让整个图像呈现只有黑和白的效果

**图像分辨率**：是指每英寸图像内的像素点数

**对比度**  =  最大亮度/最小亮度

- 数字图像：一副图像可以定义为一个二维函数f(x, y)，其中ｘ和ｙ是空间（平面）坐标，而且在任何一对空间坐标（ｘ，ｙ）处的幅值ｆ称为图像在该点处的强度或灰度。当ｘ，ｙ，和灰度值ｆ是有限的离散数值时，我们称该图像为数字图像
- 单色光（无色光）：没有颜色的光
- 强度：单色光的唯一属性
- 灰度级：表示单色光的强度，黑色到灰色到白色
- 灰度图像：单色图
- 取样与量化：对坐标进行数值化，对幅值数值化

## 2 基本操作

```
import cv2

# 0 以灰度模式读入图像，1以彩色模式读入
img = cv2.imread('1.jpg', 0)  

# 颜色空间转换 1. data， 2. BGR to GRAY
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 返回一个元祖（高， 宽， 深度）
imgInfo = img.shape

# 图像类型
img.dtype

# 获取图片的高和宽
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

# 一个像素点有bgr组成
(b, g, r) = img[100, 100]

# 画一条竖线
for i in range(0,400):
    img[230+i, 450] = (0, 255, 0)

#创建了一个可以调整大小的窗口cv2.WINDOW_NORMAL, 自适应窗口 cv2.WINDOW_AUTOSIZE
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 

# 显示一个名称(winname)为image的窗口 
cv2.imshow('image', img) 

# 参数为0，等待键盘输入
 cv2.waitKey(0)  

# 摧毁指定窗口
cv2.destroyWindow("image") 

# 摧毁所有窗口
cv2.destroyAllWindows()  
 
# 保存图片
cv2.imwrite('copy_1.jpg', img) 

# 图片缩放
cv2.resize(img, (dstWidth, dstHeight))

# 图像ROI
dst = img[200:600, 400:850]

# split比较费时，尽量使用Numpy
# 通道分离与合并 
b,g,r=cv2.split(img)
b = img.shape[:, :, 0]
img=cv2.merge(b,g,r)

# 将红色通道值都为0
img[:, :, 2] = 0

# 添加边界
# src, top, bottom, left, right, borderType[, dst[, value]]
BLUE = [255, 0, 0]
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)  # value 边界颜色

# 将像素值在[lowerb, upperb]之中的像素点设置为255，其余为0，通常在HSV空间中
mask = inRange(src, lowerb, upperb[, dst])
```

`cv2.waitKey()` 键盘绑定函数

函数等待特定的几毫秒，看是否有键盘输入。

在特定的几毫秒之内，如果按下任意键，这个函数会返回按键的ASCLL码值，程序将会继续运行。如果没有键盘输入，返回值为-1，如果参数为0，那它将会无限期的等待键盘输入

`ord()`

它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值



## 3 视频

```
# Boolean 是否成功初始化摄像头设备
cap.isOpened()

# 获取视频 参数：0为笔记本内置摄像头， 视频文件
cap = cv2.VideoCapture("1.mp4")

# 保存视频 1 file_name 2 编码器 3 帧率 4 size
video_write = cv2.VideoWriter('2.avi', -1, 5, (height, width))
video_writer.write(img)

# 一帧一帧获取视频，返回布尔值和帧
ret, frame = cap.read()

# 播放每一帧时，设置适当的持续时间
cv2.waitkey()

# 获得视频参数 0-18
cap.get(propID)

# 修改视频参数
cap.set(propID，value）

# 释放capture（捕获）资源
cap.release()
```



## 4 绘图

所有的绘图函数都返回None

`cv2.line()， cv2.circle()， cv2.rectangle()，cv2.ellipse()， v2.putText() `

上面所有的这些绘图函数需要设置下面这些参数：

- `img`：你想要绘制图形的那幅图像。
- `color`：形状的颜色。以 RGB 为例，需要传入 一个元组，例如：（ 255,0,0）代表蓝色。对于灰度图只需要传入灰度值。
-  `thickness`：线条的粗细。如果给一个闭合图形设置为 -1，那么这个图形就会被填充。默认值是 1.
-  `linetype`：线条的类型， 8 连接，抗锯齿等。默认情况是 8 连接。 `cv2.LINE_AA`为抗锯齿，这样看起来会非常平滑。 

### 4.1 画线

```
 line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
```

```python
# Create a black image
img=np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
```



### 4.2 画矩形

 ```
  rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
 ```

```
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) 
```



### 4.3 画圆

 ```
  circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
 ```

```
cv2.circle(img,(447,63), 63, (0,0,255), -1)
```



### 4.4 添加文字

 ```
  putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
 ```

```
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)
```



## 5 滑动条

- ```
  createTrackbar(trackbarName, windowName, value, count, onChange) -> None
  ```

- ```
  getTrackbarPos(trackbarname, winname) -> retval
  ```

```python
import cv2
import numpy as np


def nothing(x):
    pass


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# 只有当 转换按钮 指向 ON 时 滑动条的滑动才有用，否则窗户 都是黑的。

while True:

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')  
    # 另外一个重要应用就是用作转换按钮

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    cv2.imshow('image', img)
    k = cv2.waitKey(1)  # & 0xFF
    if k == ord("q"):
        break

cv2.destroyAllWindows()
```



## 6 算术运算



## 7 几何变换

