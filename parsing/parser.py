import csv  #library for parsing the csv file
from datetime import datetime #library for dealing with datetime strings


#class for a data point, each row in the csv should be able to
#be easily translated into a data class object aside from the tags
#column which has it's own class
#JH
class Data:
    student_name = ''
    student_email = ''
    student_id = ''
    #student_alt_id = '' REMOVED FROM FILE JH
    classification = ''
    major = ''
    #assigned_staff = '' REMOVED FROM FILE JH
    #care_unit = '' REMOVED FROM FILE JH
    services = ''
    #course_name = '' REMOVED FROM FILE JH
    #course_number = '' REMOVED FROM FILE JH
    location = ''
    check_in_date = ''
    check_in_time = ''
    check_out_date = ''
    check_out_time = ''
    check_in_duration = ''
    staff_name = ''
    staff_id = ''
    staff_email = ''

    def get_insert_statement(self):
        insert_val_names = ['student_name','student_email','student_id','services','location','check_in_date', 'check_in_time', 'check_out_date', 'check_out_time', 'check_in_duration', 'staff_name', 
'staff_email', 'staff_id']
        insert_val_list = [self.student_name, self.student_email, self.student_id, self.services, self.location.replace('_',' '),
        datetime.strptime(self.check_in_date, '%m/%d/%y').strftime('%Y-%m-%d'), self.check_in_time,
        datetime.strptime(self.check_out_date, '%m/%d/%y').strftime('%Y-%m-%d'), self.check_out_time, self.check_in_duration, self.staff_name, self.staff_email, self.staff_id];
        insert_val_list = ['\"' + str(a) + '\"' for a in insert_val_list];

        return 'INSERT INTO visits (' + ', '.join(insert_val_names) + ') VALUES (' + ', '.join(insert_val_list) + ');'


#Class for tags that mirrors how it's stored in the database
#student_id is for linking it to the student profile
#JH
class Tag:
    student_id = ''
    tag = ''
    date = ''


#pulls raw data from a csvfile
#Params csvfile: the csvfile to pull raw data from
#Returns data: a list of raw data rows from the csvfile
#JH
def raw_data(csvfile):
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
        data.append(row)
    return data

def sublist_finder(data, name):
    for nested_list in data:
        if name in nested_list:
            return data.index(nested_list)

    # Not found (should not reach this point)
    return -1


#Iterates over the rows in the raw data transforming the
#relevant data into a data class and tag class object for each row
#Params csvfile: the csv file to be parsed
#Returns formatted: a list of data class objects
#Returns tags: a list of tag class objects
#JH
def parse_report(csvfile):
    data = raw_data(csvfile)
    formatted = []
    tags = []
    staff = []
    if data[0][1] != "Check-Ins":
        return "ERROR", "Invalid header in navigate file."
    #Jumps to the column headers part of the file
    titles = data[sublist_finder(data, 'Student Name')]

    #Jumps to the data portion of the file
    data = data[(sublist_finder(data, 'Student Name') + 1):]
    for point in data:
        if point:
            formatted.append(format_data(titles, point))
            format_tag(titles, point, tags)
    return formatted, tags


#formats raw tag string data into a list of tag objects
#Params titles: list of column headers from the csvfile
#       raw   : the raw tag string data from the csvfile
#       tags  : a list of all of the tags parsed so far
#Returns None
#Mutates the tags parameter to be appended with the formatted tags
#JH
def format_tag(titles, raw, tags):
    tag_list = raw[titles.index('Tags')].split(',')
    student_id = raw[titles.index('Student ID')]
    if not tag_list[0]:
        return
    for tag in tag_list:
        new_tag = Tag()
        new_tag.student_id = student_id
        new_tag.tag = tag
        tags.append(new_tag)

#formats a row of data into a data class object
#Params titles: list of column headers from the csvfile
#       raw   : the raw data row from the csvfile
#Returns None if the data is empty
#Returns a data class object if the data is not empty
#JH
def format_data(titles, raw):
    if not raw:
        return
    data = Data()
    data.student_name = raw[titles.index('Student Name')]
    data.student_email = raw[titles.index('Student E-mail')]
    data.student_id = raw[titles.index('Student ID')]
    data.classification = raw[titles.index('Classification')]
    data.major = raw[titles.index('Major')]
    data.services = raw[titles.index('Services')]
    data.location = raw[titles.index('Location')]
    data.check_in_date = raw[titles.index('Check In Date')]
    data.check_in_time = raw[titles.index('Check In Time')]
    data.check_out_date = raw[titles.index('Check Out Date')]
    data.check_out_time = raw[titles.index('Check Out Time')]
    data.check_in_duration = raw[titles.index('Checked In Duration (In Min)')]
    data.staff_name = raw[titles.index('Staff Name')]
    data.staff_id = raw[titles.index('Staff ID')]
    data.staff_email = raw[titles.index('Staff E-mail')]
    return data
