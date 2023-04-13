from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import textwrap
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework.permissions import IsAdminUser
from refresher_course.models import Course


def paint_pdf(ob, code):
    file_name = "media/pdfs/" + f'{code}.pdf'
    image = "static/images/certificate.jpg"

    pdf = canvas.Canvas(file_name)
    pdf.setTitle(f'{ob.first_name} {ob.last_name}')
    pdf.drawImage(image, 0, 10, 590, 820)

    pdfmetrics.registerFont(TTFont('Arimo-Italic', 'Fonts/static/Arimo-VariableFont_wght.ttf'))

    pdf.setFont('Arimo-Italic', 30)
    pdf.drawCentredString(350, 680, "O‘zbekiston Respublikasi")

    pdf.setFont("Arimo-Italic", 20)
    pdf.drawCentredString(350, 630, "Malaka oshirish haqida")

    pdf.setFont("Arimo-Italic", 30)
    pdf.drawCentredString(350, 570, "SERTIFIKAT")

    pdf.setFont("Arimo-Italic", 25)
    number = str(ob.cer_nomer)
    x = number.zfill(5)
    pdf.drawCentredString(350, 510, f"MO {x}")

    pdf.setFont("Arimo-Italic", 25)
    pdf.drawCentredString(350, 450, f"{ob.first_name} {ob.last_name}")

    pdf.setFont("Arimo-Italic", 25)
    pdf.drawCentredString(350, 425, f"{ob.middle_name}")

    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 380, "2023-yil 13-20-fevral kunlari") # !

    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 360, "Bilimni baholash agentligi huzuridagi Ilmiy-o‘quv amaliy")
    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 340, f"markazida jami {ob.course.hour_course} soatlik")

    pdf.setFont("Arimo-Italic", 15)

    course_name = str(ob.course)
    segments = textwrap.wrap(course_name, width=68, break_long_words=False)

    seg_length = 320
    for segment in segments:
        pdf.drawCentredString(350, seg_length, segment)
        seg_length -= 20

    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 300 - (len(segments) - 1) * 20, "kursi bo‘yicha malakasini oshirdi.")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(210, 170, f"Boshliq: ")

    # QR code
    image = "media/qr_codes/" + f'{code}.png'
    pdf.drawInlineImage(image, 250, 150, 50, 50)

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(350, 170, f"Baratov A.A")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(210, 120, f"Sana ")
    pdf.setFont("Arimo-Italic", 10)
    year_str = ob.created_at.strftime('%Y')
    day_str = ob.created_at.strftime('%d')
    month_str = ob.created_at.strftime('%m')

    pdf.drawCentredString(290, 120, f"{day_str}.{month_str}.{year_str}")
    pdf.line(330, 115, 225, 115)

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(400, 120, f"Qayd raqami ")
    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(470, 120, f"{ob.registered_number}")
    pdf.line(505, 115, 440, 115)

    pdf.save()


def paint_pdf_gn(ob, code):
    file_name = "media/pdfs/" + f'{code}.pdf'
    image = "static/images/GN.png"

    pdf = canvas.Canvas(file_name)
    canvas.Canvas.setPageSize(pdf, (landscape(A4)))
    pdf.setTitle(f'{ob.first_name} {ob.last_name}')
    pdf.drawImage(image, 0, 0, 842, 595)

    pdfmetrics.registerFont(TTFont('Montserrat-Bold', 'Fonts/static/Montserrat-Bold.ttf'))
    pdf.setFont('Montserrat-Bold', 15.5)
    pdf.drawCentredString(200, 540, "O‘ZBEKISTON RESPUBLIKASI")
    pdf.setFont('Montserrat-Bold', 15)
    pdf.drawCentredString(190, 520, "OLIY TA’LIM, FAN VA INNOVATSIYALAR")
    pdf.setFont('Montserrat-Bold', 15.5)
    pdf.drawCentredString(200, 500, "VAZIRLIGI HUZURIDAGI")
    pdf.setFont('Montserrat-Bold', 15.5)
    pdf.drawCentredString(200, 480, "BILIM VA MALAKALARNI BAHOLASH")
    pdf.setFont('Montserrat-Bold', 15.5)
    pdf.drawCentredString(200, 460, "AGENTLIGI")

    pdfmetrics.registerFont(TTFont('Montserrat-Bold', 'Fonts/static/Montserrat-Bold.ttf'))
    pdf.setFont('Montserrat-Bold', 17)
    pdf.drawCentredString(650, 530, "BILIMNI BAHOLASH")
    pdf.setFont('Montserrat-Bold', 17)
    pdf.drawCentredString(650, 510, "AGENTLIGI HUZURIDAGI")
    pdf.setFont('Montserrat-Bold', 17)
    pdf.drawCentredString(650, 490, "ILMIY-O‘QUV AMALIY")
    pdf.setFont('Montserrat-Bold', 17)
    pdf.drawCentredString(650, 470, "MARKAZI")

    pdfmetrics.registerFont(TTFont('Montserrat-SemiBold', 'Fonts/static/Montserrat-SemiBold.ttf'))
    pdf.setFont("Montserrat-SemiBold", 60)
    pdf.drawCentredString(420, 370, "SERTIFIKAT")

    pdfmetrics.registerFont(TTFont('Arimo-Italic', 'Fonts/static/Arimo-VariableFont_wght.ttf'))
    pdf.setFont("Arimo-Italic", 30)
    number = str(ob.cer_nomer)
    x = number.zfill(6)
    pdf.drawCentredString(420, 330, f"GN {x}")

    pdf.setFont("Arimo-Italic", 20)
    pdf.drawCentredString(350, 630, "Malaka oshirish haqida")

    pdfmetrics.registerFont(TTFont('GreatVibes-Regular', 'Fonts/static/GreatVibes-Regular.ttf'))
    pdf.setFont("GreatVibes-Regular", 40)
    pdf.drawCentredString(420, 270, f"{ob.first_name} {ob.last_name} {ob.middle_name}")

    pdf.setFont("Arimo-Italic", 18)
    pdf.drawCentredString(420, 210, "Test sinovlarini o‘tkazish bo‘yicha bino rahbari va guruh ")
    pdf.setFont("Arimo-Italic", 18)
    pdf.drawCentredString(420, 190, f"nazoratchilarini o‘qitish uchun belgilangan malaka oshirish")
    pdf.setFont("Arimo-Italic", 18)
    pdf.drawCentredString(420, 170, f"kursida (12 soat) muvofaqiyatli ishtiroki uchun taqdim etildi ")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(100, 120, f"Ilmiy-o‘quv amaliy markazi")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(88, 110, f"boshliq: Baratov A.A")

    # QR code
    image = "media/qr_codes/" + f'{code}.png'
    pdf.drawInlineImage(image, 50, 50, 50, 50)

    pdf.setFont("Arimo-Italic", 14)
    pdf.drawCentredString(270, 100, f"Berilgan sanasi")
    year_str = ob.created_at.strftime('%Y')
    day_str = ob.created_at.strftime('%d')
    month_str = ob.created_at.strftime('%m')
    pdf.drawCentredString(270, 120, f"{day_str}.{month_str}.{year_str}")
    pdf.line(225, 115, 320, 115)

    pdf.setFont("Arimo-Italic", 14)
    pdf.drawCentredString(580, 100, f"Qayd raqami ")
    pdf.setFont("Arimo-Italic", 14)
    pdf.drawCentredString(580, 120, f"{ob.registered_number}")
    pdf.line(530, 115, 620, 115)

    pdf.save()
