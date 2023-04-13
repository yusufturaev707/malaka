from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# HTML Render to pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


import pandas as pd


# Read data from excell
def read_data_excell(file):
    data = pd.read_excel("." + file, header=None)
    df = pd.DataFrame(data)
    n = df.shape[0]
    users = []
    for i in range(n):
        user = []
        fam = df.iloc[i, 0]
        ism = df.iloc[i, 1]
        sharf = df.iloc[i, 2]
        jshshr = df.iloc[i, 3]
        # invoice = df.iloc[i, 4]

        user.append(fam)
        user.append(ism)
        user.append(sharf)
        user.append(jshshr)
        # user.append(invoice)

        users.append(user)

    return users


import hashlib
import datetime
import qrcode


# QR code

def qr_code_function(ob):
    # Convert the date object to a string and encode it
    date_str = str(ob.jshshr).encode('utf-8')
    # Create a hash object using the SHA-256 algorithm
    hash_object = hashlib.md5()
    # Update the hash object with the encoded date string
    hash_object.update(date_str)
    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()
    # Print the hash
    # Importing library
    # Data to be encoded
    data = f'https:www.ilmiymarkaz.com/{hex_digest}/'
    # Encoding data using make() function
    img = qrcode.make(data)
    # Saving as an image file
    img.save(f'media/qr_codes/{hex_digest}.png')
    return hex_digest
