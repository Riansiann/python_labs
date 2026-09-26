def format_record(rec: tuple[str, str, float]) -> str:
    """
    Returns a formatted string containing a student's last name, initials, group, and GPA.
    Raises:
    ValueError: If the record does not contain three elements,
        the full name is empty or invalid, the group is empty,
        or the GPA is outside the range from 0.0 to 5.0.
    TypeError: If GPA is not a number.
    """
    if len(rec) != 3:
            raise ValueError('Record must contain 3 elements: full name, group, and GPA. Check that you have entered all the necessary information, separated by commas.')

    fio, group, gpa = rec
    fio = fio.strip()
    group = group.strip()
    
    if not fio:
        raise ValueError('Full name cannot be empty')
    name_parts = fio.split()
    if len(name_parts) not in (2, 3):
        raise ValueError('Full name must contain at least Surname and First name')
    surname = name_parts[0].capitalize()
    initials = ''.join(part[0].upper() + '.' for part in name_parts[1:])
    
    if not group:
        raise ValueError('Group cannot be empty')
  
    if not isinstance(gpa, (int, float)):
        raise TypeError('GPA must be a number.')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA must be in the range from 0.0 to 5.0.')
    
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'

#test cases
print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))

    
    