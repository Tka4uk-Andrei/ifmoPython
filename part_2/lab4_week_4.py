import os
import urllib.request as r
import time
import queue
from threading import Thread

# save_dir=os.getcwd()
image_links = []
count = 0

def download(q, cout):
    tt = q.get(block=False)
    try:
        r.urlopen(tt)
        print('Process', str(cout), "downloaded", tt)
    # print(self.name, g.get()
    except:
        print("error download")


http_adress = input()
url_file = r.urlopen(http_adress)

url_html = url_file.read().decode('utf-8')
arr = url_html.split('<img')
res = ''
arr_dubl = []  # для проверки на дубликаты, также там будут хранится все подходящие ссыдки
chech_doubl_bool = 1
start_num = 1
for i in range(1, len(arr), 1):
    temp = arr[i].split('src="')
    temp2 = temp[1].split('"')
    for i in range(0, len(arr_dubl), 1):
        if arr_dubl[i] == temp2[0]:
            chech_doubl_bool = 0
    start_str = temp2[0][0: -1 * (len(temp2[0])) + 5]
    start_str2 = temp2[0][0: -1 * (len(temp2[0])) + 6]
    if ((chech_doubl_bool == 1) and ((start_str == "http:") or (start_str2 == "https:"))):
        arr_dubl.append(temp2[0])
        print(str(start_num), "image", temp2[0])
        start_num = start_num + 1
    chech_doubl_bool = 1

q = queue.Queue()
for i in range(0, len(arr_dubl), 1):
    q.put(arr_dubl[i])

therads = []
start = time.time()
for i in range(0, len(arr_dubl), 1):
    #download(q, i+1)
    t = Thread(target=download, args=(q, i + 1))
    t.setDaemon(True)
    therads.append(t)
    t.start()

for i in therads:
    i.join()
