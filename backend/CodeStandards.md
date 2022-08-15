# Python语言代码规范

python的代码风格被整理成了一份python编码规范，这一份规范就是PEP8规范。

## PEP8

- 官方文档：https://legacy.python.org/dev/peps/pep-0008/ 
- 中文翻译： https://www.jb51.net/article/103944.htm

## 基本的编码规范

### 缩进规则

1. Python 采用代码缩进和冒号（ : ）来区分代码块之间的层次。
2. 在 Python 中，对于类定义、函数定义、流程控制语句、异常处理语句等，行尾的冒号和下一行的缩进，表示下一个代码块的开始，而缩进的结束则表示此代码块的结束。
3. Python 中实现对代码的缩进，可以使用空格或者 Tab 键实现。但无论是手动敲空格，还是使用 Tab 键，通常情况下都是采用 4 个空格长度作为一个缩进量（默认情况下，一个 Tab 键就表示 4 个空格）。
4. 对于 Python 缩进规则，初学者可以这样理解，Python 要求属于同一作用域中的各行代码，它们的缩进量必须一致，但具体缩进量为多少，并不做硬性规定。

正确示例代码

```python
if a==1:
    print("正确")  # 缩进4个空白占位
else:              # 与if对齐
    print("错误")   # 缩进4个空白占位
```

错误示例代码

```python
if a==1:
    print("正确") 
else:              
    print("错误")   
 print("end")   # 改正只需将这行代码前面的空格删除即可
```

记住一点：统一使用4个空格进行缩进，不要用tab，也不要tab和空格使用（我们常用的IDE中可以设置）

### 注释部分

Python中使用 # 进行注释，我们在使用# 的时候，# 号后面要空一格
在行内注释的时候，中间应该至少加两个空格

```python
# 
# 注释部分 
```

### 空格

使用的一般性原则：

1. 在二元运算符两边各空一格，算术操作符两边的空格可灵活使用，但两侧务必要保持一致
2. 不要在逗号、分号、冒号前面加空格，但应该在它们后面加（除非在行尾）
3. 函数的参数列表中，逗号之后要有空格
4. 函数的参数列表中，默认值等号两边不要添加空格
5. 左括号之后，右括号之前不要加添加空格
6. 参数列表， 索引或切片的左括号前不应加空格

通常情况下，在运算符两侧、函数参数之间以及逗号两侧，都建议使用空格进行分隔。

### 空行使用

使用的一般性原则：

1. 编码格式声明、模块导入、常量和全局变量声明、顶级定义和执行代码之间空两行
2. 顶级定义之间空两行，方法定义之间空一行
3. 在函数或方法内部，可以在必要的地方空一行以增强节奏感，但应避免连续空行

使用必要的空行可以增加代码的可读性，通常在顶级定义（如函数或类的定义）之间空两行，而方法定义之间空一行，另外在用于分隔某些功能的位置也可以空一行。

### 模块导入部分

1. 导入总应该放在文件顶部，位于模块注释和文档字符串之后，模块全局变量和常量之前。
2. 导入应该按照从最通用到最不通用的顺序分组，分组之间空一行：

```python
标准库导入
第三方库导入
应用程序指定导入
```

3、每个 import 语句只导入一个模块，尽量避免一次导入多个模块

```python
#推荐
import os
import sys

#不推荐
import os,sys
```

### 命名规范

命名规范这一块的大家应该都比较熟悉了，但是不同的编程语言之间的明明规范也是有所区别的

Python命名建议遵循的一般性原则：

1. 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线
2. 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3. 函数名一律小写，如有多个单词，用下划线隔开
4. 私有函数可用一个下划线开头
5. 变量名尽量小写, 如有多个单词，用下划线隔开
6. 常量采用全大写, 如有多个单词，使用下划线隔开

### 引号用法

引号使用的一般性原则：

1. 自然语言使用双引号
2. 机器标识使用单引号
3. 正则表达式使用双引号
4. 文档字符串 (docstring) 使用三个双引号

### 分号用法

Python跟其他几个主流编程语言的分号使用区别很大
Python的代码末尾不需要加分号，而Java和C#等都需要添加

不要在行尾添加分号，也不要用分号将两条命令放在同一行，例如：

```python
# 不推荐
print("Hello") ;  print("World") 
```