"""@package check_exporter
    module simulate receive data to generate schedule
"""
from exporter import exporter
import datetime

from operator import attrgetter

from academic.schedule_type import ClassRoom, Lecturer, AcademicClass, Subject, Lesson


def create_data_for_student():
    ekonomika = Subject("Ekonomika i Zarzadzanie", "w")
    mes = Subject("Metody elementow skonczonych", "w")
    io = Subject("Inzynieria oprogramowania", "p")
    pr = Subject("programowanie rownolegle", "w")

    room510 = ClassRoom("b5", "510")
    room709 = ClassRoom("b5", "709")
    room601 = ClassRoom("b5", "601")

    eko_lec = Lecturer("dr inż. Krzysztof Zielinsk")
    mes_lec = Lecturer("prof. dr hab. Andriy Milenin")
    io_lec = Lecturer("mgr inż. Kazimierz Michalik")
    pr_lec = Lecturer("dr hab. inż. Krzysztof Banas")

    academic_class = AcademicClass("WIMIiP", "Informatyka stosowana", 7, 3)

    schedule_title = "Plan zajec dla {}".format(str(academic_class))

    lessons = []

    lessons.append(Lesson(mes_lec, room709, academic_class, mes, datetime.date(2017, 1, 28), datetime.time(8), datetime.time(10, 15)))
    lessons.append(Lesson(io_lec, room601, academic_class, io, datetime.date(2017, 1, 28), datetime.time(16, 30), datetime.time(19)))
    lessons.append(Lesson(pr_lec, room709, academic_class, pr, datetime.date(2017, 1, 29), datetime.time(8), datetime.time(10, 15)))
    lessons.append(Lesson(eko_lec, room510, academic_class, ekonomika, datetime.date(2017, 1, 27), datetime.time(17, 30), datetime.time(19)))
    lessons.append(Lesson(io_lec, room601, academic_class, io, datetime.date(2017, 1, 28), datetime.time(14), datetime.time(16, 15)))
    lessons.append(Lesson(eko_lec, room510, academic_class, ekonomika, datetime.date(2017, 1, 27), datetime.time(15), datetime.time(17, 15)))

    return (lessons, schedule_title)


def create_data_for_lecturer():
    io = Subject("Inzynieria oprogramowania", "p")

    room510 = ClassRoom("b5", "510")
    room601 = ClassRoom("b5", "601")

    io_lec = Lecturer("mgr inż. Kazimierz Michalik")

    academic_class = AcademicClass("WIMIiP", "Informatyka stosowana", 7, 3)

    schedule_title = "Plan zajec dla {}".format(str(io_lec))

    lessons = []

    lessons.append(Lesson(io_lec, room601, academic_class, io, datetime.date(2017, 1, 28), datetime.time(16, 30), datetime.time(19)))
    lessons.append(Lesson(io_lec, room510, academic_class, io, datetime.date(2017, 1, 28), datetime.time(14), datetime.time(16, 15)))

    return (lessons, schedule_title)


def create_data_for_class_room():
    ekonomika = Subject("Ekonomika i Zarzadzanie", "w")
    mes = Subject("Metody elementow skonczonych", "w")
    io = Subject("Inzynieria oprogramowania", "p")
    pr = Subject("programowanie rownolegle", "w")

    room709 = ClassRoom("b5", "709")

    eko_lec = Lecturer("dr inż. Krzysztof Zielinsk")
    mes_lec = Lecturer("prof. dr hab. Andriy Milenin")
    io_lec = Lecturer("mgr inż. Kazimierz Michalik")
    pr_lec = Lecturer("dr hab. inż. Krzysztof Banas")

    academic_class = AcademicClass("WIMIiP", "Informatyka stosowana", 7, 3)

    schedule_title = "Plan zajec dla {}".format(str(room709))

    lessons = []

    lessons.append(Lesson(mes_lec, room709, academic_class, mes, datetime.date(2017, 1, 28), datetime.time(8), datetime.time(10, 15)))
    lessons.append(Lesson(pr_lec, room709, academic_class, pr, datetime.date(2017, 1, 29), datetime.time(8), datetime.time(10, 15)))
    lessons.append(Lesson(io_lec, room709, academic_class, io, datetime.date(2017, 1, 28), datetime.time(14), datetime.time(16, 15)))
    lessons.append(Lesson(eko_lec, room709, academic_class, ekonomika, datetime.date(2017, 1, 27), datetime.time(15), datetime.time(17, 15)))

    return (lessons, schedule_title)

if __name__ == "__main__":
    #####################################
    # Generate excel for academic class #
    #####################################
    list_lessons, schedule_title = create_data_for_student()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(0, 'generate_file', list_lessons, "rok_akademicki", schedule_title)

    #####################################
    # Generate PDF for academic class   #
    #####################################
    list_lessons, schedule_title = create_data_for_student()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(1, 'generate_file', list_lessons, "rok_akademicki", schedule_title)

    #####################################
    # Generate excel for Lecturer       #
    #####################################
    list_lessons, schedule_title = create_data_for_lecturer()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(0, 'generate_file', list_lessons, "wykladowca", schedule_title)

    #####################################
    # Generate PDF for Lecturer         #
    #####################################
    list_lessons, schedule_title = create_data_for_student()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(1, 'generate_file', list_lessons, "rok_akademicki", schedule_title)

    #####################################
    # Generate excel for class room     #
    #####################################
    list_lessons, schedule_title = create_data_for_class_room()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(0, 'generate_file', list_lessons, "pokuj", schedule_title)

    #####################################
    # Generate PDF for class room       #
    #####################################
    list_lessons, schedule_title = create_data_for_class_room()
    list_lessons = sorted(list_lessons, key=attrgetter("date", "stime"))
    exporter(1, 'generate_file', list_lessons, "pokuj", schedule_title)
