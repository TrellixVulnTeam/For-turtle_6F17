from webbrowser import open_new
f = open('ссылки.txt')
for s in f:
    open_new(s)
    
