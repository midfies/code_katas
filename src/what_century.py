"""Codewars problem What Century is it?."""


"""codewars problem for determining what century it is given a year."""


def what_century(year):
    """Return the century given a year."""
    if str(year)[2:] == '00':
        century = str(year)[:2]
    else:
        century = str(int(str(year)[:2]) + 1)
    if int(century) > 4 and int(century) < 14:
        century += 'th'
    else:
        if century[1:] == '1':
            century += 'st'
        elif century[1:] == '2':
            century += 'nd'
        elif century[1:] == '3':
            century += 'rd'
        else:
            century += 'th'
    return century
