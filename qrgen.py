#install libraries
#in terminal-> install pip qrcode image

import qrcode



def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrkod.png")
generate_qrcode("https://github.com/hubost")
#create function that collet a text and convert it to qr
#save the qr code as image
#run the function