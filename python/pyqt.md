# PyQt

GUI(Graphical User Interface)

## 1. 安装

- pip install PyQt5 -i https://pypi.douban.com/simple/

- pip install PyQt5-tools -i https://pypi.douban.com/simple



将.ui文件转换为.py文件

pyuic5 -o firstMainWin.py firstMainWin.ui



界面与逻辑分离

界面文件---逻辑文件



widget 控件，小部件

geometry 几何
double spin Box  双精度数字调节框

sizeHint 控件的推荐尺寸
minimumSize

sizePolicy

- Horizontal Streth(水平伸展)

Edit Buddies 建立伙伴关系

Edit Tab Order 设置Tab键次序

separator 分隔符

shortcut 捷径

窗口类型 QMainWindow（主窗口）, QWidget,（可能作为顶层窗口，亦可能切入到其他窗口中） QDialog(对话框)

- 主窗口(QMainWindow) --继承自QWidget类
  - 菜单栏(Menu Bar)
  - 工具栏(Tool Bar)
  - 状态栏(Status Bar)



QDesktopWidget 描述显示屏幕的类

QLabel 对象作为一个占位符可以显示不可编辑的文本或图片，也可以放置一个GIF动画，还可以被用作提示标记为其他控件



在创建事件循环后，通过建立信号（signal）和槽（slot）的连接（QObject.signal.connect()）就可以实现对象之间的通信。当信号发射（emit）时,连接的槽函数将会自动执行。

