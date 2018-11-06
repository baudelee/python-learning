# python-learning
python elementry learning

# pool class

Pool对象调用join()方法等待所有子进程执行完毕，调用join()之前必须先调用close()，让其不再接受新的Process。

map()放入多个迭代参数，返回多个结果

# subprocess function call
 link : https://blog.linuxeye.cn/375.html （if you want to get more info, please refer to this link）
 subprocess 用来fork一个子进程，并运行一个外部程序。

  - subprocess.call(): 父进程等待子进程完成.返回退出信息(returncode,相当于linux exit code)。检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查
  - subprocess.check_call() : 父进程等待子进程完成。返回0
  - subprocess.check_output(): 父进程等待子进程完成。返回子进程向标准输出的输出结果。检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查
  ```
  >>>import subprocess
  >>>retcode = subprocess.call(["ls","-l"]) #和shell中命令ls -a显示结果一样
  >>>print retcode #0
  ```
  将程序名(ls)和所带的参数(-l)一起放在一个表中传递给subprocess.call()
  shell默认为False，在linux下，shell=False时，Popen调用os.execvp()执行args指定的程序；shell=True时，如果args是字符串，Popen直接调用系统的shell来执行args指定的程序，如果args是一个序列，则args的第一项是定义程序命令字符串，其他项是调用系统shell时的附加参数。
  所以上面代码也可写成：
  ```
  >>>retcode = subprocess.call("ls -l",shell=True)
  ```
  在Windows下，不论shell的值如何，Popen调用CreateProcess()执行args指定的外部程序。如果args是一个序列，则先用list2cmdline()转化为字符串，但需要注意的是，并不是MS Windows下所有的程序都可以用list2cmdline来转化为命令行字符串。

# 函数
- 函数调用会为函数局部变量生成一个新的符号表。确切地说，所有函数中的变量赋值都是讲值存储在局部符合表。变量引用首先在局部符合表中查找，然后是包含函数的局部符号表，然后是全局符合表，最后是内置名字表。因此，*全局变量不能再函数中直接赋值（除非用global语句命名）*，尽管他们可以被引用。
- 一个函数被另一个函数调用时，一个新的局部符号表在调用过程中被创建。
## 函数参数
- * 操作符自动把参数列表拆分
```
>>> list(range(3,6))
[3,4,5]
>>> args = [3,6]
>>> list(range(*args))
[3,4,5]
```
- ** 操作符分拆关键字参数为字典
```
>>> def parrot(voltage, state='a stiff', action='voom'):
...    print '-- This parrot wouldn't', action,
···    print 'if you put', voltage, "volts through it.",
···    print "E's", state, "!"
···
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- this parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```
## 函数式编程工具
- * filter() map() and reduce()
```
>>> def f(x): return x % 3 == 0 or x % 5 ==0
...
>>> filter(f,range(2,10))
[3,5,6,9]
```
- * filter(function, sequence)返回一个sequence(序列)，包括了给定序列中所有调用function(item)后返回值为True的元素（如果可能的话，会返回相同的类型）。如果该序列(sequence)是一个str，unicode或者tuple，返回值必定是同一个类型，否则，他总是list。

- * map(function, sequence)为每一个元素调用function(item),并将结果返回组成一个链表返回。
```
>>> def cube(x): return x*x*x
...
>>> map(cube, range(1,11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
-* 可以传入多个序列，函数也必须要有对应数量的参数，执行时会依次用各序列上对应的元素来调用函数（如果某些序列比其他短，就用None来代替）。如果把None作为函数传入，则直接返回参数作为替代。
```
>>> seq = range(8)
>>> def add(x,y): return x + y
...
>>> map(add, req, req)
[0, 2, 4, 6, 8, 10, 12, 14]
```

- * reduce(function, sequence)返回一个单值，它是这样构造的：首先以序列的前两个元素调用函数function，再以返回值和第三个参数调用，依次执行下去。
```
>>>def add(x,y): return x + y
...
>>> reduce(add, range(1,11))
55
```
如果序列只有一个元素，就返回它，如果序列是空的，就抛出一个异常。


