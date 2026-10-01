def format_record(rec: tuple[str, str, float]) -> str:
    """
    Returns a formatted string containing a student's surname, initials,
    group, and GPA.
    Raises:
    ValueError:
        If the record does not contain three elements.
        If the full name is empty or does not contain 2 or 3 parts.
        If any part of the full name contains non-alphabetic characters.
        If the group is empty.
        If the GPA is outside the range from 0.0 to 5.0.

    TypeError:
        If the record is not a tuple.
        If the full name is not a string.
        If the group is not a string.
        If the GPA is not a number (int or float), including bool.
    """
    if not isinstance(rec, tuple):
        raise TypeError('Record must be a tuple')
    if len(rec) != 3:
            raise ValueError('Record must contain 3 elements: full name, group, and GPA. Check that you have entered all the necessary information, separated by commas.')

    fio, group, gpa = rec
    

    if not fio:
        raise ValueError('Full name cannot be empty')
    if not isinstance(fio, str):
        raise TypeError('Full name must be a string')

    name_parts = fio.strip().split()

    if len(name_parts) not in (2, 3):
        raise ValueError('Full name must contain at least Surname and First name')
    if any(not part.isalpha() for part in name_parts):
        raise ValueError("Full name must contain only alphabetic characters")

    surname = name_parts[0].capitalize()
    initials = ''.join(part[0].upper() + '.' for part in name_parts[1:])


    if not group:
        raise ValueError('Group cannot be empty')
    if not isinstance(group, str):
        raise TypeError('Group must be a string')
    group = group.strip()
  
    if isinstance(gpa,bool) or not isinstance(gpa, (int, float)):
        raise TypeError('GPA must be a number.')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA must be in the range from 0.0 to 5.0.')
    
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'

#test cases

# print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
# print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
# print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
# print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))


#additional test cases for checking ValueError

# print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))
# print(format_record( (" Анна ", "ACC-01", 3.7) ))
# print(format_record( ("  ", "ABB-01", 3.999) ))
# print(format_record( ("Петров Пётр", "", 3.999) ))
# print(format_record( ("Пе67ов Пётр Пет42вич", "IKBO-12", 5.0) ))

#additional test cases for checking TypeError

# print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", "3.999") ))
# print(format_record( ("Петров Пётр", "IKBO-12", True) ))
# print(format_record( (["Иванов Иван"], "BIVT-25", 3.999) ))
print(format_record( ["Иванов Иван", "BIVT-25", 4.6] ))
