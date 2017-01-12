# M-Knife 使用教程

### 简介

M-Knife 全名Multi-function Knife，是一款程序员好助手。她拥有如下功能：随机字符串生成、UUID生成、大小写转换、字符串计数等。

### 功能点

> 以上所有命令中的直接Enter换成CMD-Enter，会直接将结果粘贴在当前光标处

#### 随机字符串生成

```
rand [length] + Enter # length为字符串长度，支持1-64位，不填默认为8位，结果会复制到剪贴板。
```

#### UUID生成

```
uuid + Enter # 将生成基于时间和完全随机的两种uuid供选择，结果会复制到剪贴板。
```

```
uuid + Shift-Enter # 会将uuid转换为大写再复制到剪贴板。
```

#### 大小写转换

```
lower ABC + Enter # 将ABC转换为abc，结果会复制到剪贴板。
```

```
upper abc + Enter # 将abc转换为ABC，结果会复制到剪贴板。
```

#### 字符串计数

```
len abc + Enter # 计算字符串长度，结果会复制到剪贴板。
```

