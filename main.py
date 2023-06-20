import pyqrcode


url = input("qr oluşturmak için lütfen url giriniz: ")

qr_code = pyqrcode.create(url)

qr_code.svg("qrcode.svg",scale=5)