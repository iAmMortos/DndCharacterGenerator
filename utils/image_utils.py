
from PIL import Image
import base64
import io


def bytestr_to_img(bstr):
  msg = base64.b64decode(bstr)
  buf = io.BytesIO(msg)
  return Image.open(buf)


def img_to_bytestr(img, img_format="PNG"):
  buffered = io.BytesIO()
  img.save(buffered, format=img_format)
  img_str = base64.b64encode(buffered.getvalue())
  return img_str


def load_img_to_bstr(filename):
  msg = b'<plain_txt_msg:img>'
  with open(filename, 'rb') as imageFile:
    msg = msg + base64.b64encode(imageFile.read())
  msg = msg + b'<!plain_txt_msg>'
  return msg


def save_bytestr_to_img_file(bstr, file):
  with open(file, 'wb') as f:
    f.write(base64.decodebytes(bstr))
