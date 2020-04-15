import urllib.parse as u
import urllib.request as r
http_adress = input()
upl_res = u.urlparse(http_adress)
url_res_tuple = tuple(upl_res)
 
print(url_res_tuple)
#print(upl_res)
 
url_file = r.urlopen(http_adress)
 
url_html = url_file.read().decode('utf-8')
arr = url_html.split('<h1>')
res = ''
for i in range(1, len(arr), 1):
    res+=arr[i].split('</h1>')[0]+' '
   
print(res[0:-1])