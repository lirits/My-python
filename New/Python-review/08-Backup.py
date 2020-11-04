# 需求：⽤户输⼊当前⽬录下任意⽂件名，程序完成对该⽂件的备份功能(备份⽂件名为xx[备份]后缀，例
# 如：test[备份].txt)。
# 1. 接收⽤户输⼊的⽂件名
# 2. 规划备份⽂件名
# 3. 备份⽂件写⼊数据

# 1. 接收⽤户输⼊的⽂件名
import time
while True:
    file_name = input('请输入你要备份的文件名')
# 2. 规划备份⽂件名
    if file_name.find('.') != -1:
        file_name_2 = file_name.rindex('.')
        if file_name_2>0:
            file_backup_name = file_name[:file_name_2]+'_backup'+file_name[file_name_2:]
            # 3. 备份⽂件写⼊数据
            f_old = open(f'{file_name}','rb')
            f_new = open(f'{file_backup_name}', 'wb')
            content = f_old.read()
            f_new.write(content)
            f_old.close()
            f_new.close()
            print('备份完成')
            break
        else:
            print('文件名不能为空')
    else:
        print('请输入正确的文件名(带后缀)')
        time.sleep(2)