"""@package exporter
    Module managing converter
"""
from converter.converterToExcel import ConverterToExcel
from converter.converterToPDF import ConverterToPDF


list_converter = [ConverterToExcel, ConverterToPDF]


def exporter(converter_type, path, schedule, name, schedule_title):
    """
    Function to run suitable converter
    -----
    converter_type:
        0 - converterToExcel
        1 - converterToPDF
    """
    if converter_type >= len(list_converter):
        raise Exception("incorect converter")
    converter = list_converter[converter_type]()
    converter.convert(schedule, path, name, schedule_title)

