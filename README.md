#pyinstaller -F -w main.py    生成exe指令

# python_trunk
#在调用PySide2库时，执行代码会出现QT平台无初始化的问题。
#解决办法是高级系统设置里面“环境变量”-》“用户变量”-》变量名“QT_QPA_PLATFORM_PLUGIN_PATH”，变量值-》“D:\学习\software_python_code\python_trunk\venv\Lib\site-packages\PySide2\plugins\platforms”


#关于在系统编译正常，但是生成exe文件时“Failed to execute script main”出现两个问题。
#调用PySide2库时__init__.py需要修改
#shiboken2 = root
#result = [shiboken2, os.path.join(root, 'PySide2')]
#dirname = os.path.dirname(__file__) 
#plugin_path = os.path.join(dirname, 'plugins', 'platforms')
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
#编译时使用的是本地工程的库“D:\学习\software_python_code\python_trunk\venv”，但是生成exe文件时使用的是“C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages”
#所以导致编译正常然后生成exe文件不正常。解决方法就是把本地编译的库同步更新到exe所需要的库里面。
