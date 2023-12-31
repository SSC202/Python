# Numpy 

## 1. 数组

### 数组的创建

使用`np.array()`函数可以从列表中创建一个数组。

```python
import numpy as np

np.array([1,2,3,4,5])
```

注意，数组中的类型必须匹配，如果数据类型不一致，则会向上匹配。

> Numpy 的数组是多维的，多维数组可以从嵌套列表中创建。

- 特殊创建方法

1. 零数组

```python
"""
	零数组创建函数
	第一个参数：长度（形状的元组）
	第二个参数 dtype：数据类型
"""
np.zeros()
```

2. 单位数组

```python
"""
	单位数组创建函数
	第一个参数：长度（形状的元组）
	第二个参数 dtype：数据类型
"""
np.ones()

"""
	单位矩阵创建函数
	第一个参数：行（列）数
"""
np.eye()
```

3.  创建同值数组

```python
"""
	同值数组创建函数
	第一个参数：长度（形状的元组）
	第二个参数：数组的元素值
"""
np.full()
```

4. 创建线性序列数组

```python
"""
	线性序列创建函数
	第一个参数：起始点
	第二个参数：中止点
	第三个参数：步长
"""
np.arange()

"""
	线性序列创建函数
	第一个参数：起始点
	第二个参数：中止点
	第三个参数：元素数量
"""
np.linspace()
```

5. 创建随机数组

```python
"""
	随机数组创建函数（均匀分布，0-1范围）
	第一个参数：数组形状
"""
np.random.random()

"""
	随机数组创建函数（正态分布）
	第一个参数：均值
	第二个参数：标准差
	第三个参数：形状
"""
np.random.normal()

"""
	随机数组创建函数（随机整型）
	第一个参数：起点
	第二个参数：终点
	第三个参数：形状
"""
np.random.randint()
```

6. 创建空数组

```python
"""
	创建空数组
	第一个参数：行（列）数
"""
np.empty()
```

### Numpy 标准数据类型

| 数据类型     | 描述                                    |
| ------------ | --------------------------------------- |
| `bool_`      | 布尔值（`True`，`False`），使用一个字节 |
| `int_`       | 默认整型，通常为`int64`或`int32`        |
| `intc`       | 通常为`int64`或`int32`                  |
| `intp`       | 同C语言的`size_t`，用作索引的整型       |
| `int8`       | 1字节整型                               |
| `int16`      | 2字节整型                               |
| `int32`      | 4字节整型                               |
| `int64`      | 8字节整型                               |
| `uint8`      | 1字节无符号整型                         |
| `uint16`     | 2字节无符号整型                         |
| `uint32`     | 4字节无符号整型                         |
| `uint64`     | 8字节无符号整型                         |
| `float_`     | `float64`                               |
| `float16`    | 半精度浮点型                            |
| `float32`    | 单精度浮点型                            |
| `float64`    | 双精度浮点型                            |
| `complex_`   | 复数`complex128`                        |
| `complex64`  | 两个32位浮点数表示的复数                |
| `complex128` | 两个64位浮点数表示的复数                |

### 数组的属性

`ndim`：数组的维度

`shape`：数组每个维度的大小

`size`：数组总大小

`dtype`：数据类型

### 数组的索引和切片

- 使用`[]`进行索引，索引从0开始；如果想从末尾开始索引，使用负数索引。
- 多维数组中，使用`,`进行索引分隔。
- 使用`[start:stop:step]`方式进行切片，注意为左闭右开区间。如果未指定，则`start = 0, stop = ndim, step = 1 `；

> 1. `step`为负数时为逆序，-1为遍历逆序；
> 2. `:`表示空切片，在获取行时可以省略行号后面的切片符，如x[0]；

注意：Numpy 数组的切片是一个数组的视图，不是数组的副本，修改切片会导致数组本身的改变。

> 为了获得副本，通常使用`copy()`函数。

### 数组的变形，分裂和拼接

#### 数组变形（reshape）

数组可以通过`reshape()`方法变形：

```python
"""
	数组变形函数
	参数：变形的形状
"""
array.reshape()

x = np.arange(1,10).reshape((3,3))
```

> 在一维数组切片中使用`newaxis`可以实现转换为列向量或者行向量。

#### 数组拼接

```python
"""
	数组拼接函数
	第一个参数：数组列表
	第二个参数：拼接方向，0为行拼接，1为列拼接
	注意：不能跨维度拼接
"""
np.concatenate()

np.concatenate([x1,x2],axis=0)
```

沿固定维度处理数组时，使用`np.vstack()`（垂直栈）函数和`np.hstack()`（水平栈），`np.dstack()`（深度栈）函数将更加简洁。

```python
"""
	栈函数
	参数：数组列表
"""
np.vstack()
np.hstack()
np.dstack()
```

#### 数组分裂

```python
"""
	数组分裂函数
	第一个参数：数组
	第二个参数：索引号标志的断电
"""
np.split()
```

沿固定维度处理数组时，使用`np.vsplit()`（垂直栈）函数和`np.hsplit()`（水平栈），`np.dsplit()`（深度栈）函数将更加简洁。

```python
"""
	栈函数
	第一个参数：数组
	第二个参数：索引号标志的断电
"""
np.vsplit()
np.hsplit()
np.dsplit()
```

## 2. Numpy 通用函数

### 数组运算函数

| 运算符 | 通用函数            | 描述         |
| ------ | ------------------- | ------------ |
| `+`    | `np.add()`          | 加法运算     |
| `-`    | `np.substract()`    | 减法运算     |
| `-`    | `np.negative()`     | 负数运算     |
| `*`    | `np.multiply()`     | 乘法运算     |
| `/`    | `np.divide()`       | 除法运算     |
| `//`   | `np.floor_divide()` | 向下整除运算 |
| `**`   | `np.power()`        | 指数运算     |
| `%`    | `np.mod()`          | 模/余数      |

- 绝对值函数`np.abs()`
- 三角函数（输入为弧度值）

`np.sin()`，`np.cos()`，`np.tan()`，`np.arcsin()`，`np.arccos()`，`np.arctan()`

- 指数和对数函数

`np.exp()`，`np.exp2()`，`np.power()`，`np.log()`，`np.log2()`，`np.log10()`，`np.expm1()`，`np.log1p()`

通用函数有指定输出，聚合，外积等性质。

### 聚合函数

| 函数名            | 描述                     |
| ----------------- | ------------------------ |
| `np.sum()`        | 计算所有元素的和         |
| `np.prod()`       | 计算所有元素的积         |
| `np.mean()`       | 计算所有元素的平均值     |
| `np.std()`        | 计算所有元素的标准差     |
| `np.var()`        | 计算所有元素的方差       |
| `np.min()`        | 计算最小值               |
| `np.max()`        | 计算最大值               |
| `np.argmin()`     | 计算最小值的索引         |
| `np.argmax()`     | 计算最大值的索引         |
| `np.median()`     | 计算中位数               |
| `np.percentile()` | 计算基于元素排序的统计值 |
| `np.any()`        | 计算是否存在元素为`True` |
| `np.all()`        | 计算所有元素是否为`True` |

### 数组的布尔运算

布尔运算返回布尔类型的数组，将会进行逐元素的逻辑运算。

| 运算符 | 通用函数             |
| ------ | -------------------- |
| `==`   | `np.equal()`         |
| `!=`   | `np.not_equal()`     |
| `<`    | `np.less()`          |
| `>`    | `np.less_equal()`    |
| `<=`   | `np.greater()`       |
| `>=`   | `np.greater_equal()` |

对于布尔类型的矩阵，可以进行算术运算和逻辑运算：

| 运算符 | 通用函数         |
| ------ | ---------------- |
| `&`    | `np.bitwise_and` |
| `|`    | `np.bitwise_or`  |
| `^`    | `np.bitwise_xor` |
| `~`    | `np.bitwise_not` |

## 3. 数组的广播

数组的广播机制允许对两个形状不相同的数组进行二元运算；

**广播规则**：

1. 两个数组的维度数不相同，则小维度数组将会在左边添加1个维度；
2. 两个数组在任何一个维度都不匹配，则数组的形状会沿着维度为1的维度扩展进行匹配；
3. 如果两个数组在任何一个维度不匹配且无一个维度为1，则引发异常。

4. 扩展即复制自身元素。



