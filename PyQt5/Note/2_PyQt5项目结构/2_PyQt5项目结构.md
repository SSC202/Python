# Python PyQt5 2_PyQt5的项目结构

## 1. 面向过程的项目

<font color=LightGreen>1. 导入需要的库</font>

 ```python
 import sys
 from PyQt5.Qt import *
 ```

<font color=LightGreen>2. 创建一个应用程序</font>

```python
app = QApplication(sys.argv)
```

<font color=LightGreen>3. 控件操作(创建控件，设置控件，添加子控件，事件/信号处理，控件显示)</font>

```python
w = QWidget()
w.show()
```

> - 创建控件之后，如果此控件无父控件，则此控件为顶层控件（窗口），系统自动为窗口添加标题栏等装饰。
> - 默认情况下不会展示控件，需要调用`show()`方法。

<font color=LightGreen>4. 执行程序并进入消息循环</font>

```python
sys.exit(app.exec())
```

## 2. 面向对象的项目

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("PyQt5")
      self.label = QLabel(self)
      self.label.setText("Hello World")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      self.label.setFont(font)
      self.label.move(50,20)
    
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
    
if __name__ == '__main__':
   main()
```

