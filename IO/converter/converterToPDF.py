"""@package converter
    Module to convert schedule data to PDF
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer, TableStyle

import os


class ConverterToPDF:
    """
    class to convert schedule data to PDF
    """

    def __init__(self):
        """Constructor"""

        self.width, self.height = letter
        self.styles = getSampleStyleSheet()

    def _coord(self, x, y, unit=1):
        """
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height - y * unit
        return x, y

    def convert(self, schedule, path, name, schedule_title):
        """
        Run the convert data to PDF
        """
        if len(schedule) == 0:
            raise Exception("nothing to do")

        self.schedule = schedule
        self.schedule_title = schedule_title

        # Create path to generate file
        filename = os.path.join(path, name + ".pdf")

        self.doc = SimpleDocTemplate(filename)
        self.story = [Spacer(1, 0.5*inch)]
        self._createLineItems()

        self.doc.build(self.story, onFirstPage=self._createDocument)
        print(filename)

    def _createDocument(self, canvas, doc):
        """
        Create the document
        """
        normal = self.styles["Normal"]

        header_text = "<h1><b>{}</b></h1>".format(self.schedule_title)
        p = Paragraph(header_text, normal)
        p.wrapOn(canvas, self.width, self.height)
        p.drawOn(canvas, *self._coord(50, 12, mm))

    def _createLineItems(self):
        """
        Create table with schedule
        """
        titles = ["Data zajec", "Od", "Do", "Przedmiot", "Prowadzacy", "Sala", "Forma zajec"]
        d = []
        font_size = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in titles:
            ptext = "<font size=%s><b>%s</b></font>" % (font_size, text)
            p = Paragraph(ptext, centered)
            d.append(p)

        data = [d]

        line_num = 1

        formatted_line_data = []

        for elem in self.schedule:
            line_elem = [elem.date.strftime("%Y/%m/%d %A"),
                         elem.stime.strftime("%H:%M"),
                         elem.etime.strftime("%H:%M"),
                         elem.subject.name,
                         elem.lecturer.name,
                         str(elem.classroom),
                         elem.subject.form
                         ]

            for item in line_elem:
                ptext = "<font size=%s>%s</font>" % (font_size-1, item)
                p = Paragraph(ptext, centered)
                formatted_line_data.append(p)
            data.append(formatted_line_data)
            formatted_line_data = []
            line_num += 1

        tstyle = [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                  ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]
        table = Table(data)
        table.setStyle(TableStyle(tstyle))

        self.story.append(table)
