import os
#做一个搜索所有.py文件的程序，然后把这些.py文件放在一个文件夹里
def search(catalog,target):
    os.chdir(catalog)
    
    for each_file in os.listdir(os.curdir):
        tuple_temp = os.path.splitext(each_file)
        if tuple_temp[1] in target:
            py_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search(each_file,target) #继续搜索子文件夹里有没有
            os.chdir(os.pardir) #返回上一层是必须的，结束递归


catalog = input('请输入待查找的初始目录：')
target = ['.py']
py_list = []
search(catalog,target)

f = open(os.getcwd() + os.sep + 'pythonlist.txt','w')
f.writelines(py_list)
f.close()

