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
