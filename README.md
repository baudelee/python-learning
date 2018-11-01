# python-learning
python elementry learning

# pool class

Pool对象调用join()方法等待所有子进程执行完毕，调用join()之前必须先调用close()，让其不再接受新的Process。

map()放入多个迭代参数，返回多个结果

# subprocess function call
link : https://blog.linuxeye.cn/375.html
subprocess 用来fork一个子进程，并运行一个外部程序。

  subprocess.call(): 父进程等待子进程完成.返回退出信息(returncode,相当于linux exit code)
  subprocess.check_call() : 父进程等待子进程完成。返回0

  检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查
