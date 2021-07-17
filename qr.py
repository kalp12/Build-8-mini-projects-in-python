import pyqrcode
import png
def qrcode():
    q = pyqrcode.create(input('Enter word  '))
    q.png('qrcode.png',scale=6)
    print('QR generated')

if __name__ == '__main__':
    qrcode()