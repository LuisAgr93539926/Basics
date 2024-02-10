import qrcode


class QR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(version=1, box_size=size, border=padding)

    def create_qr(self, file_name: str, foreground, background):
        user_input: str = input('Type some text -> ')

        self.qr.add_data(user_input)
        image = self.qr.make_image(fill_color=foreground, back_color=background)
        image.save(file_name)


if __name__ == '__main__':
    myQR = QR(10, 2)
    myQR.create_qr("qr.png", "Green", "White")