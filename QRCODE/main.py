

# SKUYMI [helmisalsabila.com]

import pyqrcode as qr
import png

link = 'https://www.helmisalsabila.com'
qrc = qr.create(link)
qrc.png('helmisalsabila.png', scale=5)