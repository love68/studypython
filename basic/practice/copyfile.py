# -*- coding: utf-8 -*-
import os
from multiprocessing import Pool,Manager


def copyFileTask(name, oldPath, newPath,queue):
    fr = open(oldPath+"/"+name)
    fw = open(newPath+"/"+name,"w")
    while len(fr.read(1024)) != 0:
        fw.write(fr.read(1024))
    fr.close()
    fw.close()
    queue.put(name)


def main():
    oldPath = "G:\美剧\天堂执法者\第四季"
    newPath = "G:\美剧\复制"
    os.mkdir(newPath)
    files = os.listdir(oldPath)

    pool = Pool(5)
    # 线程间通信，创建Queue
    queue = Manager().Queue()

    for name in files:
        pool.apply_async(copyFileTask, args=(name, oldPath, newPath,queue))

    total = len(files)
    num = 0
    while num<total:
        queue.get()
        num+=1
        copyRate = num/total
        print("复制进度%.2f"%(copyRate*100),end="")


if __name__=="__main__":
    main()


