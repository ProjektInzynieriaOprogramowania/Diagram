## @package academic
#  academic package contains representation schedule items
#  #

class Lecturer:
    """
    Class representing the lecturer
    """
    def __init__(self, name):
        """Constructor"""
        self.name = name

    def __repr__(self):
        return "Lecturer<{}>".format(self.name)

    def __str__(self):
        return "{}".format(self.name)


class ClassRoom:
    """
    Class representing class room
    attribute:
        building
        number
    """
    def __init__(self, building, number):
        """Constructor"""
        self.building = building
        self.number = number

    def __repr__(self):
        return "ClassRoom<{}, {}>".format(self.building, self.number)

    def __str__(self):
        return "{} - {}".format(self.building, self.number)


class AcademicClass:
    """
    Class representing the single academic year
    attribute:
        department on university
        specialization
        semestr
        group
    """
    def __init__(self, department, specialization, semestr, group):
        """Constructor"""
        self.department = department
        self.specialization = specialization
        self.semestr = semestr
        self.group = group

    def __repr__(self):
        return "AcademicClass<{}, {}, {}, {}>".format(self.department, self.specialization, self.semestr, self.group)

    def __str__(self):
        return "{} {}, semestr {}, gr {}".format(self.department, self.specialization, self.semestr, self.group)


class Subject:
    """
    Class representing the single subject
    attribute:
        name subject
        form ("Lecture", "seminars", "lab")
    """
    classForm = {
        "w": "Wyklad",
        "p": "cwiczenia praktyczne",
        "s": "zajecia seminaryjne"
        }

    def __init__(self, name, form):
        """Constructor"""
        self.name = name
        self.form = Subject.classForm[form]

    def __repr__(self):
        return "Subject<{}, {}>".format(self.name, self.form)

    def __str__(self):
        return "{} {}".format(self.name, self.form)


class Lesson:
    """
    Class representing single reservation for lecturer, room or academic class
    attribute:
        lecturer
        class room
        academic year
        subject
        date
        start time booking
        end time booking
    """
    def __init__(self, lecturer, classroom, academic_class, subject, date, stime, etime):
        """Constructor"""
        self.lecturer = lecturer
        self.classroom = classroom
        self.academic_class = academic_class
        self.subject = subject
        self.date = date
        self.stime = stime
        self.etime = etime

    def __repr__(self):
        return "Lesson<{}, {}, {}, {}, {}, {}, {}>".format(self.lecturer,
                                                           self.classroom,
                                                           self.academic_class,
                                                           self.subject,
                                                           self.date,
                                                           self.stime,
                                                           self.etime)

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.lecturer,
                                                   self.classroom,
                                                   self.academic_class,
                                                   self.subject,
                                                   self.date,
                                                   self.stime,
                                                   self.etime)
