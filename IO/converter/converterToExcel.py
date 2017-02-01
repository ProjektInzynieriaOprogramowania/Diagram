"""@package converter
    Module to convert schedule data to excel
    """
import xlwt
import os


class ConverterToExcel:
    """
    class to convert schedule data to excel
    """

    def __init__(self):
        """Constructor"""
        self.rowIndex = 0
        self.columnwidth = {}

    def _genRow(self, sh, i, elem):
        """ helper class to add next row and increment row index """

        # simulate auto fit cell
        if self.rowIndex in self.columnwidth:
            if len(elem) > self.columnwidth[self.rowIndex]:
                self.columnwidth[self.rowIndex] = len(elem)
        else:
            self.columnwidth[self.rowIndex] = len(elem)

        sh.write(i, self.rowIndex, elem)
        self.rowIndex += 1

    def _genCol(self, sh, i, elem):
        """
        helper class to add next row and increment row index
        """

        # simulate auto fit cell
        if i in self.columnwidth:
            if len(elem) > self.columnwidth[i]:
                self.columnwidth[i] = len(elem)
        else:
            self.columnwidth[i] = len(elem)

        sh.write(1, i, elem)

    def convert(self, schedule, path, name, schedule_title):
        """Run the convert data to PDF"""
        if len(schedule) == 0:
            raise Exception("nothing to do")

        # Create path to generate file
        filename = os.path.join(path, name + ".xls")

        book = xlwt.Workbook()
        sh = book.add_sheet(name)

        # Add title
        style = "align: horiz center"
        sh.write_merge(0, 0, 0, 6, schedule_title, xlwt.easyxf(style))

        # Add title to column
        titles = ["Data zajec", "Od", "Do", "Przedmiot", "Prowadzacy", "Sala", "Forma zajec"]
        for i, title in enumerate(titles):
            self._genCol(sh, i, title)

        # Add all data to right row and column
        for i, elem in enumerate(schedule, start=2):
            self._genRow(sh, i, elem.date.strftime("%Y/%m/%d %A"))
            self._genRow(sh, i, elem.stime.strftime("%H:%M"))
            self._genRow(sh, i, elem.etime.strftime("%H:%M"))
            self._genRow(sh, i, elem.subject.name)
            self._genRow(sh, i, elem.lecturer.name)
            self._genRow(sh, i, str(elem.classroom))
            self._genRow(sh, i, elem.subject.form)
            self.rowIndex = 0

        # set corect width cell. Simulate auto fit
        for column, width in self.columnwidth.items():
            sh.col(column).width = (width + 2) * 367

        book.save(filename)
        print(filename)
