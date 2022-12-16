import os

path="C:/Users/jayw7/OneDrive/桌面"
os.makedirs(path+"/music/a/b", exist_ok =True)
# 函數功能: 顯示指定路徑下，該層的檔案及資料夾名稱
def batch_showname(path):
    listdir1=os.listdir(path)
    print(listdir1)
    print(type(listdir1))
    for fname in listdir1:
        print(os.path.join(path, fname))
batch_showname("C:")

# 函數功能: 遞迴顯示指定路徑下的所有檔案及資料夾名稱
def find_dir(path):
    for fd in os.listdir(path):
        full_path=os.path.join(path,fd)
        if os.path.isdir(full_path):
            print('資料夾:',full_path)
            find_dir(full_path)
        else:
            print('檔案:',full_path)
#find_dir("C:/Users/jayw7/OneDrive/桌面")


def path_convert(path):
    c1='\\'
    c2='//'
    return [l for l in path if l != c1 else c2].join('')
ans="C:\Users\jayw7\OneDrive\桌面"
print(ans)
print(path_convert(ans))