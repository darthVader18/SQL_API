import data_access 

def add_student_data(_id, first_name, last_name, phone_number, email_address, grade_id):
    data =  data_access.add_student_data(_id, first_name, last_name, phone_number, email_address, grade_id)
    return data

def delete_student_data(_id):
    data = data_access.delete_student_data(_id)
    return data

def update_student_data(_id, first_name, last_name, phone_number, email_address, grade_id, find_id):
    data = data_access.update_student_data(_id, first_name, last_name, phone_number, email_address, grade_id, find_id)
    return data

def read_student_data(_id):
    data = data_access.read_student_data(_id)
    return data

def add_teacher_data(_id, first_name, last_name, phone_number, email_address):
    data =  data_access.add_teacher_data(_id, first_name, last_name, phone_number, email_address)
    return data

def delete_teacher_data(_id):
    data = data_access.delete_teacher_data(_id)
    return data

def update_teacher_data(_id, first_name, last_name, phone_number, email_address, find_id):
    data = data_access.update_teacher_data(_id, first_name, last_name, phone_number, email_address, find_id)
    return data

def read_teacher_data(_id):
    data = data_access.read_teacher_data(_id)
    return data

def add_subject_data(_id, text):
    data = data_access.add_subject_data(_id, text)
    return data

def delete_subject_data(text):
    data = data_access.delete_subject_data(text)
    return data

def update_subject_data(_id, text, find_text):
    data = data_access.update_subject_data(_id, text, find_text)
    return data