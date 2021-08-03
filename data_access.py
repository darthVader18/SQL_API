import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CPJ8BK2;'
                      'Database=Chaitanya;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


def add_student_data(_id, first_name, last_name, phone_number, email_address, grade_id):
    try:
        query = "INSERT INTO students VALUES(?,?,?,?,?,?)"
        cursor.execute(query, [_id, first_name, last_name, phone_number, email_address, grade_id])
        conn.commit()
        return {"status": 200, "message": "Data saved successfully"}

    except:
        return {"status": 400, "message": "Something is wrong, Please check!!"}
    
 

def delete_student_data(_id):
    print(_id)
    try:
        deleteQuery = "DELETE FROM students WHERE id = ?"
        cursor.execute(deleteQuery, [_id])
        conn.commit()
        return "Data deleted successfully!"
    except:
        return "No record found to delete."



def update_student_data(_id = None, first_name = None, last_name = None, phone_number = None, email_address = None, grade_id = None, find_id = None):
    print(_id, first_name, last_name, phone_number, email_address, grade_id, find_id)
    
    try:
        query = "UPDATE students SET id = ?, first_name = ?, last_name = ?, phone_number = ?, email_address = ?, grade_id = ? WHERE id = ?"
        cursor.execute(query, [_id, first_name, last_name, phone_number, email_address, grade_id, find_id])
        conn.commit()
        return "Data Updated Successfully"
            
    except:
        return "No record found to update."
            


def read_student_data(_id):
    try:
        query = "SELECT * FROM students WHERE id = ?"
        cursor.execute(query, [_id])
        for row in cursor:
            return ('row = %r' % (row,))

    except:
        return "Data is not in the list."



def add_teacher_data(_id, first_name, last_name, phone_number, email_address):
    try:
        query = "INSERT INTO teachers VALUES(?,?,?,?,?)"
        cursor.execute(query, [_id, first_name, last_name, phone_number, email_address])
        conn.commit()
        return "Data Saved Successfully"
    except:
        return "Something worng, please check"



def delete_teacher_data(_id):
    try:
        deleteQuery = "DELETE FROM teachers WHERE id = ?"
        cursor.execute(deleteQuery, [_id])
        conn.commit()
        return "Data deleted successfully!"
    except:
        return "No record found to delete."


def update_teacher_data(_id = None, first_name = None, last_name = None, phone_number = None, email_address = None, find_id = None):
    try:
        query = "UPDATE teachers SET id = ?, first_name = ?, last_name = ?, phone_number = ?, email_address = ? WHERE id = ?"
        cursor.execute(query, [_id, first_name, last_name, phone_number, email_address, find_id])
        conn.commit()
        return "Data Updated Successfully"
            
    except:
        return "No record found to update."

def read_teacher_data(_id):
    try:
        query = "SELECT * FROM teachers WHERE id = ?"
        cursor.execute(query, [_id])
        for row in cursor:
            return ('row = %r' % (row,))
        
    except:
        return "Data is not in the list."


def add_subject_data(_id, text):
    try:
        query = "INSERT INTO subjects VALUES(?,?)"
        cursor.execute(query, [_id, text])
        conn.commit()
        return {"status": 200, "message": "Data saved successfully"}

    except:
        return {"status": 400, "message": "Something is wrong, Please check!!"}


def delete_subject_data(text):
    try:
        deleteQuery = "DELETE FROM subjects WHERE text = ?"
        cursor.execute(deleteQuery, [text])
        conn.commit()
        return "Data deleted successfully!"
    except:
        return "No record found to delete."


def update_subject_data(_id = None, text = None, find_text = None):
    try:
        query = "UPDATE subjects SET id = ?, text = ? WHERE text = ?"
        cursor.execute(query, [_id, text, find_text])
        conn.commit()
        return "Data Updated Successfully"
            
    except:
        return "No record found to update."

