title = input()
color = input()
color2 = input()
title1 = input()
text = input()
 
print('<html>')
print('<head>')
res = '<title>' + title + '</title>'
print(res)
res = '<style>h1{color:' + color + '}p{color:' +  color2 +  '}</style>'
print(res)
print('</head>')
print('<body>')
res = '<h1>'+title1+'</h1>'
print(res)
res = '<p>'+text +'</p>'
print(res)
print('</body>')
print('</html>')
