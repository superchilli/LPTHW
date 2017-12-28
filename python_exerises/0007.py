# 第 0007 题：

# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# 1. 遍历目录里的文件，找出文件结尾是 .py 的文件
# 2. 读取文件，统计行数，如果是空行，空行+1，如果是#开通，或者在"""或'''之间的代码，注释+1，否则code+1。

import os


def findFile(path):
    file_path=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('py'):
                file_path.append(os.path.join(root, f))
    return file_path
        

def countCode(path):
    file_name=os.path.basename(path)
    comment_flag=False
    code_line=0
    comment_line=0
    space_line=0
    
    with open(path) as f:
        for line in f.read().split('\n'):
            code_line += 1
            
            if line.strip().startswith('"""') and not comment_flag:
                comment_flag = True
                comment_line += 1
                continue
                
            if line.strip().startswith('"""'):
                comment_flag = False
                comment_line += 1
                
            if line.strip().startswith('#') or comment_flag:
                comment_line += 1
                
            if len(line) == 0:
                space_line += 1
            
    print('File {0} have {1} lines code, {2} lines space, {3} lines comment.'.format(file_name, code_line, space_line, comment_line))
    
    
if __name__ == '__main__':
    for f in findFile('.'):
        countCode(f)
    