# import os
# file_name = os.listdir('./')
# for name in file_name:
#     new_name = name+'python'
#     os.renames(name,new_name)
import os
# 设置重命名标识：如果为1则添加指定字符，flag取值为2则删除指定字符
flag = 2
# 获取指定⽬录
dir_name = '../'
# 获取指定⽬录的⽂件列表
file_list = os.listdir(dir_name)
# print(file_list)
# 遍历⽂件列表内的⽂件
for name in file_list:
    # 添加指定字符
    if flag == 1:
        new_name = 'Python-' + name
    # 删除指定字符
    elif flag == 2:

        # num_index = name.find('python')
        num_index = len('Python-')
        new_name = name[num_index:]
    # 打印新⽂件名，测试程序正确性
    print(new_name)
    # 重命名
    os.rename(dir_name+name, dir_name+new_name)
