import requests

link = 'http://online.flipbuilder.com/aimn/niys/files/mobile/1.jpg'

for x in range(1,89):
    link = 'http://online.flipbuilder.com/aimn/niys/files/mobile/' + str(x) + '.jpg'
    print link
    f = open(str(x) + '.jpg', 'wb')
    f.write(requests.get(link).content)
    f.close()

