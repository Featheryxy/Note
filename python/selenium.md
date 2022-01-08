# Selenium

## 1 简介

Selenium：最初是驱动页面进行交互的 Javascript 库，能让浏览器测试后自动返回测试结果。如今可以实现模拟人类操纵浏览器的行为的项目 

python+Selenium+Chrome+webdriver

谷歌webdriver驱动下载

https://chromedriver.storage.googleapis.com/index.html

```
#导入 selenuim 库
from selenium import webdriver

#下面一行代码用于启动 Chrome 浏览器
wb = webdriver.Chrome(r'E:\chromedriver_win32\chromedriver.exe')

driver.set_window_size(800, 480)

#退出浏览器
driver.quit()
```

```
#前进
driver.back()
#后退
driver.forward()
#刷新
driver.refresh()
#退出
driver.quit()
#截图
driver.save_screenshot("save_1.png")
```

```
#ActionChains 是一个用来模拟鼠标操作的库
from selenium.webdriver import ActionChains
```

## Cookie 的调用 

- get_cookies(): 获得所有 cookie 信息。
- delete_all_cookies():删除所有 cookie 信息。
- get_cookie([name])：返回字典的 key 为[name]的 cookie
- add_cookie(cookie_dict):添加 cookie。“cookie_dict”指字典对象，必须有 name 和value 两个值。
- delete_cookie([name],[optionsString]):删除 cookie 信息。[name]是要删除的 cookie的名称。第二个参数[optionsString]是 cookie 选项，目前支持的选项包括“路径”，“域”
  

```
JS1='window.open("https://www.sogou.com");'
driver.execute_script(JS1)
```

## 元素定位 

```
 find_element_by_id()
 find_element_by_name()
 find_element_by_class_name()
 find_element_by_tag_name()
 find_element_by_link_text()
 find_element_by_partial_link_text()
 find_element_by_xpath()
 find_element_by_css_selector()
```

```
from selenium import webdriver

driver.get('https:\\www.baidu.com')
element = driver.find_element_by_id("kw")

element.text
# ''

element.tag_name
# 'input'
 
element.get_attribute('name')
# 'wd'

element.get_property('name')
# 'wd'

# 在搜索框中输入seleniumm
element.send_keys('seleniumm')

element = driver.find_element_by_id("su")
# 点击搜索
element.click()

driver.quit()
```

